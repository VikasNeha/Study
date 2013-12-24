import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import Select

ffProfile = FirefoxProfile()
ffProfile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(ffProfile)

driver.get("http://store.nike.com/us/en_us/pd/hyper-elite-crew-basketball-socks/pid-729377/pgid-729367")
select = driver.find_element_by_class_name("exp-pdp-size-and-quantity-container")
select2 = select.find_element_by_tag_name("a")
select2.click()
time.sleep(1)
lis = select.find_elements_by_tag_name("li")
for li in lis:
    if li.text.strip() == 'M':
        li.click()
        print "Done"
        break
time.sleep(1)
button = driver.find_element_by_class_name("exp-pdp-save-container")
button.find_element_by_tag_name("button").click()