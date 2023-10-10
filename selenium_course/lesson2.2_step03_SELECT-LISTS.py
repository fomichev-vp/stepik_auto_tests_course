from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math

def calc(num1, num2):
    num1, num2 = int(num1), int(num2)
    return str(num1 + num2)

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1_element = browser.find_element(By.ID, "num1")
    number1 = number1_element.text

    number2_element = browser.find_element(By.ID, "num2")
    number2 = number2_element.text

    answer = calc(number1, number2)

    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
    select1.select_by_value(answer)

    submit1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit1.click()

finally:
    time.sleep(10)
    browser.quit()
