from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep



class CartPage(BasePage):
    CART_PAGE_YOUR_CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, ".sc-fe064f5c-0.fJliSz")
    CART_PAGE_VERIFY_CART_ITEMS = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    CART_PAGE_VERIFY_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_cart_empty(self):
        #expected_result = 'Your cart is empty'
        self.verify_text('Your cart is empty',*self.CART_PAGE_YOUR_CART_IS_EMPTY_TEXT)
        sleep(5)
        # actual_result = self.driver.find_element(*self.CART_PAGE_YOUR_CART_IS_EMPTY_TEXT).text
        # assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'

    def open_cart_url(self):
        self.driver.get('https://www.target.com/cart')
        sleep(5)

    def verify_cart_items(self,amount):
        self.verify_partial_text(amount, *self.CART_PAGE_VERIFY_CART_ITEMS)

    def verify_product_name(self,product):
        self.verify_partial_text(product,*self.CART_PAGE_VERIFY_PRODUCT_NAME)




