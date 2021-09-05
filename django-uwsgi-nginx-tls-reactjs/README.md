# django-uwsgi-nginx-tls-reactjs

A docker-compose environment for rapid prototyping web applications w/ reactjs.  This is insecure and should be used with caution.

* Web Server
    * Django project (mysite) with single application (myapp)
    * UWSGI
    * Nginx
    * reactjs
* Storage
    * Postgresql

For creating a production-capable Django project with HTTPS.

## Build

```bash
docker-compose build
```

## Run

```bash
docker-compose up -d
```

Various practical things that should be changed when using in a project:

* models
* tls crt/key pair

```bash
openssl req -nodes -x509 -newkey rsa:4096 -keyout nginx/conf/tls/tls.key -out nginx/conf/tls/tls.crt -days 36500
```

* db name
* app name
