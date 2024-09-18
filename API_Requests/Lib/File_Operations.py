import datetime
import json
import os.path
from conf.logger import logger



def save_json_to_file(response,response_dir='API_Requests/Data/Response_Body'):
    """
    Prepare the response data and save it to a JSON file.

    :param response_dir: The response directory where all response file will be stored
    :param response: The response data to be saved, can be a dict, list, tuple, or string.

    """

    # Create a folder based on the current date
    current_date = datetime.datetime.now().strftime("%Y_%m_%d")
    date_folder_path = os.path.join(response_dir, current_date)

    def handle_tuple(data):
        return data[0]

    def handle_list(data):
        return data

    def handle_string(data):
        return json.loads(data)

    def handle_dict(data):
        return data
    # Mapping of types to their corresponding handling functions
    handler_mapping = {
        tuple: handle_tuple,
        list : handle_list,
        str  : handle_string,
        dict : handle_dict
                    }

    try:
        # Create the directory if it doesn't exist
        os.makedirs(date_folder_path, exist_ok=True)

        # Prepare the timestamped file path
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        full_file_path = os.path.join(date_folder_path, f"response_{timestamp}.json")


        # Normalize the path for logging
        full_path_normalized = full_file_path.replace(os.sep,'/')

        # Select the handler based on the type of response
        handler = handler_mapping.get(type(response))
        if not handler:
            raise TypeError("Unsupported response type")
        json_data = handler(response)

        # Save the JSON data to the specified file
        with open(full_file_path, 'w') as file:
            json.dump(json_data, file, indent=4, separators=(',', ': '))
            logger.info(f"JSON data successfully saved to {full_path_normalized}")
    except (json.JSONDecodeError, TypeError) as e:
        logger.error(f"An error occurred while preparing JSON data:{e}")
        raise e
    except OSError as e:
        logger.error(f"An error occurred while saving JSON data:{e}")
        raise e


def read_json_from_file(file_path,request_dir='API_Requests/Data/Request_Body'):
    """  Static method to read JSON data from a file.
        :param request_dir: directory where the request json data is stored.
        :param file_path: Path to the file from which the JSON data will be read.
        :return: Parsed JSON data (as a dictionary or list).
    """
    try:
        full_path = os.path.join(request_dir,file_path)

        # Normalize the path for logging
        full_path_normalized = full_path.replace(os.sep, '/')

        with open(full_path, 'r') as file:
            data = json.load(file)
        logger.info(f"JSON data successfully read from {full_path_normalized}")
        return data
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode JSON: {e}")
        raise e
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise e
    except Exception as e:
        logger.exception(f"An error occurred while reading JSON data: {e}")
        raise e
