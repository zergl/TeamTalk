/*
 * HttpConn.h
 *
 *  Created on: 2013-9-29
 *      Author: ziteng
 */

#ifndef __HTTP_CONN_H__
#define __HTTP_CONN_H__

#include "base/netlib.h"
#include "base/util.h"
#include "base/HttpParserWrapper.h"

#define HTTP_CONN_TIMEOUT   60000

#define READ_BUF_SIZE   2048
#define HTTP_RESPONSE_HTML          "HTTP/1.1 200 OK\r\n"\
                                    "Connection:close\r\n"\
                                    "Content-Length:%d\r\n"\
                                    "Content-Type:text/html;charset=utf-8\r\n\r\n%s"
#define HTTP_RESPONSE_HTML_MAX      1024

enum {
    CONN_STATE_IDLE,
    CONN_STATE_CONNECTED,
    CONN_STATE_OPEN,
    CONN_STATE_CLOSED,
};

class CHttpConn : public CRefObject
{
public:
    CHttpConn();
    virtual ~CHttpConn();

    uint32_t GetConnHandle() { return m_conn_handle; }
    char* GetPeerIP() { return (char*)m_peer_ip.c_str(); }

    int Send(void* data, int len);

    void Close();
    void OnConnect(net_handle_t handle);
    void OnRead();
    void OnWrite();
    void OnClose();
    void OnTimer(uint64_t curr_tick);
    void OnWriteComlete();
private:
    void _HandleMsgServRequest(string& url, string& post_data);

protected:
    net_handle_t m_sock_handle;
    uint32_t m_conn_handle;
    bool m_busy;

    uint32_t        m_state;
    std::string     m_peer_ip;
    uint16_t        m_peer_port;
    CSimpleBuffer   m_in_buf;
    CSimpleBuffer   m_out_buf;

    uint64_t        m_last_send_tick;
    uint64_t        m_last_recv_tick;
    
    CHttpParserWrapper m_cHttpParser;
};

//typedef hash_map<uint32_t, CHttpConn*> HttpConnMap_t;

typedef hash_map<uint32_t, CHttpConn*> HttpConnMap_t;

CHttpConn* FindHttpConnByHandle(uint32_t handle);
void init_http_conn();


//add by zergl
//todo: msfs has the same function code; so pls wrap as a common class in base module.
class HttpConnMgr
{
public:
    static HttpConnMgr * instance()
    {
        if(_inst == NULL)
        {
            _inst = new HttpConnMgr();
        }

        return _inst;
    };

    static void clean_instance()
    {
        if(_inst)
        {
            delete _inst;
            _inst = NULL;
        }
    }


    const uint32_t get_conn_num() 
    {
        return (++conn_num_);
    }

    HttpConnMap_t get_conn_map() 
    {
        return conn_map_;
    }

    CHttpConn *find_handle(const uint32_t s) 
    {
        HttpConnMap_t::iterator it = conn_map_.find(s);
        return it != conn_map_.end() ? it->second : NULL;
    }

    void erase_handle(const uint32_t s)
    {
        conn_map_.erase(s);
    }

    void register_handle(uint32_t socket_handle, CHttpConn *conn_handle)
    {
        conn_map_.insert(make_pair(socket_handle, conn_handle));
    }


private:
    static HttpConnMgr *_inst;

    uint32_t conn_num_;

    HttpConnMap_t conn_map_;

private:
    HttpConnMgr(){ conn_num_ = 0;};
    ~HttpConnMgr(){};
};

#endif /* HttpCONN_H_ */

