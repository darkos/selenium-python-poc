from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenengine as seleng

# driver = webdriver.Firefox()
driver = seleng.firefox_driver()
driver.get("http://webplease.org")
log_in_link = seleng.click_on_link('Log in')
# driver.maximize_window()

# driver.close()
