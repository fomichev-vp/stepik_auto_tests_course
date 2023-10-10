python3 --version
Python 3.7.3

$ mkdir environments
$ cd environments
Создадим виртуальное окружение с помощью команды python3:

$ python3 -m venv selenium_env
Активируем окружение:

$ source selenium_env/bin/activate

Проверим, что мы можем ﻿﻿теперь использовать Python. Запустим интерпретатор Python и напишем собственную версию HelloWorld. В итоге мы должны увидеть вывод строки "Hello, Selenium!":


$ source selenium_env/bin/activate

﻿(selenium_env) alekspog@xenial:~/environments$ python

﻿>>> print("Hello, Selenium!")

Hello, Selenium
Теперь выйдем из интерпретатора:

>>> exit()

Установка Selenium для Python

pip install selenium==4.*

Проверим, что библиотека действительно установлена:

pip list

Установка драйвера для браузера: macOS

brew install wget

Для установки драйвера откройте сайт https://sites.google.com/chromium.org/driver/ и скопируйте ссылку на ту версию ChromeDriver
cd ~/Downloads
wget https://chromedriver.storage.googleapis.com/76.0.3809.68/chromedriver_mac64.zip

Разархивируйте скачанный файл и переместите его в папку /usr/local/bin, чтобы он был глобально доступен в вашей системе.

unzip chromedriver_mac64.zip
sudo mv chromedriver /usr/local/bin
Проверим, что нужная версия chromedriver установлена.

chromedriver --version
Мы должны увидеть ответ системы:

ChromeDriver 76.0.3809.68 (420c9498db8ce8fcd190a954d51297672c1515d5-refs/branch-heads/3809@{#864})


Запуск браузера и первый скрипт
Для всех ОС:
В нашем виртуальном окружении запустим интерпретатор python:  

~/environments$ python 
