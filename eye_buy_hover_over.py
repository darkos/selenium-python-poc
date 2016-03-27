from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

firefox = webdriver.Firefox()
firefox.get('https://www.eyebuydirect.com/eyeglasses')

popup = firefox.find_element_by_xpath("//span[@class='popup-close']")
popup.click()

element_to_hover_over = firefox.find_element_by_id("collections-nav")
# element_to_hover_over = firefox.find_element_by_xpath("//a[@href='/sunglasses']")

hover = ActionChains(firefox)
hover.move_to_element(element_to_hover_over)
hover.perform()
hover.click()
# alt="His Edge"
# his_edge = firefox.find_element_by_xpath("//a[@href='/collections/his-edge']")
his_edge = firefox.find_element_by_xpath("//img[@alt='His Edge']")
# hover.move_to_element(his_edge)
# hover.perform()
# hover1 = ActionChains(firefox).move_to_element(his_edge)
# hover1.perform()
his_edge.click()
html = his_edge.get_attribute('outerHTML')
print(html)
