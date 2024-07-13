from training_project.pages.login_page import LoginPage
from training_project.pages.reset_password_page import ResetPasswordPage


def test_forgot_password_redirect(browser, login_page_load):
    login_page = LoginPage(browser)
    forgot_password_page = ResetPasswordPage(browser)

    login_page.click_forgot_password()

    reset_password_displayed = forgot_password_page.redirect_displayed()

    assert reset_password_displayed, ""
