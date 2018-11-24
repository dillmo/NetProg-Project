from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Firefox driver
# Dependencies:
# * Selenium Server running locally on port 4444
# * Gecko WebDriver
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.FIREFOX)

# Go to the shop page
driver.get('http://127.0.0.1:8000/shop')

login_link = driver.find_element_by_id('login')
login_link.click()
time.sleep(1)

# Replace iamauser and iamapassword with whatever credentials the dummy account
# is using
username_element = driver.find_element_by_name('username')
username_element.send_keys('iamauser')
password_element = driver.find_element_by_name('password')
password_element.send_keys('iamapassword')
password_element.submit()
time.sleep(1)

product_link = driver.find_element_by_id('product_1')
product_link.click()
time.sleep(1)

add_to_cart_link = driver.find_element_by_id('add_to_cart')
add_to_cart_link.click()
time.sleep(1)

cart_link = driver.find_element_by_id('cart')
cart_link.click()
time.sleep(1)

checkout_link = driver.find_element_by_id('checkout')
checkout_link.click()
time.sleep(1)

total = driver.find_element_by_id("total").text
cc_number_element = driver.find_element_by_name("cc_number")
cc_number_element.submit()

print("Checked out successfully!")
print("Total:", total)

driver.quit()