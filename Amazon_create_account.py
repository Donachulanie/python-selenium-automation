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

#CSS SELECTOR for "amazon" logo element
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')


#CSS SELECTOR for "Creat account"  element
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')


#CSS SELECTOR for "Your name" element
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

#CSS SELECTOR for "Mobile number or email" element
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#CSS SELECTOR for "Password" element
driver.find_element(By.CSS_SELECTOR, 'ap_password')

#CSS SELECTOR for "Re-enter password" element
driver.find_element(By.CSS_SELECTOR, 'ap_password_check')

#CSS SELECTOR for "Create your Amazon account" element
driver.find_element(By.CSS_SELECTOR, 'a-button-input')

#CSS SELECTOR for "Conditions of Use" element
driver.find_element(By.CSS_SELECTOR, 'a-button-input')

#XPATH for "Privacy Notice" element
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_privacy_notice')]")

#CSS SELECTOR for "Sign in" element
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")
