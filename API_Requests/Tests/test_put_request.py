from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logger
from conf.conftest import setup_teardown
from API_Requests.Lib.File_Operations import read_json_from_file


class Test_003:
    def test_003(self,setup_teardown):
        self.base_url = get_config()['API']['base_url']
        self.client = RestClient(self.base_url)
        self.endpoint = get_config()['API']['put_endpoint']
        self.json = read_json_from_file('put_data.json')

        self.headers = {
            'Content-Type' : 'application/json'
        }

        logger.info("*********** executing test_003 ****************")

        put_request = self.client.put_request(end_point=self.endpoint,data=self.json,
                                              headers=self.headers, json_data_fmt=True,response_with_status_code=True,auto_save=True)

        assert put_request is not None, "PUT request returned None"
