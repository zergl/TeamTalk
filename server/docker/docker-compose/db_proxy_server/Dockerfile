FROM teamtalk/base_iamge:v20171212

MAINTAINER zergl e3.gemini@qq.com

#RUN groupadd -r teamtalk && useradd -r -g teamtalk teamtalk
ENV BIN_NAME="db_proxy_server"
ENV RUN_DIR="/teamtalk/"

LABEL architecture="x86_64" \
	name="teamtalk/${BIN_NAME}" \
	vendor="github.com/zergl"

RUN mkdir -p ${RUN_DIR}
ADD ${BIN_NAME} ${RUN_DIR}
RUN chmod 655 "${RUN_DIR}/${BIN_NAME}"
ADD ${BIN_NAME}.conf ${RUN_DIR}
ADD log4cxx.properties ${RUN_DIR}

EXPOSE 10600

RUN chown -R teamtalk:teamtalk ${RUN_DIR}
WORKDIR ${RUN_DIR}
CMD ["./db_proxy_server"]

