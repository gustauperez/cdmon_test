FROM jenkins/jenkins:latest

USER root
RUN apt-get update -qq
RUN apt-get install -y apt-transport-https ca-certificates
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
RUN echo deb https://apt.dockerproject.org/repo debian-jessie main > /etc/apt/sources.list.d/docker.list
RUN apt-get update -qq
RUN apt-get install -y sudo
RUN apt-get install -y docker-engine docker-compose
RUN apt-get install -y vim
RUN apt-get install -y maven
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

COPY jenkins.sh /
RUN chmod 755 /jenkins.sh
ENTRYPOINT ["/jenkins.sh"]
