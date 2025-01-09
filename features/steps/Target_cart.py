from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart icon')
def click_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(5)


@then('Verify “Your cart is empty” message is shown')
def verify_message(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0.fJliSz").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'