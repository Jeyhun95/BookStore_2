from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.need_review
@pytest.mark.parametrize('promo_num',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_num):
    page = ProductPage(browser, promo_num)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.is_prices_are_equal()
    page.is_names_are_equal_text()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.is_no_success_message_when_adding_to_cart()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.is_no_success_message_when_adding_to_cart()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.is_success_message_in_cart_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link_new_locator()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page_new_locator()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()
    page.basket_is_empty_text()


@pytest.mark.xfail
def test_guest_can_see_empty_text_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()
    page.no_empty_text_in_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser_2):
        page = ProductPage(browser_2, link)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.open()
        page.go_to_login_page_new_locator()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser_2):
        page = ProductPage(browser_2, link)
        page.open()
        page.is_no_success_message_when_adding_to_cart()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser_2):
        page = ProductPage(browser_2, link)
        page.open()
        page.add_to_cart()
        page.is_prices_are_equal()
        page.is_names_are_equal_text()
