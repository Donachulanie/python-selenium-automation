from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#CART_PAGE_YOUR_CART_IS_EMPTY_TEXT = (By.CSS_SELECTOR, ".sc-fe064f5c-0.fJliSz")
#CART_PAGE_VERIFY_CART_ITEMS = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
#CART_PAGE_VERIFY_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@when('Open cart page')
def open_cart(context):
    #context.driver.get('https://www.target.com/cart')
    context.app.cart_page.open_cart_url()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)

    #cart_summary = context.driver.find_element(*CART_PAGE_VERIFY_CART_ITEMS).text
    #assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"



@then('Verify cart has correct {product}')
def verify_product_name(context,product):
    context.app.cart_page.verify_product_name(product)
    # actual_name = context.driver.find_element(*CART_PAGE_VERIFY_PRODUCT_NAME).text
    # print(f'Actual product in cart name: {actual_name}')
    # print(f'Product name stored earlier: {context.product_name}')
    # assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"



@then('Verify “Your cart is empty” message is shown')
def verify_message(context):
    context.app.cart_page.verify_cart_empty()
    #expected_result = 'Your cart is empty'
    #actual_result = context.driver.find_element(*CART_PAGE_YOUR_CART_IS_EMPTY_TEXT).text
    #assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
    sleep(5)