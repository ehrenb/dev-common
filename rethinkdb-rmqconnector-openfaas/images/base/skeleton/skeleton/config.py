import logging
import os

_rethinkdb_default_host = 'rethinkdb'
_rethinkdb_default_port = 28015
_rethinkdb_default_name = 'dbname' # your db name here
_rethinkdb_default_user = 'admin'
_rethinkdb_default_pass = ''

_rmq_default_host = "rabbitmq"
_rmq_default_port = 5672
_rmq_default_user = "user"
_rmq_default_pass = "pass"

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_rmq_config(rmq_default_host=_rmq_default_host,
                   rmq_default_port=_rmq_default_port,
                   rmq_default_user=_rmq_default_user,
                   rmq_default_pass=_rmq_default_pass):
    rmq_host = os.getenv('RMQ_HOST')
    if not rmq_host:
        logger.warn("RMQ_HOST defaulted to: {}".format(rmq_default_host))
        rmq_host = rmq_default_host

    rmq_port = os.getenv('RMQ_PORT')
    if not rmq_port:
        logger.warn("RMQ_PORT defaulted to: {}".format(rmq_default_port))
        rmq_port = rmq_default_port
    rmq_port = int(rmq_port)

    rmq_user = os.getenv('RMQ_USER')
    if not rmq_user:
        logger.warn("RMQ_USER defaulted to: {}".format(rmq_default_user))
        rmq_user = rmq_default_user

    rmq_pass = os.getenv('RMQ_PASS')
    if not rmq_pass:
        logger.warn("RMQ_PASS defaulted to: {}".format(rmq_default_pass))
        rmq_pass = rmq_default_pass

    return rmq_host, rmq_port, rmq_user, rmq_pass

def get_db_config(rethinkdb_default_host=_rethinkdb_default_host,
                  rethinkdb_default_port=_rethinkdb_default_port,
                  rethink_db_default_name=_rethinkdb_default_name,
                  rethinkdb_default_user=_rethinkdb_default_user,
                  rethinkdb_default_pass=_rethinkdb_default_pass):
    rethinkdb_host = os.getenv('RETHINKDB_HOST')
    if not rethinkdb_host:
        logger.warn("RETHINKDB_HOST defaulted to: {}".format(rethinkdb_default_host))
        rethinkdb_host = rethinkdb_default_host

    rethinkdb_port = os.getenv('RETHINKDB_PORT')
    if not rethinkdb_port:
        logger.warn("RETHINKDB_PORT defaulted to: {}".format(rethinkdb_default_port))
        rethinkdb_port = rethinkdb_default_port
    rethinkdb_port = int(rethinkdb_port)

    rethinkdb_name = os.getenv('RETHINKDB_NAME')
    if not rethinkdb_name:
        logger.warn("RETHINKDB_NAME defaulted to: {}".format(rethink_db_default_name))
        rethinkdb_name = rethink_db_default_name

    rethinkdb_user = os.getenv('RETHINKDB_USER')
    if not rethinkdb_user:
        logger.warn("RETHINKDB_USER defaulted to: {}".format(rethinkdb_default_user))
        rethinkdb_user = rethinkdb_default_user

    rethinkdb_pass = os.getenv('RETHINKDB_PASS')
    if not rethinkdb_pass:
        logger.warn("RETHINKDB_PASS defaulted to: {}".format(rethinkdb_default_pass))
        rethinkdb_pass = rethinkdb_default_pass

    return rethinkdb_host, rethinkdb_port, rethinkdb_name, rethinkdb_user, rethinkdb_pass