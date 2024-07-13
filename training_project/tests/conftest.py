import pytest
from selenium import webdriver

from training_project.helper_entities.user import User
from training_project.pages.base_page import BasePage

base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login_page_load(browser):
    page = BasePage(browser)
    page.load(base_url)
    return page


@pytest.fixture
def valid_user():
    return User("Admin", "admin123")


@pytest.fixture
def invalid_user():
    return User("Admin", "wrongpass###")
