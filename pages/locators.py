from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_OF_MAIN_PRODUCT = (By.CSS_SELECTOR, ".product_main>.price_color")
    NAME_OF_MAIN_PRODUCT = (By.CSS_SELECTOR, ".product_main>h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    ALERT_NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".alertinner>strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    
    
class BasketPageLocators():
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p")
