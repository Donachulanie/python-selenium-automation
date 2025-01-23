from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class SearchResultsPage(BasePage):
    VERIFY_SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButtonOr']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test=content-wrapper] [id*='addToCartButtonOr']")


    def verify_search_results(self,product):
        self.verify_partial_text(product,*self.VERIFY_SEARCH_RESULTS)
        #actual_result = self.find_element(*self.VERIFY_SEARCH_RESULTS).text
        #assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

    def verify_search_url(self,product):
        self.verify_partial_url(product)
        # url = self.driver.current_url
        # assert product in url, f'...'

    def click_on_add_to_cart(self):
        self.wait_and_click(*self.ADD_TO_CART_BTN)

    def store_product_name(self,product):
        self.wait_and_click(*self.PRODUCT_NAME)

    def verify_add_to_cart_from_right_side(self):
        self.wait_and_click(*self.ADD_TO_CART_SIDE_NAV_BTN)





