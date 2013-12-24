import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

ffProfile = FirefoxProfile()
ffProfile.set_preference('permissions.default.image', 2)
driver = webdriver.Firefox(ffProfile)

#driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
driver.get("https://swa.aecglobal.com/Popup/NaicsCodePopup.aspx?value=&ParentAddFuntionName=content_productservice_naicsSelector_AddItem_Multiple%20&SelectionMethod=IFrame")

while True:
    try:
        #imgs = treeview.find_elements_by_tag_name("img")
        treeview = driver.find_element_by_id('TreeView1')
        imgs = treeview.find_elements_by_xpath("//img[contains(@alt, 'Expand')]")
        print len(imgs)
        clicked = False
        for img in imgs:
            if 'Expand' in img.get_attribute("alt"):
                img.click()
                time.sleep(1)
                clicked = True
        if not clicked:
            print 'Done'
            break
    except:
        print sys.exc_info()
        break

treeview = driver.find_element_by_id('TreeView1')
spans = treeview.find_elements_by_xpath("//span[@onclick]")
filename = "naics"
theFile = open(filename, 'wb')
print len(spans)
for span in spans:
    try:
        print>>theFile, span.text
    except:
        continue

print "Done"

