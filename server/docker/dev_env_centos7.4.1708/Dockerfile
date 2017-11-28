FROM centos:7.4.1708
ENV container docker
MAINTAINER "zergl" 859077290@qq.com

RUN yum -y update; yum clean all
RUN yum -y install systemd; yum clean all; 

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN yum install -y openssh-server
#RUN systemctl start sshd
#RUN systemctl enbale sshd

RUN yum install -y libcurl-devel libuuid-devel apr-devel apr-util-devel 
RUN yum install -y gcc gcc-c++ make cmake automake autoconf libtool
RUN yum install -y git vim
RUN yum clean all
RUN yum clean packages

RUN useradd -m teamtalk
WORKDIR /home/teamtalk

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]

