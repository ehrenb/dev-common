FROM ubuntu:focal
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update \
 && apt install -y python3.8 \
                   python3-pip \
                   python3-dev \
                   nginx
RUN useradd www
WORKDIR /app/mysite

COPY mysite /app/mysite
COPY run.sh /app/mysite/run.sh
RUN chmod +x /app/mysite/run.sh

# Nginx configurations
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/enabled-site.conf /etc/nginx/sites-available/enabled-site.conf
COPY conf/tls/tls.key /etc/nginx/tls.key
COPY conf/tls/tls.crt /etc/nginx/tls.crt
COPY conf/uwsgi_params /etc/nginx/uwsgi_params
COPY conf/uwsgi.ini /app/mysite/uwsgi.ini

## add permissions for www user
RUN chown -R www:www /app && chmod -R 755 /app && \
        chown -R www:www /var/log/nginx && \
        chown -R www:www /etc/nginx && \
        chown -R www:www /var/lib/nginx
RUN touch /var/run/nginx.pid && \
        chown -R www:www /var/run/nginx.pid

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# enable the site
RUN ln -s /etc/nginx/sites-available/enabled-site.conf /etc/nginx/sites-enabled/

USER www
