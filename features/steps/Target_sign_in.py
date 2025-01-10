from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SIGN_IN_TEXT_ON_SIDE_NAV_PAGE = (By.XPATH, "//h2[@data-test='modal-drawer-heading']")
SIGN_IN_ICON_IN_SIDE_NAV_PAGE = (By.XPATH, "//button[@data-test='accountNav-signIn']")
SIGN_IN_FORM_TEXT = (By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 lnvRvp diHlfH']")

@then('Verify "Sign in" text shown')
def verify_sign_in_page_opened(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(*SIGN_IN_TEXT_ON_SIDE_NAV_PAGE).text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


@when('Click on sign in icon in the loaded page')
def click_sign_in_icon(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_ICON_IN_SIDE_NAV_PAGE)).click()
    #context. driver.find_element(*SIGN_IN_ICON_IN_SIDE_NAV_PAGE).click()


@then('Verify "Sign into your Target account" text is shown')
def verify_Sign_in_form_opened(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(*SIGN_IN_FORM_TEXT).text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'