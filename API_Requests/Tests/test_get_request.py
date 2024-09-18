from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logger
from conf.conftest import setup_teardown


class Test_001:
    def test_001(self,setup_teardown):

        """" Test to check GET Request is successful with response and successful status code"""

        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)
        self.endpoint = get_config()['API']['get_endpoint']

        self.headers = {
            'Content-Type' : 'application/json'
        }

        logger.info("*********** executing test_001 ****************")

        # send get request
        get_request,status_code = self.client.get_request(end_point= self.endpoint, headers=self.headers,
                                                response_with_status_code=True,json_data_fmt=True,auto_save=True)

        # verify response is not None (json)
        assert get_request is not None, "GET request returned None"

        logger.info(f"type of json response : {type(self.client.parse_response(get_request))}")

