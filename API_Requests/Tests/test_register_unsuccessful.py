from jinja2.nodes import Assign

from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logGen
from conf.conftest import setup_teardown
from API_Requests.Lib.File_Operations import read_json_from_file

logger = logGen()


class Test_007:
    def test_007(self,setup_teardown):
        """" Test to check POST Request to register successfully """

        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)
        self.json = {
                        "email": "sydney@fife"
                    }

        self.headers = {
            'Content-Type': 'application/json'
                        }

        logger.info("*********** executing test_007 ****************")

        post_request,status_code = self.client.post_request(end_point="register",data=self.json,headers=self.headers,json_data_fmt=True,response_with_status_code=True)

        assert post_request is not None, "POST request returned None"
        assert status_code == 201