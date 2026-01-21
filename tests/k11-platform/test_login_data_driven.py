import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import expect
from utilities.data_reader import read_json_data, read_csv_data, read_excel_data

# Load/read the data from the test data files

csv_data = read_csv_data("testdata/logindata.csv")
json_data = read_json_data("testdata/logindata.json")

@pytest.mark.datadriven
@pytest.mark.parametrize("testName,email,password,expected", csv_data)
def test_login_data_driven(page, testName, email, password, expected):
	home_page = HomePage(page)
	login_page = LoginPage(page)
	dashboard_page = DashboardPage(page)

	home_page.click_my_account()
	home_page.click_login()

	login_page.login(email, password)
	time.sleep(3)

	if expected == "success":
		expect(dashboard_page.get_title()).to_be_visible(timeout=3000)
	else:
		expect(login_page.get_login_error()).to_be_visible(timeout=3000)
# ...existing code...
