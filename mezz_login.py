from selenium import webdriver
from selenium.webdriver.common.keys import Keys
base_url = "http://www.webplease.org"
login_url = "http://www.webplease.org/admin/login/?next=/admin/"
browser = webdriver.Firefox()
browser.maximize_window()
browser.get(login_url)
username = browser.find_element_by_id('id_username')
password = browser.find_element_by_id('id_password')
login = browser.find_element_by_xpath("//input[@type='submit']")
username.send_keys('admin')
password.send_keys('admintest')
login.click()
browser.implicitly_wait(10)
logout = browser.find_element_by_link_text('Log out')
logout.click()
browser.close();
