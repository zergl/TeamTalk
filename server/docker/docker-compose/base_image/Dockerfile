FROM centos:7.4.1708

MAINTAINER zergl 859077290@qq.com

RUN groupadd -r teamtalk && useradd -r -g teamtalk teamtalk
ENV RUN_DIR="/teamtalk/"

LABEL architecture="x86_64" \
	name="zergl/${BIN_NAME}" \
	vendor="github.com/zergl"

RUN yum install -y libcurl-devel libuuid-devel apr-devel apr-util-devel
RUN mkdir -p ${RUN_DIR}
RUN chown -R teamtalk:teamtalk ${RUN_DIR}
WORKDIR ${RUN_DIR}

