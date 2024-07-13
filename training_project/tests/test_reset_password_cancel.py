from training_project.pages.login_page import LoginPage
from training_project.pages.reset_password_page import ResetPasswordPage


def test_reset_password_cancel(browser, login_page_load):
    login_page = LoginPage(browser)
    reset_password_page = ResetPasswordPage(browser)

    login_page.click_forgot_password()

    reset_password_page.redirect_displayed()

    reset_password_page.click_cancel_button()

    assert login_page.is_login_page()
