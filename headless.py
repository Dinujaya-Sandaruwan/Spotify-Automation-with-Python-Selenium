from selenium import webdriver
import time
import threading

# Create an instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.set_window_position(2000, 0)

# Open the website
driver.get("https://spotifyclone.lol/")
driver.maximize_window()

# time.sleep(3)
element = driver.find_element("id","next_btn")
element.click()
# time.sleep(1000)
 
def printit():
  threading.Timer(500, printit).start()
  driver.execute_script("console.log('Playing...');")

printit()