
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButtonOr']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test=content-wrapper] [id*='addToCartButtonOr']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


# @then('Verify search results shown')
# def verify_search_results(context):
#     expected_result = 'tea'
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'




@then('Verify search results shown for {product}')
def verify_search_results(context,product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'
    sleep(10)

@when('Click on Add to Cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_SIDE_NAV_BTN))


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Verify Add to Cart button from right side navigation page')
def verify_add_to_cart_from_right_side(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN)).click()
    #context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN).click()



@then('Verify Added to cart message shown')
def verify_add_to_cart_message_shown(context):
    expected_message = 'Added to cart'
    actual_message = context.driver.find_element(By.CSS_SELECTOR,"[data-test=modal-drawer-heading]").text
    assert expected_message == actual_message, f'Expected text {expected_message} not in actual {actual_message}'
