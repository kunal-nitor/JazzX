from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logger
from conf.conftest import setup_teardown


class Test_002:
    def test_002(self,setup_teardown):
        """" Test to check POST Request is successful to add new resource into server"""

        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)
        self.endpoint = get_config()['API']['post_endpoint']
        self.json = {
                        "name": "morpheus",
                        "job": "leader"
                    }


        headers ={
            'Content-Type' : 'application/json'
        }

        logger.info("*********** executing test_002 ****************")

        # send post request
        post_request = self.client.post_request(end_point=self.endpoint, data=self.json,
                                                json_data_fmt=True, response_with_status_code=True,headers=headers,auto_save=True)

        # verify response
        assert post_request is not None, "POST request returned None"

