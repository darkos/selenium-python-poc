from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()

def firefox_driver():
    return browser


def click_on_link(link_text):
    link_to_click = find_element_by_link_text(link_text)
    if link_to_click:
        link_to_click.click()


    ##########################
    ###  Research Methods  ###
    ##########################
def find_element_by_id(elem_id):
    try:
        element_by_id = browser.find_element_by_id(elem_id)
        return element_by_id
    except NoSuchElementException as nse:
        print(nse.msg)
    return None


def find_element_by_xpath(xpath_val):
    try:
        element_by_xpath = browser.find_element_by_xpath(xpath_val)
        return element_by_xpath
    except NoSuchElementException as nse:
        print(nse.msg)
    return None


def find_elements_by_xpath(xpath_val):
    try:
        elements_by_xpath = browser.find_elements_by_xpath(xpath_val)
        return elements_by_xpath
    except NoSuchElementException as nse:
        print(nse.msg)
    return None


def find_element_by_link_text(link_text):
    try:
        link_with_text = browser.find_element_by_link_text(link_text)
        return link_with_text
    except NoSuchElementException as nse:
        print(nse.msg)
    return None

def find_element_by_partial_link_text(partial_link_text):
    try:
        link_with_partial_text = browser.find_element_by_partial_link_text(partial_link_text)
        return link_with_partial_text
    except NoSuchElementException as nse:
        print(nse.msg)
    return None


def find_elements_by_class_name(class_name):
    try:
        elements_by_class_name = browser.find_elements_by_class_name(class_name)
        return elements_by_class_name
    except NoSuchElementException as nse:
        print(nse.msg)
    return None
