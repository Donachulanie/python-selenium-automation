from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


#SIGN_IN_ICON =(By.XPATH, "//a[@data-test='@web/AccountLink']")

HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
HEADER_LINKS_AMOUNT = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
SIGN_IN_TEXT_ON_SIDE_NAV_PAGE = (By.XPATH, "//h2[@data-test='modal-drawer-heading']")


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()
    # context.driver.get('https://www.target.com/')


# @when('Search for tea')
# def search_product(context):
#     context.driver.find_element(By.ID, 'search').send_keys('tea')
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)


@when('Search for {product}')
def search_product(context,product):
    context.app.header.search_product(product)
    #context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    #context.driver.find_element(*SEARCH_BTN).click()
    #sleep(10)



@when('Click on Sign in icon')
def click_sign_in_icon(context):
    context.app.header.click_sign_in_icon()
    # context.driver.find_element(*SIGN_IN_ICON).click()
    # context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_TEXT_ON_SIDE_NAV_PAGE))



@when('Click on Cart icon')
def click_icon(context):
    context.app.header.click_cart()
    #context.driver.find_element(*CART_BTN).click()
    #context.driver.wait.until(EC.visibility_of_element_located(CART_PAGE_YOUR_CART_IS_EMPTY_TEXT))






@then('Verify at least 1 header link is shown')
def verify_header_links(context):
    print('\nFind element:')
    el = context.driver.find_element(*HEADER_LINKS)
    print(el)
    context.driver.refresh()
    sleep(5)

    print('\nAfter REFRESH Find element:')
    el = context.driver.find_element(*HEADER_LINKS)
    print(el)

    el.click()
    sleep(3)



@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context,expected_amount):
    links = context.driver.find_elements(*HEADER_LINKS_AMOUNT)
    print('\nFind elementS:')
    print(links)
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'

