
from selenium import webdriver
import time
import threading

# Path to the Chrome Driver
driver_path = "C:/Users/ChromeDriver/chromedriver.exe"

# Create an instance of the Chrome driver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
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