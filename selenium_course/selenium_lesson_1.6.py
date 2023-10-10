необходимо явно закрывать окно браузера в нашем коде при помощи команды browser.quit()
Каждый раз при открытии браузера browser = webdriver.Chrome() в системе создается процесс, который останется висеть, если вы вручную закроете окно браузера.
Чтобы не остаться без оперативной памяти после запуска нескольких скриптов, всегда добавляйте к своим скриптам команду закрытия:
-------------
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()
-------------

browser.close() закрывает текущее окно браузера
browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии
https://stackoverflow.com/questions/15067107/difference-between-webdriver-dispose-close-and-quit 


-----------------------------
Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках, 
проще всего использовать конструкцию try/finally:

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()


Системы UNIX/Linux ожидают пустую строку в конце файла, 
если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.

