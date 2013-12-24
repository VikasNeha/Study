#from selenium import webdriver
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

#ffProfile = FirefoxProfile()
#ffProfile.set_preference('permissions.default.image', 2)
#driver = webdriver.Firefox(ffProfile)
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
# driver.get("https://www.google.com")
# driver.find_element(by=By.NAME, value='q')


f_swa = open('naics')
swa_codes = f_swa.readlines()
f_swa.close()

f_naics = open('NAICS_main')
naics_codes = f_naics.readlines()
f_naics.close()

file_diff = open('swa_naics_diff', 'wb')

for swa_code in swa_codes:
    found = False
    for naics_code in naics_codes:
        if swa_code[:6] in naics_code:
            found = True
            break
    if not found:
        print>>file_diff, swa_code[:6]