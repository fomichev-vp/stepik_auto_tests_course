        Как работают методы get и find_element

Разберем простой тест на WebDriver, проверяющий работу кнопки.
  Открыть страницу http://suninjuly.github.io/wait1.html
  Нажать на кнопку "Verify"
  Проверить, что появилась надпись "Verification was successful!"

Для открытия страницы мы используем метод get, затем находим нужную кнопку с помощью одного из методов find_element 
и нажимаем на нее с помощью метода click.
Далее находим новый элемент с текстом и проверяем соответствие текста на странице ожидаемому тексту.


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

Попробуйте сначала выполнить тест вручную, а затем запустить автотест. 
В первом случае, вы завершите тест успешно, во втором случае автотест упадет с сообщением NoSuchElementException для элемента c id="verify". Почему так происходит?

Тест будет работать абсолютно стабильно, только если в данной веб-странице не используется JavaScript
(что маловероятно для современного веба)

Скрипт может управлять появлением кнопки на странице и показывать ее, например, с задержкой, чтобы кнопка красиво и медленно возникала на странице.
В этом случае наш тест упадет с уже известной нам ошибкой NoSuchElementException,
так как в момент выполнения команды button = browser.find_element(By.ID, "verify") элемент с id="verify" еще не отображается на странице.

#  !!!
На данной странице пауза перед появлением кнопки установлена на 1 секунду, 
метод find_element() сделает только одну попытку найти элемент и в случае неудачи уронит наш тест.
#  !!!