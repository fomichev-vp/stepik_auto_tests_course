from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

def calc(number):
    number = int(number)
    return str(log(abs(12*sin(number))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(answer)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox1)
    checkbox1.click()

    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton1)
    radiobutton1.click()

    submit1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit1)
    submit1.click()

finally:
    time.sleep(10)
    browser.quit()
