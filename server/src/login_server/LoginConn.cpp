/*
 * LoginConn.cpp
 *
 *  Created on: 2013-6-21
 *      Author: ziteng@mogujie.com
 */

#include "LoginConn.h"
#include "IM.Server.pb.h"
#include "IM.Other.pb.h"
#include "IM.Login.pb.h"
#include "base/public_define.h"

using namespace IM::BaseDefine;
static ConnMap_t g_client_conn_map;
static ConnMap_t g_msg_serv_conn_map;
static uint32_t g_total_online_user_cnt = 0;    // 并发在线总人数

map<uint32_t, msg_serv_info_t*> g_msg_serv_info;

void login_conn_timer_callback(void* callback_data, uint8_t msg, uint32_t handle, void* pParam)
{
    uint64_t cur_time = get_tick_count();
    for (ConnMap_t::iterator it = g_client_conn_map.begin(); it != g_client_conn_map.end(); ) 
    {
        ConnMap_t::iterator it_old = it;
        it++;

        CLoginConn* pConn = (CLoginConn*)it_old->second;
        pConn->OnTimer(cur_time);
    }

    for (ConnMap_t::iterator it = g_msg_serv_conn_map.begin(); it != g_msg_serv_conn_map.end(); ) 
    {
        ConnMap_t::iterator it_old = it;
        it++;

        CLoginConn* pConn = (CLoginConn*)it_old->second;
        pConn->OnTimer(cur_time);
    }
}

void init_login_conn()
{
    netlib_register_timer(login_conn_timer_callback, NULL, 1000);
}

CLoginConn::CLoginConn()
{
}

CLoginConn::~CLoginConn()
{

}

void CLoginConn::Close()
{
    if (m_handle != NETLIB_INVALID_HANDLE) 
    {
        netlib_close(m_handle);
        if (m_conn_type == LOGIN_CONN_TYPE_CLIENT) 
        {
            g_client_conn_map.erase(m_handle);
        } 
        else 
        {
            g_msg_serv_conn_map.erase(m_handle);

            // remove all user count from this message server
            map<uint32_t, msg_serv_info_t*>::iterator it = g_msg_serv_info.find(m_handle);
            if (it != g_msg_serv_info.end()) 
            {
                msg_serv_info_t* pMsgServInfo = it->second;

                g_total_online_user_cnt -= pMsgServInfo->cur_conn_cnt;
                log("onclose from MsgServer: %s:%u ", pMsgServInfo->hostname.c_str(), pMsgServInfo->port);
                
                delete pMsgServInfo;
                g_msg_serv_info.erase(it);
            }
        }
    }

    ReleaseRef();
}

void CLoginConn::OnConnect2(net_handle_t handle, int conn_type)
{
    m_handle = handle;
    m_conn_type = conn_type;
    ConnMap_t* conn_map = &g_msg_serv_conn_map;
    if (conn_type == LOGIN_CONN_TYPE_CLIENT) 
    {
        conn_map = &g_client_conn_map;
    }else
        conn_map->insert(make_pair(handle, this));

    netlib_option(handle, NETLIB_OPT_SET_CALLBACK, (void*)imconn_callback);
    netlib_option(handle, NETLIB_OPT_SET_CALLBACK_DATA, (void*)conn_map);
}

void CLoginConn::OnClose()
{
    Close();
}

void CLoginConn::OnTimer(uint64_t curr_tick)
{
    if (m_conn_type == LOGIN_CONN_TYPE_CLIENT) 
    {
        //客户端连接，超时则断开
        if (curr_tick > m_last_recv_tick + CLIENT_TIMEOUT) 
        {
            Close();
        }
    } 
    else 
    {
        //定时发送心跳包给msg_server
        if (curr_tick > m_last_send_tick + SERVER_HEARTBEAT_INTERVAL) 
        {
            IM::Other::IMHeartBeat msg;
            SendPdu(SID_OTHER, CID_OTHER_HEARTBEAT, msg);
        }

        if (curr_tick > m_last_recv_tick + SERVER_TIMEOUT) 
        {
            log("connection to MsgServer timeout ");
            Close();
        }
    }
}

void CLoginConn::HandlePdu(CImPdu* pPdu)
{
    switch (pPdu->GetCommandId()) {
        case CID_OTHER_MSG_SERV_INFO:
            _HandleMsgServInfo(pPdu);
            break;
        case CID_OTHER_USER_CNT_UPDATE:
            _HandleUserCntUpdate(pPdu);
            break;
        case CID_LOGIN_REQ_MSGSERVER:
            _HandleMsgServRequest(pPdu);
            break;

        default:
            log("wrong msg, cmd id=%d ", pPdu->GetCommandId());
            break;
    }
}

