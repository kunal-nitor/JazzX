from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logGen
from conf.conftest import setup_teardown
from API_Requests.Lib.File_Operations import read_json_from_file
logger = logGen()


class Test_003:
    def test_003(self,setup_teardown):
        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)
        self.json = read_json_from_file('put_data.json')

        self.headers = {
            'Content-Type' : 'application/json'
        }

        logger.info("*********** executing test_003 ****************")

        put_request = self.client.put_request(end_point="users/2",data=self.json,headers=self.headers, json_data_fmt=True,response_with_status_code=True)

        assert put_request is not None, "PUT request returned None"
