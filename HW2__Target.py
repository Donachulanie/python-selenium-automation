
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')

#Sign in button verifying using XPATH
# driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(5)

#verify sign in page loaded
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

sleep(5)

#verify "Sign into your Target account" text is shown

expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 lnvRvp diHlfH']").text

sleep(5)
assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test case passed')


# sign in button shown
actual_result = driver.find_element(By.ID, "login").click()
sleep(5)

driver.quit()