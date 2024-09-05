Prerequisites
Python 3.9.1 or above


Steps to set_up
1. Create Python Virtual Environment
python -m venv /path/to/new/virtual/environment

2.Activate Python virtual environment
<path to new virtual environment>\Scripts\activate


3.Install required python3 package
Navigate to home directory of project
pip3 install -r requirements.txt


Run the tests:
To execute all tests under example run:
pytest -v -s -rA
To execute a specific tests under example add -m and test marker:
pytest -v -s -m smoke -rA
To execute a specific tests with certain keyword under example file:
pytest -v -s -rA -k example 


Reports
After execution is completed reports will get generated under report folders name called Allure_Reports and HTML_Reports
to generate HTML report 
pytest -v -s -rA --html=test_example_report.html

to generate Allure Report
1) first to make directory where all json files will be stored 
pytest -v -s -rA --alluredir=Allure_Reports

2) to generate allure reports pytest
allure serve Allure_Reports
