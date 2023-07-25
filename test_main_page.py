from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
from selenium.webdriver.common.by import By
import select as something


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    # login_page = page.go_to_login_page()                # Первый способ перехода: возвращать нужный Page Object.
    page.go_to_login_page()                               # Второй способ перехода: переход происходит неявно, страницу инициализируем в теле теста
    login_page = LoginPage(browser, browser.current_url)  # Второй способ перехода: переход происходит неявно, страницу инициализируем в теле теста
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_goods_in_basket()
    basket_page.basket_should_be_empty()
    
