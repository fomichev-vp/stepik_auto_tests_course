import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

class TestPage1():

    def test_user_should_enter(self, browser):
        browser.get(link)
        login_btn1 = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
        login_btn1.click()
        
        email_input = browser.find_element(By.CSS_SELECTOR, "input[id='id_login_email']")
        # enter email in parenthesis
        email_input.send_keys('')
        password_input = browser.find_element(By.CSS_SELECTOR, "input[id='id_login_password']")
        # enter password in parenthesis
        password_input.send_keys('')
        login_btn2 = browser.find_element(By.CSS_SELECTOR, "button[class='sign-form__btn button_with-loader ']")
        login_btn2.click()

        time.sleep(10)