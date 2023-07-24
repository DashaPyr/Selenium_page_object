from .pages.product_page import ProductPage
import pytest
import time

"""
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

list_of_failed_num = [7]
tested_links = [f"{product_base_link}?promo=offer{i}" if i not in list_of_failed_num else
                pytest.param(f"{product_base_link}?promo=offer{i}",
                             marks=pytest.mark.xfail(reason="some bug", strict=True)
                             )
                for i in range(10)]

@pytest.mark.parametrize("link", tested_links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.basket_price_should_be_equal_product_price()
    page.book_name_same_in_basket_and_product_page()
"""

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()
