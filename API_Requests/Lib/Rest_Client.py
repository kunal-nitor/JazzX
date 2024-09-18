import time
import requests
import json
from conf.logger import logGen
from API_Requests.Lib.File_Operations import save_json_to_file

logger = logGen()


class RestClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.http_session = requests.Session()
        self.http_session.headers = headers
        self.http_session.verify = True


        logger.info(f"Base url is : {self.base_url}")
        self.success_status_code = (200, 201, 202, 204)


    def get_request(self, end_point=None, data=None, headers=None, json_data_fmt=False, params=None, fmt='json',
                retries=0, response_with_status_code=False,auto_save=False):

        """
        This method is to send 'Get' request
        :param end_point(str): API endpoint/url
        :param data (dict) : Body of Request
        :param headers: Header of a request
        :param json_data_fmt (bool): True if data should be in json else False
        :param params (dict) : Parameter for a request
        :param fmt: used for return response type
        :param retries:
        :param response_with_status_code (bool): True if status code is required else false
        :param auto_save (bool) : saves response into json file if True else False
        :return:

        """
        if end_point is None:
            request_url = self.base_url
        else:
            request_url = self.base_url + end_point


        logger.info(f"Request url is : {request_url}")
        if json_data_fmt:
            data = json.dumps(data)

        try:
            logger.info(f"Initializing GET rest call from {request_url}")
            get_response = self.http_session.get(request_url, params=params, headers=headers,
                                             data=data, verify=True)
            response_data = self.parse_response(get_response)

            logger.info(f"GET Response : {response_data}")
            logger.info(f"GET Request Status Code : {get_response.status_code}")

            if get_response.status_code in self.success_status_code:
                logger.info("GET request is Successful.....")

                if auto_save:
                    save_json_to_file(response_data)

                if fmt == "raw":
                    return get_response

                if response_with_status_code:
                    return self.parse_response(get_response), get_response.status_code

                return response_data
            else:
                logger.error(f"GET Request failed....!!!")
                logger.error(f"Response Error Message: {self.parse_response(get_response)}")
                return self.parse_response(get_response), get_response.status_code

        except Exception as exc:
            if retries > 0:
                logger.info(f"GET request failed, retrying : {str(retries)} more times...")
                time.sleep(15)
                self.get_request(end_point=end_point, params=params, headers=headers, data=data,
                         json_data_fmt=json_data_fmt, retries=retries - 1)

            else:
                logger.info(f"GET request failed...")
                logger.exception(f"Exception occurred : {exc}")
                raise exc


    def post_request(self, end_point, data=None, headers=None, json_data_fmt=False, params=None,
                     fmt='json', retries=1, response_with_status_code=False,auto_save=False):
        """
        This method is used to send 'POST' Request
        :param end_point: API end point/url
        :param data: Body of a Request
        :param headers (dict) : Header of a request
        :param json_data_fmt: True if data should be in json else false
        :param params (dict): Parameters of a request
        :param fmt(str) : Used for response type json or row
        :param retries: Number of Retires
        :param response_with_status_code(bool): True if status code is required else false
        :param auto_save (bool) : saves response into json file if True else False
        :return: response of the request

        """
        request_url = self.base_url + end_point
        logger.info(f"Request url is : {request_url}")
        if json_data_fmt:
            data = json.dumps(data)

        try:
            logger.info(f"Initializing POST rest call from {request_url}")
            post_response = self.http_session.post(request_url, params=params, headers=headers, data=data, verify=True)
            response_data = self.parse_response(post_response)

            logger.info(f"POST Response : {response_data}")
            logger.info(f"POST Request Status Code : {post_response.status_code}")
            if post_response.status_code in self.success_status_code:
                    logger.info("POST request is successful...")
                    if auto_save:
                        save_json_to_file(response_data)

                    if fmt == 'raw':
                        return post_response

                    if response_with_status_code:
                        return self.parse_response(post_response), post_response.status_code
                    return self.parse_response(post_response)

            else:
                logger.error(f"POST Request Failed")
                logger.error(f"Response Error message: {self.parse_response(post_response)}")
                return self.parse_response(post_response), post_response.status_code
        except Exception as exc:
            if retries > 0:
                logger.info(f"POST request failed,retrying: {str(retries)} more times...")
                logger.info("Waiting for 15 sec....")
                time.sleep(15)
                self.post_request(end_point=end_point, data=data, headers=headers,
                      json_data_fmt=json_data_fmt, fmt=fmt, retries=retries - 1)
            else:
                logger.info("POST request failed...!!!")
                logger.exception(f"Exception Occurred : {exc}")


    def put_request(self, end_point, data=None, headers=None, json_data_fmt=False, params=None,
                    fmt="json", response_with_status_code=False,auto_save=False):
        """
        This method is to send put request
        :param end_point (str): API endpoint/url
        :param data (dict): Body of a request
        :param headers (dict): Headers of a request
        :param json_data_fmt (bool): True if data should be in json else False
        :param params (dict): parameters for a request
        :param fmt(str): Used for response type json or raw
        :param response_with_status_code (bool): True if status code os required else False
        :param auto_save (bool) : saves response into json file if True else False
        :return: response of the request

        """
        request_url = self.base_url + end_point


        logger.info(f"Request url is : {request_url}")
        if json_data_fmt:
            data = json.dumps(data)

        try:
            logger.info(f"Initializing PUT rest call from {request_url}")
            put_response = self.http_session.put(request_url, params=params, headers=headers,
                                             data=data,verify=True)
            response_data = self.parse_response(put_response)

            logger.info(f"PUT Response : {self.parse_response(put_response)}")
            logger.info(f"PUT request Status code : {put_response.status_code}")

            if put_response.status_code in self.success_status_code:
                logger.info("PUT request is successful.....")

                if auto_save:
                    save_json_to_file(response_data)
                if fmt == "raw":
                    return put_response
                if response_with_status_code:
                    return self.parse_response(put_response), put_response.status_code
                return self.parse_response(put_response)
            else:
                logger.error(f"PUT request Failed....")
                logger.error(f"Response Error Message: {self.parse_response(put_response)}")
                return self.parse_response(put_response), put_response.status_code
        except Exception as exc:
            logger.info("PUT Request is failed...!!!")
            logger.exception(f"Exception Occurred : {exc}")


    def delete_request(self, end_point, data=None, headers=None, json_data_fmt=None, params=None,
                       fmt="json", response_with_status_code=False,auto_save=False):
        """
        This method is to send delete request
        :param end_point (str): API endpoint/URL
        :param data (dict): Body of a request
        :param headers (dict): Parameters for a request
        :param json_data_fmt (bool): True if data should be in json else False
        :param params: Used for response type json or raw
        :param fmt:
        :param response_with_status_coode (bool): True if Status code os required else False
        :param auto_save (bool) : saves response into json file if True else False
        :return: Response of the request

        """
        request_url = self.base_url + end_point

        logger.info(f"Request url is : {request_url}")
        if json_data_fmt:
            data = json.dumps(data)
        try:
            logger.info(f"Initializing DELETE REST call from {request_url}")
            delete_response = self.http_session.delete(request_url, params=params, headers=headers, data=data,verify=True)
            response_data = self.parse_response(delete_response)

            logger.info(f"DELETE Response : {self.parse_response(delete_response)}")
            logger.info(f"DELETE request Status code : {delete_response.status_code}")

            if delete_response.status_code in self.success_status_code:
                logger.info(f"DELETE request is successful....")
                if auto_save:
                    save_json_to_file(response_data)
                if fmt == "raw":
                    return delete_response
                if response_with_status_code:
                    return self.parse_response(delete_response), delete_response.status_code
                return self.parse_response(delete_response)
            else:
                logger.error(f"PUT request Failed...!!!")
                logger.error(f"Response Error Message: {self.parse_response(delete_response)}")
                return self.parse_response(delete_response), delete_response.status_code

        except Exception as exc:
            logger.info("DELETE request is failed...!!!")
            logger.exception(f"Exception occurred : {exc}")


    def parse_response(self, response):
        """
        This method is to parse a response from the API.
        :param response: request response
        :return: parsed response based on expected format
        """
        try:
            # Check if the response is a requests.Response object
            if hasattr(response, 'headers'):
                content_type = response.headers.get('Content-Type')
                # Handle JSON responses
                if content_type in ['application/json', 'application/json; charset=utf-8']:
                    logger.info(f"Response JSON : {response.text}")
                    try:
                        return response.json()
                    except ValueError:
                        logger.error("Response content is not valid JSON.")
                        return None
                # Handle non-JSON responses (text, HTML, etc.)
                # elif response.text:
                #     logger.info(f"Response Text : {response.text}")
                #     return response.text

                else:
                    # For DELETE requests with no response content
                    if response.request.method.upper() == 'DELETE' and not response.content:
                        logger.info("DELETE request sent successfully, no response content returned.")
                        return None

                    logger.error("Unknown content type or empty response.")
                    return None

            # If response is directly passed (like list, str, tuple)
            elif isinstance(response, (list, str, tuple, dict)):
                return response

            else:
                logger.error("Unexpected response type encountered.")
                return None

        except Exception as exc:
            logger.exception(f"Failed to parse response: {str(exc)}")
            time.sleep(5)
            raise exc
