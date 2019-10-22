import logging
import os
from src import definitions

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(definitions.LOGGER_DIR, 'debug.log'), filemode='w')