FROM httpd:latest

USER root
COPY assets/asset.txt /usr/local/apache2/htdocs/
COPY assets/app /app

RUN apt-get update -qq
RUN apt-get install -y apt-transport-https ca-certificates
RUN apt-get install -y sudo
RUN apt-get install -y vim
RUN apt-get install -y python python-pip
# Show minimal information, we don't want to disclouse information about the server
RUN sed -i  's/ServerTokens Full/ServerTokens Prod/' /usr/local/apache2/conf/extra/httpd-default.conf \
        /usr/local/apache2/conf/original/extra/httpd-default.conf
RUN echo "ServerTokens Prod" >> /usr/local/apache2/conf/httpd.conf
