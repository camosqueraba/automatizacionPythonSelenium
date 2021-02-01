import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

print ("hola")

url = "https://www.google.com/"
 

driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get(url)
barra_busqueda = driver.find_element_by_name('q').click()
#barra_busqueda.send_keys("falcao")
#barra_busqueda.send_keys(Keys.ENTER)

driver.find_element_by_name('q').send_keys("leidy vargas")
driver.find_element_by_name('q').send_keys(Keys.ENTER)