На веб-страницах мы также встречаем раскрывающиеся (выпадающие) списки.
У таких списков есть несколько важных особенностей:
У каждого элемента списка обычно есть уникальное значение атрибута value
В списках может быть разрешено выбирать как только один, так и несколько вариантов, в зависимости от типа списка
Визуально списки могут различаться тем, что в одном случае все варианты скрыты в выпадающем меню (http://suninjuly.github.io/selects1.html), а в другом все варианты или их часть видны (http://suninjuly.github.io/selects2.html)

html для списка:

<label for="dropdown">Выберите язык программирования:</label>
<select id="dropdown" class="custom-select">
    <option selected>--</option>
    <option value="1">Python</option>
    <option value="2">Java</option>
    <option value="3">JavaScript</option>
</select>

Варианты ответа задаются тегом option, значение value может отсутствовать.
Можно отмечать варианты с помощью обычного метода click(). 
Для этого сначала нужно применить метод click() для элемента с тегом select, чтобы список раскрылся, а затем кликнуть на нужный вариант ответа:

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()

Последняя строчка может выглядеть и так:
browser.find_element(By.CSS_SELECTOR, "[value='1']").click

Это не самый удобный способ, так как нам приходится делать лишний клик для открытия списка.
Есть более удобный способ, для которого используется специальный класс Select из библиотеки WebDriver.
Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select.
Далее можно найти любой вариант из списка с помощью метода select_by_value(value):

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1")  # ищем элемент с текстом "Python"

Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index).
Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.
Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля.
Для того чтобы найти элемент с текстом "Python", нужно использовать select.select_by_index(1), 
так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".
