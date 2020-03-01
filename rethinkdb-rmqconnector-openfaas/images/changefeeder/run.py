#!/usr/bin/env python3

'''Listens for changes on a rethinkdb table and sends them over a
RabbitMQ topic exchange.
The topic will be <tablename>.<type_of_change> where type_of_change is
create, delete or update.'''
import logging

import pika
from rethinkdb import r

from skeleton.config import get_db_config, get_rmq_config
from skeleton.db.init import init_db

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_host, db_port, db_name, db_user, db_pass = get_db_config()
rmq_host, rmq_port, rmq_user, rmq_pass = get_rmq_config()

# Setup RethinkDB connection
logger.info("attempting to connect to rethink db instance")
rethink_conn = r.connect(host=db_host, port=db_port)

# Make RethinkDB DB if doesnt already exist
init_db()

# Setup rabbit connection and exchange
credentials = pika.PlainCredentials(rmq_user,rmq_pass)
logger.info("attempting to connect to rmq instance")
rabbit_conn = pika.BlockingConnection(
    pika.ConnectionParameters(rmq_host, rmq_port, '/', credentials)
)

logger.info("acquiring rmq channel")
exchange = "OpenFaasEx"
channel = rabbit_conn.channel()
channel.exchange_declare(exchange, exchange_type='direct', durable=True)

def type_of_change(change):
    '''Determines whether the change is a create, delete or update'''
    if change['old_val'] is None:
        return 'create'
    elif change['new_val'] is None:
        return 'delete'
    else:
        return 'update'

logger.info('waiting for changes...')

# Start feeding...
table_changes = r.db(db_name).table('files').changes()
try:
    for change in table_changes.run(rethink_conn):
        # TODO: Hook tables here and publish to RMQ
        # routing_key = 'new-file' #'mytable.' + type_of_change(change)
        # logger.info('RethinkDB -({})-> RabbitMQ'.format(routing_key))
        # logger.info(change)
        # channel.basic_publish(exchange, routing_key, json.dumps(change))
        pass
except r.RqlRuntimeError as e:
    # Table may have been dropped, connection failed etc
    logger.info(e.message)