from selenium.webdriver.common.by import By

from training_project.pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input')
    RESET_PASSWORD_FORM = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[1]')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')

    reset_password_link = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"

    def redirect_displayed(self):
        reset_password = self.find_element(self.RESET_PASSWORD_FORM)
        return reset_password.is_displayed()

    def click_cancel_button(self):
        click_cancel_button = self.find_element(self.CANCEL_BUTTON)
        click_cancel_button.click()

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def click_reset_password_button(self):
        click_reset_password_button = self.find_element(self.RESET_PASSWORD_BUTTON)
        click_reset_password_button.click()

    def link_sent_successfully_displayed(self):
        return self.reset_password_link in self.get_current_url()
