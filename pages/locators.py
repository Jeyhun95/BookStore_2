from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK_2 = (By.CSS_SELECTOR, "#registration_link")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    CART_TOTAL = (By.CSS_SELECTOR, 'div.alertinner p strong')
    ADD_TO_CART_SUCCESS = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) .alertinner strong')
    SUCCESS_MESSAGE_WHEN_ADDING_TO_CART = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    REGISTRATION_MAIL = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini .btn-default:nth-child(1)')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//*[contains(text(), "Your basket is empty.")]')
