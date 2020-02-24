FROM ubuntu:bionic

RUN apt update \
 && apt install -y python3.8 \
                   python3-pip \
                   python3-dev \
                   nginx

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY mysite /root/mysite
COPY run.sh /root/mysite/run.sh
RUN chmod +x /root/mysite/run.sh

# Nginx configurations
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/enabled-site.conf /etc/nginx/sites-available/enabled-site.conf
COPY conf/tls/tls.key /etc/nginx/tls.key
COPY conf/tls/tls.crt /etc/nginx/tls.crt
COPY conf/uwsgi_params /etc/nginx/uwsgi_params
COPY conf/uwsgi.ini /root/mysite/uwsgi.ini

# enable the site
RUN ln -s /etc/nginx/sites-available/enabled-site.conf /etc/nginx/sites-enabled/

WORKDIR /root/mysite
