# from urllib import urlretrieve
#
# urlretrieve("http://fiverr.com/download/17487459/original/laptops.txt", "laptops.txt")


# import urllib2
# url = "http://fiverr.com/download/17487459/original/laptops.txt"
# req = urllib2.Request(url, headers={'User-Agent': "Mozilla/5.0"})
# f = urllib2.urlopen(req)
# data = f.read()
# with open("laptops.txt", "wb") as code:
#     code.write(data)


# import requests
#
# r = requests.get(url)
# with open("laptops.txt", "wb") as code:
#     code.write(r.content)

# import fileDownloader
# downloader = fileDownloader.DownloadFile("http://fiverr.com/download/17487459/original/laptops.txt",
#                                          "laptops.txt", ('jenniferusa', '*princepanda*'))
# downloader.download()


from urllib2 import URLError, HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, install_opener, build_opener

# Set up a HTTPS request with username/password authentication
try:
    # create a password manager
    password_mgr = HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    url = "http://fiverr.com/download/17487459/original/laptops.txt"
    password_mgr.add_password(None, url, "jenniferusa", "*princepanda*")
    opener = build_opener(HTTPBasicAuthHandler(password_mgr))
    file = opener.open(url)

    # After you get the "file", you pretty much work with it the same way as you normally would.
    print file

except URLError, e:
    print 'URLError: "%s"' % e
    raise