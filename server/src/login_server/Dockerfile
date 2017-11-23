FROM centos:7.4.1708

MAINTAINER zergl e3.gemini@qq.com

ENV BIN_NAME="tt_login_server"
ENV RUN_DIR="/data/app/teamtalk/tt_login_server"

LABEL architecture="x86_64" \
	name="zergl/${BIN_NAME}" \
	vendor="github.com/zergl"

RUN yum install -y libcurl-devel libuuid-devel apr-devel apr-util-devel
RUN mkdir -p ${RUN_DIR}
ADD ${BIN_NAME} ${RUN_DIR}
ADD start.sh ${RUN_DIR}
RUN chmod 644 "${RUN_DIR}/start.sh"
#ADD ${BIN_NAME}.conf ${RUN_DIR}
ADD loginserver.conf ${RUN_DIR}
#ADD ${BIN_NAME}.log4cxx.properties ${RUN_DIR}
ADD log4cxx.properties ${RUN_DIR}
#ADD tt_login_server.service /etc/systemd/system/tt_login_server.service
#RUN chmod 644 /etc/systemd/system/tt_login_server.service
#RUN systemctl enable tt_login_server
#RUN cd ${RUN_DIR};/usr/bin/nohup /data/app/teamtalk/tt_login_server/tt_login_server >> /data/app/teamtalk/tt_login_server/tt_login_server.log 2&>1 &

EXPOSE 8080

#CMD ["/usr/sbin/init"]
#CMD ["/usr/bin/systemctl", "start ${BIN_NAME}"]
CMD ["/usr/bin/bash"]

ENTRYPOINT ${RUN_DIR}/start.sh

