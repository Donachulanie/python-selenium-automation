from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    SIGN_IN_ICON = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    SIGN_IN_TEXT_ON_SIDE_NAV_PAGE = (By.XPATH, "//h2[@data-test='modal-drawer-heading']")
    SIGN_IN_ICON_IN_SIDE_NAV_PAGE = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def search_product(self, product):
        self.input_text(product,*self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)


    def click_cart(self):
        #self.click(*self.CART_BTN)
        self.wait_and_click(*self.CART_BTN)


    def click_sign_in_icon(self):
        self.wait_and_click(*self.SIGN_IN_ICON)
        sleep(5)

    def verify_sign_in_page_opened(self):
        self.verify_text('Sign in', *self.SIGN_IN_TEXT_ON_SIDE_NAV_PAGE)

    def click_sign_in_icon_side_nav_page(self):
        self.wait_and_click(*self.SIGN_IN_ICON_IN_SIDE_NAV_PAGE)




