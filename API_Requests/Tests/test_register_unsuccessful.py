from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logger
from conf.conftest import setup_teardown


class Test_007:
    def test_007(self,setup_teardown):
        """" Test to check POST Request to register successfully """

        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)
        self.endpoint = get_config()['API']['register_endpoint']
        self.json = {
                        "email": "sydney@fife"
                    }

        self.headers = {
            'Content-Type': 'application/json'
                        }

        logger.info("*********** executing test_007 ****************")

        post_request,status_code = self.client.post_request(end_point=self.endpoint,data=self.json,headers=self.headers,
                                            json_data_fmt=True,response_with_status_code=True,auto_save=True)

        assert post_request is not None, "POST request returned None"
        assert status_code == 201