msg_serv_info_t* CLoginConn::_FindMinLoadMsgSever()
{
    msg_serv_info_t* pMsgServInfo;
    msg_serv_info_t* min_ms;

    uint32_t min_user_cnt = 0; //最低在线
    map<uint32_t, msg_serv_info_t*>::iterator it;

    for (it = g_msg_serv_info.begin(); it != g_msg_serv_info.end(); it++)
    {
        pMsgServInfo = it->second;
        if ((pMsgServInfo->cur_conn_cnt < pMsgServInfo->max_conn_cnt) &&
            (pMsgServInfo->cur_conn_cnt < min_user_cnt))
        {
            min_user_cnt = pMsgServInfo->cur_conn_cnt;
            min_ms = pMsgServInfo;
        }
    }

    return min_ms;
}

void CLoginConn::_HandleMsgServInfo(CImPdu* pPdu)
{
    msg_serv_info_t* pMsgServInfo = new msg_serv_info_t;
    IM::Server::IMMsgServInfo msg;
    msg.ParseFromArray(pPdu->GetBodyData(), pPdu->GetBodyLength());
    
    pMsgServInfo->ip_addr1 = msg.ip1();
    pMsgServInfo->ip_addr2 = msg.ip2();
    pMsgServInfo->port = msg.port();
    pMsgServInfo->max_conn_cnt = msg.max_conn_cnt();
    pMsgServInfo->cur_conn_cnt = msg.cur_conn_cnt();
    pMsgServInfo->hostname = msg.host_name();
    g_msg_serv_info.insert(make_pair(m_handle, pMsgServInfo));
    log("g_msg_serv_info: %u", g_msg_serv_info.size());
    g_total_online_user_cnt += pMsgServInfo->cur_conn_cnt;

    log("MsgServInfo, ip_addr1=%s, ip_addr2=%s, port=%d, max_conn_cnt=%d, cur_conn_cnt=%d, hostname: %s. ",
        pMsgServInfo->ip_addr1.c_str(), pMsgServInfo->ip_addr2.c_str(), pMsgServInfo->port,pMsgServInfo->max_conn_cnt,
        pMsgServInfo->cur_conn_cnt, pMsgServInfo->hostname.c_str());
}

void CLoginConn::_HandleUserCntUpdate(CImPdu* pPdu)
{
    map<uint32_t, msg_serv_info_t*>::iterator it = g_msg_serv_info.find(m_handle);
    if (it == g_msg_serv_info.end())
    {
        //error log or alertmsg
        log("socket %d not found.", m_handle);
        return;
    }

    IM::Server::IMUserCntUpdate msg;
    if (!pPdu->Decode(msg))
    {
        //decode fail
        log("decode fail.");
        return;
    }

    msg_serv_info_t* pMsgServInfo = it->second;
    //@zergl: 每个用户上线、下线都来个通知信息~ 这思路…打脸啪啪啪~~~
    uint32_t incr_num = (msg.user_action() == USER_CNT_INC) ? 1 : -1;
    pMsgServInfo->cur_conn_cnt += incr_num;
    g_total_online_user_cnt += incr_num;

    log("%s:%d, cur_cnt=%u, total_cnt=%u ", pMsgServInfo->hostname.c_str(),
        pMsgServInfo->port, pMsgServInfo->cur_conn_cnt, g_total_online_user_cnt);
}

//处理客户端来的请求信息，这个是TCP协议（HttpConn里同名接口处理的是http协议）
void CLoginConn::_HandleMsgServRequest(CImPdu* pPdu)
{
    log("HandleMsgServReq. ");

    IM::Login::IMMsgServReq msg;
    if (!pPdu->Decode(msg))
    {
        log("decode failed.");
        return;
    }

    //回包
    IM::Login::IMMsgServRsp rsp_msg;
    
    if (g_msg_serv_info.size() == 0)
    {
        rsp_msg.set_result_code(::IM::BaseDefine::REFUSE_REASON_NO_MSG_SERVER);
    }
    else
    {
        // 找到负载最低的服务器
        msg_serv_info_t* ms = _FindMinLoadMsgSever();
        if (ms == NULL)
        {
            rsp_msg.set_result_code(::IM::BaseDefine::REFUSE_REASON_MSG_SERVER_FULL);
        } else {
            rsp_msg.set_result_code(::IM::BaseDefine::REFUSE_REASON_NONE);
            rsp_msg.set_prior_ip(ms->ip_addr1);
            rsp_msg.set_backip_ip(ms->ip_addr2);
            rsp_msg.set_port(ms->port);
        }
    }

    SendPdu(SID_OTHER, CID_LOGIN_RES_MSGSERVER, rsp_msg);

    Close();    // after send MsgServResponse, active close the connection
}
