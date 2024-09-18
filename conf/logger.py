import datetime
import logging
import os



def logGen():
    current_date = datetime.datetime.now().strftime("%Y_%m_%d")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create a folder for the current date inside the Logs directory
    log_directory ="Logs"
    date_folder_path = os.path.join(log_directory, current_date)
    os.makedirs(date_folder_path, exist_ok=True)

    # Define the log file path with timestamp
    log_file_path = os.path.join(date_folder_path,f"log_{timestamp}.log")



    log_directory = "Logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Configure the logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file_path, mode="w")
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(file_handler)

    return logger

logger = logGen()