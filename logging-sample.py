import logging
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logger = logging.getLogger(__name__)
    logger.debug("test")