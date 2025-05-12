import os
import logging
from datetime import datetime
from utils.log_rotation import rotate_logs
from utils.config import LOG_FILE_PATH, LOG_ROTATION_DAYS

def get_logger(name: str) -> logging.Logger:
    rotation_days = int(LOG_ROTATION_DAYS)

    os.makedirs(LOG_FILE_PATH, exist_ok=True)
    log_file = os.path.join(LOG_FILE_PATH, f"{datetime.now().strftime('%Y-%m')}_{name.split('.')[0]}.log")

    rotate_logs(LOG_FILE_PATH, rotation_days, logf=log_file)

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(name)s - PID:%(process)d] %(message)s')

        # Console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # Fichier
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def get_new_logger_or_not(name, logname=None):
    if logname is None:
        #logging.basicConfig(level=logging.DEBUG)
        get_logger(name)
        logger = logging.getLogger(name)
        print(f"logger lognamenone : {logger}")
        return logger
    else:
        logger = logging.getLogger(logname)
        print(f"logger pasnone : {logger}")
        return logger
    