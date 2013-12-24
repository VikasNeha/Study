import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

ffProfile = FirefoxProfile()
ffProfile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(ffProfile)

# driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
f = open('temp')
links = f.readlines()
f.close()


class naics:
    def __init__(self, code, title):
        self.code = code
        self.title = title

naicsList = []

for link in links:
    driver.get(link)
    table = driver.find_element_by_class_name('drilldown_chart')
    trs = table.find_elements_by_tag_name('tr')
    trs.pop(0)
    trs.pop(0)
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        naicsList.append(naics(tds[0].text, tds[1].text))

f2 = open('NAICS_main', 'wb')
for item in naicsList:
    item.code = item.code.encode('ascii', 'ignore')
    item.title = item.title.encode('ascii', 'ignore')
    print>>f2, item.code, ':', item.title
print 'Done'