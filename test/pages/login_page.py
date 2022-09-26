from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert len(self.browser.find_elements(*LoginPageLocators.LOGIN_FORM)) == 1, \
            "Login form is absent or duplicated"

    def should_be_register_form(self):
        assert len(self.browser.find_elements(*LoginPageLocators.REGISTER_FORM)) == 1, \
            "Register form is absent or duplicated"
