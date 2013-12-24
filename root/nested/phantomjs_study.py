from selenium import webdriver
import time

dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36")
service_args = ['--load-images=false', '--proxy-type=none', '--ignore-ssl-errors=true']
driver = webdriver.PhantomJS(executable_path="C:\\phantomjs.exe", service_args=service_args, desired_capabilities=dcap)

# for k, v in driver.desired_capabilities.iteritems():
#     print k, ":", v


# driver.get("http://www.expireddomains.net/")
# print driver.current_url
# print driver.title

driver.get("https://satoshimines.com/newplayer.php")
print driver.title



