from training_project.pages.base_page import BasePage
from training_project.pages.dashboard_page import DashboardPage
from training_project.pages.login_page import LoginPage


def test_successful_login(browser, login_page_load, valid_user):
    login_page = LoginPage(browser)
    dashboard_page = DashboardPage(browser)

    login_page.login(valid_user)

    assert dashboard_page.dashboard_displayed()
