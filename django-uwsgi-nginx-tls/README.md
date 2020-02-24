# django-uwsgi-nginx-tls

A docker-compose environment for rapid prototyping web applications.  This is insecure and should be used with caution.

* Web Server
    * Django project (mysite) with single application (myapp)
    * UWSGI
    * Nginx
* Storage
    * Postgresql

For creating a production-capable Django project with HTTPS.

## Build

```bash
cd server 
./cicd/build.sh
```

## Run

```bash
docker-compose up -d
```

Various practical things that should be changed when using in a project:

* models
* tls crt/key pair
* db name
* app name