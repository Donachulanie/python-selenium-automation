from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(BasePage):
    SIGN_IN_FORM_TEXT = (By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 lnvRvp diHlfH']")
    EMAIL_FIELD_ID = (By.CSS_SELECTOR, "input[autocomplete='username webauthn']")
    PASSWORD_FIELD_ID = (By.CSS_SELECTOR, "input[data-test='login-password']")
    SIGN_IN_WITH_PASSWORD_ICON = (By.CSS_SELECTOR, "button[id='login'")

    def verify_sign_in_form_opened(self):
        self.verify_text('Sign into your Target account', *self.SIGN_IN_FORM_TEXT)
        sleep(5)

    def input_valid_email(self,email,password):
        self.input_text(email, *self.EMAIL_FIELD_ID)
        self.input_text(password, *self.PASSWORD_FIELD_ID)


    def click_sign_in_with_password_icon(self):
        self.click(*self.SIGN_IN_WITH_PASSWORD_ICON)


    def verify_user_logged_in(self):
        self.wait_for_element_invisible(*self.SIGN_IN_FORM_TEXT)

