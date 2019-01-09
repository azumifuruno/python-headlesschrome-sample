import pychrome
import time
import base64
from selenium import webdriver
import chromedriver_binary

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--remote-debugging-port=10000')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:10000")

# create a tab
tab = browser.new_tab()


# start the tab 
tab.start()

# call method
tab.Network.enable()
# call method with timeout
tab.Page.navigate(url="https://github.com/fate0/pychrome", _timeout=5)

# wait for loading
tab.wait(5)

data = tab.Page.printToPDF()
print(data)
with open("%s.pdf" % time.time(), "wb") as fd:
    fd.write(base64.b64decode(data['data']))

# stop the tab (stop handle events and stop recv message from chrome)
tab.stop()

# close tab
browser.close_tab(tab)

driver.quit()