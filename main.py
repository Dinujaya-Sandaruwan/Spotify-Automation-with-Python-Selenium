from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "/chromedriver.exe"
driver = webdriver.Chrome(PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver.get("https://spotifyclone.lol/")
print(driver.title)
driver.execute_script("nextTrack()")
# time.sleep(4.2)
# driver.quit()