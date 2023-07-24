from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import math
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    browser.implicitly_wait(5)
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(5)
    page.basket_price_should_be_equal_product_price()
    page.book_name_same_in_basket_and_product_page()

    time.sleep(5)
