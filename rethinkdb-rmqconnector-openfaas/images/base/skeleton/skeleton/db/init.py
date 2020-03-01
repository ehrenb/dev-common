#!/usr/bin/env python3

import logging

import rethinkdb
from rethinkdb import r
from remodel.connection import pool
from remodel.helpers import create_tables, create_indexes

from skeleton.config import get_db_config

db_host, db_port, db_name, db_user, db_pass = get_db_config()
rethink_conn = r.connect(host=db_host, port=db_port)

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def mk_db():
    try:
        r.db_create(db_name).run(rethink_conn)
    except rethinkdb.errors.ReqlOpFailedError as e:
        if 'already exists' in str(e).lower():
            logger.info("db already exists, won't remake it")
        else:
            raise e

pool.configure(host=db_host, port=db_port, auth_key=None, user=db_user, password=db_pass, db=db_name)

# Import all Models to be created into namespace
from skeleton.db.models.file import File

def init_db():
    logger.info("making db")
    mk_db()
    logger.info("making tables")
    create_tables()
    logger.info("creating indexes")
    create_indexes()
#
# if __name__ == '__main__':
#     init()