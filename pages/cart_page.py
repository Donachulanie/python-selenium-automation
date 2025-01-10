from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class CartPage(BasePage):
    CART_PAGE_YOUR_CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, ".sc-fe064f5c-0.fJliSz")

    def verify_cart_empty(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.CART_PAGE_YOUR_CART_IS_EMPTY_TEXT).text
        assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'