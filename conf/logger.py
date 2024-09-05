import logging
import os
import time


def logGen():
    logging.basicConfig(filename=f'API_Requests/Logs/log_{time.strftime('%Y%m%d_%H%M%S')}.log',format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%m %d %Y %H %M %S', filemode='w')

    log_directory = "Logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Configure the logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(f"Logs/log_{time.strftime('%Y%m%d_%H%M%S')}.log", mode="w")
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(file_handler)

    return logger