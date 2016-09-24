""" Demo logging."""

import logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - [%(levelname)8s]: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.debug('this is debig')
logger.warning('this is warning')
logger.info('this is info')
logger.error('this is error')
logger.critical('this is critical')
