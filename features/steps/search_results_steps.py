from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')



# @then('Verify search results shown')
# def verify_search_results(context):
#     expected_result = 'tea'
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


@then('Verify search results shown for {product}')
def verify_search_results(context,product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

