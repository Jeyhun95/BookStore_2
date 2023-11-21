from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators
import time


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def is_prices_are_equal(self):
        assert self.is_element(*ProductPageLocators.ITEM_PRICE).text == self.is_element(
            *ProductPageLocators.CART_TOTAL).text, \
            'Prices are not equal'

    def is_names_are_equal(self):
        assert self.is_element(*ProductPageLocators.ITEM_NAME).text == self.is_element(
            *ProductPageLocators.ADD_TO_CART_SUCCESS).text, 'There is no such name in success message'

    def is_names_are_equal_text(self):
        assert self.get_element_text(*ProductPageLocators.ITEM_NAME) == self.get_element_text(
            *ProductPageLocators.ADD_TO_CART_SUCCESS), 'There is no such name in success message'

    def is_no_success_message_when_adding_to_cart(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_WHEN_ADDING_TO_CART), \
            'Success message when adding the item to the cart is displayed'

    def is_success_message_in_cart_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_WHEN_ADDING_TO_CART), \
            'Element is not disappeared'

    def register_new_user(self, email, password):
        registration_mail = self.browser.find_element(*BasePageLocators.REGISTRATION_MAIL)
        registration_mail.send_keys(email)
        registration_password = self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD)
        registration_password.send_keys(password)
        registration_password_repeat = self.browser.find_element(*BasePageLocators.REGISTRATION_PASSWORD_REPEAT)
        registration_password_repeat.send_keys(password)
        submit_button = self.browser.find_element(*BasePageLocators.REGISTRATION_SUBMIT)
        submit_button.click()