from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logGen
from conf.conftest import setup_teardown
from API_Requests.Lib.File_Operations import read_json_from_file

logger = logGen()


class Test_005:
    def test_005(self,setup_teardown):
        """" Test to check POST Request is successful to add new resource into server"""

        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)
        self.json = read_json_from_file('post_data.json')

        self.headers = {
            'Content-Type': 'application/json'
        }

        logger.info("*********** executing test_005 ****************")

        post_request = self.client.post_request(end_point="users",data=self.json,headers=self.headers,json_data_fmt=True,response_with_status_code=True)

        assert post_request is not None, "POST request returned None"
