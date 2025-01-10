from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BENIFIT_CELLS_AMOUNT =(By.CSS_SELECTOR,"[class*='cell-item-content']")

@given('Open Target circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')



@then('Verify {expected_amount} benefit cells are shown')
def verify_benefit_cells_amount(context,expected_amount):
    cells = context.driver.find_elements(*BENIFIT_CELLS_AMOUNT)
    print('\nFind elements:')
    print(cells)

    assert len(cells) == int(expected_amount), f'Expected {expected_amount} cells but got {len(cells)}'