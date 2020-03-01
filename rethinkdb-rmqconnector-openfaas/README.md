# rethinkdsb-rmqconnector-openfaas skeleton

Skeleton project that combines the below features to create a scalable database-event-driven function-as-a-service architecture.

* [RethinkDB Changefeeds](https://rethinkdb.com/docs/changefeeds/python/) - push-based data access
* [OpenFaaS](https://www.openfaas.com/) - provides invokable 'functions', each within isolated container environments
* [Rabbitmq-connector](https://github.com/Templum/rabbitmq-connector) - invokes OpenFaas functions via user-defined database events (e.g. create,update,insert,delete)

## Setup

### OpenFaaS

* Install OpenFaas CLI

```bash
curl -sL https://cli.openfaas.com | sudo sh
```

* Install Docker
* Initialize Docker Swarm
```bash
docker swarm init
```

* Deploy a vanilla stack

```bash
git clone https://github.com/openfaas/faas && \
  cd faas && \
  ./deploy_stack.sh
```

* **Make note of the generated admin password!**

* Verify Gateway ui at http://127.0.0.1:8080

### Database and RabbitMQ

* Configure your OpenFaaS credentials in .auth/user.txt and .auth/pass.txt
* Build and bring RethinkDB, RabbitMQ, and Connector up:

```bash
docker-compose up -d
```

* Verify RethinkDB at: http://127.0.0.1:8081
* Verify RabbitMQ at : http://127.0.0.1:5672

* Initialize DB models and changefeeds (table bindings to rabbitmq)

```bash
virtualenv -p python3 skeleton
source skeleton/bin/activate
cd images/base/skeleton
python3 setup.py install
python3 init.py
```

* Deploy functions in stack

```bash
faas-cli deploy -f stack.yml
```
