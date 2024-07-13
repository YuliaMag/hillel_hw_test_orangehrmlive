from training_project.pages.login_page import LoginPage


def test_unsuccessful_login(browser, login_page_load, invalid_user):
    login_page = LoginPage(browser)

    login_page.login(invalid_user)

    assert login_page.is_login_page()
    assert login_page.get_error_message() != ""
