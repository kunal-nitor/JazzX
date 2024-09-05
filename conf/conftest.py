import pytest
from API_Requests.Lib.Rest_Client import RestClient
from conf.config import get_config
from conf.logger import logGen

logger = logGen()


def pytest_addoption(parser):
    parser.addoption("--log_file", action="store", default="Logs/pytest.log", help="Specify the log file path.")
    parser.addoption("--config_file", action="store", default="config.ini", help="Specify the configuration file path.")


@pytest.fixture
def log_file(request):
    return request.config.getoption("--log_file")


@pytest.fixture
def config_file(request):
    return request.config.getoption("--config_file")


@pytest.fixture(scope='class', autouse=True)
def setup_teardown(request):
    print("==================================================================")
    logger.info("Starting test setup process...")
    # Simulating the generation of a bearer token (you can replace this with actual logic)
    logger.info("Generating authentication token...")
    request.cls.restclient = RestClient(get_config()['API']['base_url'])
    logger.info("Authentication token generated successfully.")
    logger.info("Test setup completed. Ready to execute tests.")
    yield
    logger.info("Starting test cleanup process...")
    # Simulating the cleanup of the bearer token (you can replace this with actual logic)
    logger.info("Cleaning up authentication token...")
    logger.info("Authentication token cleaned up successfully.")
    logger.info("Test cleanup completed. Resources released.")
