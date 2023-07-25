from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        basket_content = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)
        assert 'Your basket is empty' in basket_content.text, \
            f"expected 'Your basket is empty' to be substring of '{basket_content.text}'"
        
            
    def should_be_no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "There are goods in basket"
