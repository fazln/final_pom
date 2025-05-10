from pages.base_page import BasePage
from pages.locators import register_locator as reg_loc
from pages.locators import exp_results_locators as exp_loc
from tests.data.register import user


class RegisterPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_register_form(self, first_name, last_name, email, password):
        self.find_element(reg_loc.FIRST_NAME).send_keys(first_name)  # wait_for_element
        self.find_element(reg_loc.LAST_NAME).send_keys(last_name)
        self.find_element(reg_loc.EMAIL).send_keys(email)
        self.find_element(reg_loc.PASSWORD).send_keys(password)
        self.find_element(reg_loc.CONFIRM_PASSWORD).send_keys(password)

    def submit(self):
        self.click(reg_loc.SUBMIT)

    def check_register_form_visible(self):
        assert self.wait_for_element(reg_loc.FIRST_NAME).is_displayed()
        assert self.wait_for_element(reg_loc.LAST_NAME).is_displayed()
        assert self.wait_for_element(reg_loc.EMAIL).is_displayed()
        assert self.wait_for_element(reg_loc.PASSWORD).is_displayed()
        assert self.wait_for_element(reg_loc.CONFIRM_PASSWORD).is_displayed()

    def check_text_success_register(self, text):
        success_register = self.get_text_of_(exp_loc.SUCCESS_REGISTER)
        assert text == success_register, 'The text not match for successful registration'

    def check_contact_information(self, first_name, last_name, email):
        contact_information = self.get_text_of_(reg_loc.CONTACT_INFO)
        assert first_name in contact_information, f"Expected {user['first_name']} but got {first_name}"
        assert last_name in contact_information, f"Expected {user['last_name']} but got {last_name}"
        assert email in contact_information, f"Expected {user['email']} but got {email}"

    def check_text_short_password(self, text):
        weak_pass = self.get_text_of_(reg_loc.PASSWORD_ERROR)
        assert text == weak_pass, 'The text not match for short password'
