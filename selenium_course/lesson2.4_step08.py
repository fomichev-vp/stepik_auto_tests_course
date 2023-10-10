from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

def calc(x):
    return math.log(12*math.sin(x))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price1 = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x_element = browser.find_element(By.ID, "input_value")
    x_value = int(x_element.text)
    answer1 = calc(x_value)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer1)
    time.sleep(1)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(15)
    browser.quit()