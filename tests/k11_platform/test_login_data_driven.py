
import re
import time

import pytest

from pages.k11_platform.home_page import HomePage
from pages.k11_platform.login_page import LoginPage
from pages.k11_platform.dashboard_page import DashboardPage
from playwright.sync_api import expect
from utilities.data_reader import read_json_data, read_csv_data, read_excel_data

# Load/read the data from the test data files

csv_data = read_csv_data("testdata/logindata.csv")
json_data = read_json_data("testdata/logindata.json")

@pytest.mark.datadriven
@pytest.mark.parametrize("testName,email,password,expected", csv_data)

def test_login_data_driven(page, testName, email, password, expected):
	# Go to the login page directly
	page.goto("https://k11softwaresolutions.com/login")

	login_page = LoginPage(page)
	dashboard_page = DashboardPage(page)

	login_page.login(email, password)

	if expected == "success":
		# Wait for dashboard URL and then check for dashboard welcome text
		expect(page).to_have_url(re.compile(r"/dashboard"), timeout=10000)
		expect(page.locator("text=Manage your account and view updates")).to_be_visible(timeout=10000)
	else:
		expect(login_page.get_login_error()).to_be_visible(timeout=10000)
# ...existing code...
