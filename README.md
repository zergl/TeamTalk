### modified by [zergl](https://github.com/zergl/TeamTalk)
不为别的，纯属无聊。

1. Windows下编译通过;

    - base -- 编译成功
    - db_proxy_server
    - file_server
    - http_msg_server
    - login_server -- 编译通过
    - msfs
    - msg_server -- 调整中
    - push_server
    - route_server
    - ...


2. 调整工程组织，使得看上去舒服点、编译也变得愉快点；

    - 第三方组件统一目录；-- 完成 (server/3rdparty)
    - 协议目录梳理；      -- 完成 (proto)
    - makefile文件重构；  -- 进行中 (cmake很强大，学习中)
    - 封装一个日志模块    -- 未开始
    - 梳理配置文件        -- 未开始
    - 简化编译&部署文档   -- 进行中
    - 配置服务器          -- 未开始（ConfigSvr）
    - 统一命名为tt_*_svr形式 -- 未开始

3. 测试

   - 性能剖析
   - 压力测试
   - …
   
4. 文档梳理

   - 部署结构图
   - 交互协议梳理
   - 代码走读
 
 
----------------------------------------------

# TeamTalk
	TeamTalk is a solution for enterprise IM
	
	具体文档见doc目录下,安装之前请仔细阅读相关文档。
	
# 交流
		建议大家在开发过程中遇到问题,提交issues到https://github.com/mogujie/TeamTalk/issues  
		
		我们的官方维护人员会抽时间解答,谢谢大家的理解.
		* qq群:341273218
