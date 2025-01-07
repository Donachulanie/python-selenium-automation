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

#get into the Amazon page
driver.get('https://www.amazon.com/')


#Navigating to the login page by clicking the "sign in" Icon by ID
driver.find_element(By.ID, 'nav-signin-tooltip').click()

sleep(6)


# find logo element by XPATH and test case results display

actual_result= 'amazon'
expected_result=driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']").text

assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test case passed')

#find email field element by ID
driver.find_element(By.ID, 'ap_email').click()

#find continue button element by ID
driver.find_element(By.ID, 'continue').click()
sleep(2)

#conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]").click()

# Privacy note link
driver.find_element(By.XPATH, ).click()
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]").click()

#Need help link by XPATH
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-expand']").click()

sleep(2)

# forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom').click()

#Other issues with sign in link
driver.find_element(By.ID, 'ap-other-signin-issues-link').click()

# create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit').click()

# sleep(5)




# driver.quit()

