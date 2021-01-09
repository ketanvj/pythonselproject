# pip install -U selenium
import time

from selenium import webdriver
print(type(webdriver))
driver = webdriver.Chrome(executable_path="../resources/chromedriver-79.exe")
driver.maximize_window()

# The driver.get method will navigate to a page given by the URL.
# WebDriver will wait until the page has fully loaded
# (that is, the “onload” event has fired)
# before returning control to your test or script.
# It’s worth noting that if your page uses a lot of AJAX on load
# then WebDriver may not know when it has completely loaded.
driver.get("http://selenium-examples.nichethyself.com")
driver.find_element_by_id("loginname").send_keys("stc123")

# my_element = driver.find_element_by_id("loginname")
# my_element.send_keys("stc123")
# myelement = WebElement() # creating an object of WebElement
# return myelement

driver.find_element_by_id("loginpassword").send_keys("12345")
driver.find_element_by_id("loginbutton").click()
# driver.find_element_by_id("loginbutton").maximize_window()
time.sleep(4) # this should be avoided. If your application takes lesser than 4 still it will wait for 4
# if your application takes more than 4 then test will fail.
#driver.

print(driver.title)


driver.quit()