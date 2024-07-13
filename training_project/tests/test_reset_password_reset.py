from training_project.pages.login_page import LoginPage
from training_project.pages.reset_password_page import ResetPasswordPage


def test_reset_password_reset(browser, login_page_load):
    login_page = LoginPage(browser)
    reset_password_page = ResetPasswordPage(browser)

    login_page.click_forgot_password()

    reset_password_page.redirect_displayed()

    reset_password_page.enter_username("Admin")
    reset_password_page.click_reset_password_button()

    reset_password_displayed = reset_password_page.redirect_displayed()
    link_displayed = reset_password_page.link_sent_successfully_displayed()

    assert reset_password_displayed, ""
    assert link_displayed, ""
