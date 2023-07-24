from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
    
    
    def basket_price_should_be_equal_product_price(self):
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_MAIN_PRODUCT)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == price_of_product.text, f"expected '{basket_price}' to be  '{price_of_product}'"
    
        
    def book_name_same_in_basket_and_product_page(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_MAIN_PRODUCT)
        alert_name_of_product = self.browser.find_element(*ProductPageLocators.ALERT_NAME_OF_PRODUCT)
        assert alert_name_of_product.text == name_of_product.text, f"expected '{alert_name_of_product}' to be  '{name_of_product}'"
    
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disapper, but haven't done it"
