from API_Requests.Lib.Rest_Client import RestClient, logger
from conf.config import get_config
from conf.logger import logger
from conf.conftest import setup_teardown
from API_Requests.Lib.File_Operations import save_json_to_file



class Test_006:
    def test_006(self,setup_teardown):

        """" Test to check GET Request is successful with response and successful status code"""

        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)

        self.headers = {
            'Content-Type' : 'application/json'
        }

        logger.info("*********** executing test_006 ****************")

        get_request,status_code = self.client.get_request(end_point="unknown/23", headers=self.headers,
                                        response_with_status_code=True,json_data_fmt=True,auto_save=True)

        assert get_request is not None, "GET request returned None"

        logger.info(f"type of json response : {type(self.client.parse_response(get_request))}")
        assert status_code == 200
        save_json_to_file(get_request)
