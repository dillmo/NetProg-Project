from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
import json

# Wait for the right product to exist
item_name = 'Cat food'
item_exists = 0
item_id = 0
while not item_exists:
    time.sleep(1)
    response = requests.get('http://127.0.0.1:8000/shop/api/')
    json = response.json()
    if json:
        for product in json:
            if product['name'] == item_name:
                item_id = product['id']
                item_exists = 1
                break

# We want to measure the time it takes to buy an item
start_time = time.time()
# Create a new instance of the Firefox driver
# Dependencies:
# * Selenium Server running locally on port 4444
# * Gecko WebDriver
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.FIREFOX)
delay  = 3 # seconds

# Go to the shop page
driver.get('http://127.0.0.1:8000/shop')

login_link = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'login')))
login_link.click()

try:
    # Replace iamauser and iamapassword with whatever credentials the dummy account
    # is using
    # WebDriverWait is used to block until a specific element loads
    username_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'username')))
    username_element.send_keys('iamauser')
    password_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'password')))
    password_element.send_keys('iamapassword')
    password_element.submit()

    product_link = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'product_' + str(item_id))))
    product_link.click()

    add_to_cart_link = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'add_to_cart')))
    add_to_cart_link.click()

    cart_link = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'cart')))
    cart_link.click()

    checkout_link = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'checkout')))
    checkout_link.click()

    total = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'total'))).text
    cc_number_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'cc_number')))
    cc_number_element.submit()

    print('Time spent:', time.time() - start_time, 'seconds')
    print('Checked out successfully!')
    print(total)

finally:
    driver.quit()