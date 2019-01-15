from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome()     #driverにchromeを入れる
driver.get('https://www.google.com/')   #chromeでgoogleを表示
driver.maximize_window()        #ウィンドウを最大化する。

search_box = driver.find_element_by_name("q")   #elementに"q"を持つのを見つける。
search_box.send_keys('youtube') #search_boxにyoutubeを送る
search_box.submit() #検索する


for i, g in enumerate(driver.find_elements_by_class_name("g")):
    print("------ " + str(i+1) + " ------")
    r = g.find_element_by_class_name("r")
    print(r.find_element_by_tag_name("h3").text)  # タイトル
    URL = r.find_element_by_tag_name("a").get_attribute("href")
    print("\t" + URL )  # URL
    if [URL]:
        driver.get(URL)
        break

time.sleep(5)
driver.save_screenshot('youtube.png')
driver.quit()
