import logging
import os
from datetime import datetime

LOG_FILE =LOG_FILE = '{}.log'.format(datetime.now().strftime('%m_%d_%Y_%H_%M_%S'))
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
try:
    os.makedirs(logs_path)
except FileExistsError:
    pass

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename = LOG_FILE_PATH,
    format=  '[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )


if __name__=='__main__':
    logging.info('logging has started')