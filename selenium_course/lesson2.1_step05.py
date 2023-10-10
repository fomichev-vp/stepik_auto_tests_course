from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:    
    link = "https://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(1)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    time.sleep(1)

    option2 = browser.find_element(By.ID,"robotsRule")
    option2.click()
    time.sleep(1)

    submit1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit1.click()

finally:
    time.sleep(10)
    browser.quit()
