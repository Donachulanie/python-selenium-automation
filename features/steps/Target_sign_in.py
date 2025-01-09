from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on Sign in icon')
def click_sign_in_icon(context):
    context. driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(5)


@then('Verify "Sign in" text shown')
def verify_sign_in_page_opened(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH,
                                                "//h2[@data-test='modal-drawer-heading']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


@when('Click on sign in icon in the loaded page')
def click_sign_in_icon(context):
    context. driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('Verify "Sign into your Target account" text is shown')
def verify_Sign_in_form_opened(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 lnvRvp diHlfH']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'