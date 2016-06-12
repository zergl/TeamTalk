/*
 * login_server.cpp
 *
 *  Created on: 2013-6-21
 *      Author: ziteng@mogujie.com
 */

#include "LoginConn.h"
#include "base/netlib.h"
#include "base/ConfigFileReader.h"
#include "base/version.h"
#include "HttpConn.h"
#include "ipparser.h"

IpParser* pIpParser = NULL;
string strMsfsUrl;
string strDiscovery;//发现获取地址


// this callback will be replaced by imconn_callback() in OnConnect()
void msg_serv_callback(void* callback_data, uint8_t msg, uint32_t handle, void* pParam)
{
    log("msg_server come in");

    if (msg == NETLIB_MSG_CONNECT)
    {
        CLoginConn* pConn = new CLoginConn();
        pConn->OnConnect2(handle, LOGIN_CONN_TYPE_MSG_SERV);
    }
    else
    {
        log("!!!error msg: %d ", msg);
    }
}


void http_callback(void* callback_data, uint8_t msg, uint32_t handle, void* pParam)
{
    if (msg == NETLIB_MSG_CONNECT)
    {
        CHttpConn* pConn = new CHttpConn();
        pConn->OnConnect(handle);
    }
    else
    {
        log("!!!error msg: %d ", msg);
    }
}

int main(int argc, char* argv[])
{
    if ((argc == 2) && (strcmp(argv[1], "-v") == 0)) 
    {
        printf("Server Version: LoginServer/%s\n", VERSION);
        printf("Server Build: %s %s\n", __DATE__, __TIME__);
        return 0;
    }

    signal(SIGPIPE, SIG_IGN);

    //todo:
    //ret = load_config();
    CConfigFileReader config_file("loginserver.conf");

    char* http_listen_ip = config_file.GetConfigName("HttpListenIP");
    char* str_http_port = config_file.GetConfigName("HttpPort");
    char* msg_server_listen_ip = config_file.GetConfigName("MsgServerListenIP");
    char* str_msg_server_port = config_file.GetConfigName("MsgServerPort");
    char* str_msfs_url = config_file.GetConfigName("msfs");
    char* str_discovery = config_file.GetConfigName("discovery");

    if (!msg_server_listen_ip || !str_msg_server_port || !http_listen_ip
        || !str_http_port || !str_msfs_url || !str_discovery) 
    {
        log("config item missing, exit... ");
        return -1;
    }

    uint16_t msg_server_port = atoi(str_msg_server_port);
    uint16_t http_port = atoi(str_http_port);
    strMsfsUrl = str_msfs_url;
    strDiscovery = str_discovery;
    
    
    pIpParser = new IpParser();
    
    int ret = netlib_init();

    if (ret == NETLIB_ERROR)
        return ret;
    

    CStrExplode msg_server_listen_ip_list(msg_server_listen_ip, ';');
    for (uint32_t i = 0; i < msg_server_listen_ip_list.GetItemCnt(); i++) 
    {
        ret = netlib_listen(msg_server_listen_ip_list.GetItem(i), msg_server_port, msg_serv_callback, NULL);
        if (ret == NETLIB_ERROR)
            return ret;
    }
    
    CStrExplode http_listen_ip_list(http_listen_ip, ';');
    for (uint32_t i = 0; i < http_listen_ip_list.GetItemCnt(); i++) {
        ret = netlib_listen(http_listen_ip_list.GetItem(i), http_port, http_callback, NULL);
        if (ret == NETLIB_ERROR)
            return ret;
    }
    
    fprintf(stdout,
        "server start listen on:\n"
        "For MsgServer: %s:%d\n"
        "For http:%s:%d\n", 
        msg_server_listen_ip, 
        msg_server_port, 
        http_listen_ip, 
        http_port);

    init_login_conn();
    init_http_conn();

    printf("now enter the event loop...\n");
    
    writePid();

    netlib_eventloop();

    //todo: 直接deamonize不好么

    return 0;
}
