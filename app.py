# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

driver = webdriver.Firefox();

driver.get("https://nodarbibas.rtu.lv/")

course_select = driver.find_element(By.ID,"program-id");
course_select.send_keys("Datorsistēmas (CDBD0)");
course_select.send_keys(Keys.RETURN);
kurss_select = driver.find_element(By.ID, "course-id")
