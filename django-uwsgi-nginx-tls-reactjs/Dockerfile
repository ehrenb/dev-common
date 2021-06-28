FROM ubuntu:focal

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update \
 && apt install -y python3.8 \
                   python3-pip \
                   python3-dev \
                   nginx \
                   curl \
                   vim

# NodeJS
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

RUN useradd --create-home www
WORKDIR /app/mysite

COPY mysite /app/mysite
COPY run.sh /app/mysite/run.sh
RUN chmod +x /app/mysite/run.sh

# Nginx configurations
COPY nginx/conf/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf/enabled-site.conf /etc/nginx/sites-available/enabled-site.conf
COPY nginx/conf/tls/tls.key /etc/nginx/tls.key
COPY nginx/conf/tls/tls.crt /etc/nginx/tls.crt
COPY nginx/conf/uwsgi_params /etc/nginx/uwsgi_params
COPY nginx/conf/uwsgi.ini /app/mysite/uwsgi.ini

## add permissions for www user
RUN chown -R www:www /app && chmod -R 755 /app && \
        chown -R www:www /var/log/nginx && \
        chown -R www:www /etc/nginx && \
        chown -R www:www /var/lib/nginx

RUN touch /var/run/nginx.pid && \
        chown -R www:www /var/run/nginx.pid
#        chown -R www:www /var/cache/nginx && \
#        chown -R www:www /etc/nginx/conf.d && \

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

RUN cd /app/mysite/frontend && npm install


# enable the site
RUN ln -s /etc/nginx/sites-available/enabled-site.conf /etc/nginx/sites-enabled/

USER www
