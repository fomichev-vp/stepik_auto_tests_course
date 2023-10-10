        Загрузка файлов

Если нам понадобится загрузить файл на веб-странице, мы можем использовать уже знакомый нам метод send_keys.
Только теперь нам нужно в качестве аргумента передать путь к нужному файлу на диске вместо простого текста.

Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой — os.
В этом случае ваш код не будет зависеть от операционной системы, которую вы используете.

Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт, который вы запускаете:

import os

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
element.send_keys(file_path)


Попробуйте добавить в файл отдельно команды 
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
и посмотрите на разницу.

Подробнее о методах модуля os можете почитать самостоятельно в документации: https://docs.python.org/3/library/os.path.html.

# ВНИМАНИЕ
Это будет работать только при запуске кода из файла, в интерпретаторе не сработает.


# ПРИМЕР

Допустим, мы написали код скрипта и сохранили код в lesson2_step7.py в своей локальной папке D:\stepik_homework.
Активируем виртуальное окружение и запускаем его python lesson2_step7.py.
В таком случае конструкция os.path.abspath(os.path.dirname(__file__)) вернет нам путь до директории файла с кодом, то есть D:\stepik_homework.
В эту же папку кладем файл, который хотим прикрепить, то есть file.txt.
Тогда, после выполнения команды:

file_path = os.path.join(current_dir, 'file.txt')

В переменной file_path будет полный путь к файлу 'D:\stepik_homework\file.txt'.
Фишка в том, что если мы файлы lesson2_step7.py вместе с file.txt перенесем в другую папку, или на компьютер с другой ОС, то такой код без правок заработает и там. 


Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file".
Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path).







# ДОПОЛНЕНИЕ И КРАТКОЕ ПОЯСНЕНИЕ

Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
Три способа задать путь к файлу:

1. вбить руками

element.send_keys("/home/user/stepik/Chapter2/file_example.txt")

 

2. задать с помощью переменных

# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)
# отправляем файл
element.send_keys(file_path)
3.путь автоматизатора.
если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
element.send_keys(file_path)
"""
итоговый код:

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)