from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Testfirstname")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Testlastname")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@testmail.com")


    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "testfile.txt")

    file1 = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file1.send_keys(file_path)
    time.sleep(1)
    
    submit1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit1.click()

finally:
    time.sleep(10)
    browser.quit()