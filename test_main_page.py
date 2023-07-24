from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


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
