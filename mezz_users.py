from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

base_url = "http://www.webplease.org"
login_url = "http://www.webplease.org/admin/login/?next=/admin/"


def login_as_admin():
    browser.get(login_url)
    username = browser.find_element_by_id('id_username')
    password = browser.find_element_by_id('id_password')
    login = browser.find_element_by_xpath("//input[@type='submit']")
    username.send_keys('admin')
    password.send_keys('admintest')
    login.click()


def goto_users_page():
    users_link = browser.find_element_by_link_text('Users')
    users_link.click()


def add_user(user_name, password, user_first_name, user_last_name, email_address):
    add_user_link = browser.find_element_by_link_text('Add user')
    add_user_link.click()
    username = browser.find_element_by_id('id_username')
    password1 = browser.find_element_by_id('id_password1')
    password2 = browser.find_element_by_id('id_password2')
    save_button = browser.find_element_by_name('_save')
    username.send_keys(user_name)
    password1.send_keys(password)
    password2.send_keys(password)
    save_button.click();
    first_name = browser.find_element_by_id('id_first_name')
    last_name = browser.find_element_by_id('id_last_name')
    email = browser.find_element_by_id('id_email')
    first_name.send_keys(user_first_name)
    last_name.send_keys(user_last_name)
    email.send_keys(email_address)
    save_button = browser.find_element_by_name('_save')
    save_button.click()


def logout():
    logout = browser.find_element_by_link_text('Log out')
    logout.click()


def delete_user(username):
    username_link = browser.find_element_by_link_text(username)
    username_link.click()
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Delete")))
    delete_link = browser.find_element_by_link_text('Delete')
    delete_link.click()
    iamsure = browser.find_element_by_xpath("//input[@type='submit']")
    iamsure.click()

browser = webdriver.Firefox()

# browser = webdriver.Remote(
#    # command_executor='http://127.0.0.1:4444/wd/hub',
#    command_executor='http://159.203.75.45:5556/wd/hub',
#    desired_capabilities=DesiredCapabilities.CHROME)

browser.maximize_window()

login_as_admin()
goto_users_page()
add_user('darko', 'darkotest', 'Darko', 'Stefanovic', 'stefanovic.darko@gmail.com')
add_user('webplease', 'webpleasetest', 'Web', 'Please', 'webplease@gmail.com')
logout()

# browser.close();

login_as_admin()
goto_users_page()
delete_user('darko')
delete_user('webplease')
logout()

browser.close();
