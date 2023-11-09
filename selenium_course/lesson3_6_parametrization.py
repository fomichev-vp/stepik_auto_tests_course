import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

links = ('https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'
)

@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser()
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_find_message(browser, link):
        browser.get(link)
        login_btn1 = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
        login_btn1.click()
        
        email_input = browser.find_element(By.CSS_SELECTOR, "input[id='id_login_email']")
        email_input.send_keys('fomich.vp@gmail.com')
        password_input = browser.find_element(By.CSS_SELECTOR, "input[id='id_login_password']")
        password_input.send_keys('s010694fomich')
        login_btn2 = browser.find_element(By.CSS_SELECTOR, "button[class='sign-form__btn button_with-loader ']")
        login_btn2.click()

        textarea1 = browser.find_element(By.CSS_SELECTOR, "textarea[class='ember-text-area ember-view textarea string-quiz__textarea']")
        answer = math.log(int(time.time()))
        textarea1.send_keys(answer)
        submit_btn1 = browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']")
        submit_btn1.click()
        