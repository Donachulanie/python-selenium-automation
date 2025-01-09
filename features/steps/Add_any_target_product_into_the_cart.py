from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Search for {product}')
def search_product(context,product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)



@when('Click on Add to Cart button')
def click_on_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOr']").click()
    sleep(5)




@then('Verify Add to Cart button from right side navigation page')
def verify_add_to_cart_from_right_side(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test=content-wrapper] [id*='addToCartButtonOr']").click()

    sleep(5)

@then('Verify Added to cart message shown')
def verify_add_to_cart_message_shown(context):
    expected_message = 'Added to cart'
    actual_message = context.driver.find_element(By.CSS_SELECTOR,"[data-test=modal-drawer-heading]").text
    assert expected_message == actual_message, f'Expected text {expected_message} not in actual {actual_message}'





