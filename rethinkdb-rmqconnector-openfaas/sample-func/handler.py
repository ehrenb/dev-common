import json
import logging
import os

from remodel.connection import pool

from skeleton.config import get_db_config
# from skeleton.db.models.file import File

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_host, db_port, db_name, db_user, db_pass = get_db_config()
pool.configure(host=db_host, port=db_port, auth_key=None, user=db_user, password=db_pass, db=db_name)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    # do something with the event given in 'req'
    logger.info(req)
    logger.info(os.environ)

    return req
