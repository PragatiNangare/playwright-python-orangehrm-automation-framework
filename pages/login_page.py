from utils.logger import get_logger
import allure


class LoginPage:
    logger = get_logger()

    def __init__(self, page):
        self.page = page
       
        
        self.username_input = page.locator("input[name='username']")
       
        self.password_input = page.locator("input[name='password']")

        self.login_button = page.locator("button[type='submit']")
        self.error_message = page.locator(".oxd-alert-content-text")

    @allure.step("Entering username")
    def enter_username(self, username):
        self.logger.info("Entering username")
        self.username_input.fill(username)
        return self

    def enter_password(self, password):
        self.logger.info("Entering password")
        self.password_input.fill(password)
        return self

    def click_login(self):
        self.logger.info("Clicking login button")
        self.login_button.click()
        return self

    def get_error_message(self):
        return self.error_message.text_content()

    def login(self, username, password):
        self.logger.info("Performing login")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # wait for dashboard to appear
        
        self.page.wait_for_selector("h6:has-text('Dashboard')")
        self.logger.info("Login successful - Dashboard loaded")
        return self
      
    