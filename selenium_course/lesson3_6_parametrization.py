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

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.mark.parametrize('link', links)
class TestPage1():

    def test_find_message(self, browser, link):
        result = ''
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

        textarea1 = browser.find_element(By.CSS_SELECTOR, "textarea[class='ember-text-area ember-view textarea string-quiz__textarea']")
        answer = math.log(int(time.time()))
        textarea1.send_keys(answer)
        submit_btn1 = browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']")
        time.sleep(2)
        submit_btn1.click()

        time.sleep(5)
        text_info = browser.find_element(By.CSS_SELECTOR, "div>p[class='smart-hints__hint']").text
        if text_info != "Correct!":
            result += text_info
        assert text_info == "Correct!", "Text message: {}".format(text_info)
        print("\nResult: {}".format(result))
        time.sleep(5)

#div>p[class="smart-hints__hint"]
#div[class="attempt__actions"]>button[class="again-btn white"]