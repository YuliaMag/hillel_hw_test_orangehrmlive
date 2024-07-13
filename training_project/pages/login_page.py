from selenium.webdriver.common.by import By

from training_project.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

        self.username_name = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        self.forgot_password_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[''2]/form/div[4]/p')
        self.error_msg = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p')

    def enter_username(self, username):
        self.enter_text(self.username_name, username)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def click_login(self):
        self.click_element(self.login_button)

    def click_forgot_password(self):
        self.click_element(self.forgot_password_button)

    def get_error_message(self):
        return self.get_text(self.error_msg)

    def is_login_page(self):
        return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" in self.get_current_url()

    def login(self, user):
        self.enter_username(user.username)
        self.enter_password(user.password)
        self.click_login()
