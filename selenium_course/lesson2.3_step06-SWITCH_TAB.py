from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit1.click()
    time.sleep(1)

    window1 = browser.window_handles[1]
    browser.switch_to.window(window1)

    x_element = browser.find_element(By.ID, "input_value")
    x_value = x_element.text
    x_num = int(x_value)
    answer1 = calc(x_num)

    input1 = browser.find_element(By.NAME, "text")
    input1.send_keys(answer1)

    submit2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit2.click()

finally:
    time.sleep(10)
    browser.quit()