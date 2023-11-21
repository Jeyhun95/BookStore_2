from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):

    def basket_is_empty(self):
        try:
            assert not self.browser.find_element(*BasketPageLocators.BASKET_ITEMS), \
                'The basket is not empty'
        except NoSuchElementException:
            return True

    def basket_is_empty_text(self):
        assert self.get_element_text(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), \
            'The text that basket is empty not shown'

    def no_empty_text_in_basket(self):
        assert not self.get_element_text(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), \
            'The text that basket is empty displayed'

