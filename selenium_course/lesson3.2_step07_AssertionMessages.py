        Проверка ожидаемого результата

assert abs(-42) == -42, "Should be absolute value of a number"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be absolute value of a number


        Составные сообщения об ошибках 

Если вы проверяете наличие элемента, то обязательно пишите, что это за элемент по смыслу на странице: 
assert self.is_element_present('create_class_button', timeout=30), "No create class button"
#  Примечание: Функция is_element_present() вспомогательная. Как её реализовать и использовать, мы разберемся чуть позжe.

Если элемент встречается на нескольких страницах приложения, не лишним будет указать, где именно произошла ошибка: 
assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"

В сообщении об ошибке всегда лучше выводить оба значения: то, которое ожидалось, и то, которое получили по факту.
Всё как в хорошем багрепорте: ожидаемый и фактический результат.


        Форматирование строк с помощью конкатенации

В питоне такое можно провернуть с помощью конкатенации строк, например:
actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something went wrong")

Но из-за обилия кавычек, знаков сложения и вот этого всего этот способ не самый удобный и читается тоже плохо.


        Форматирование строк с помощью str.format

https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat

Python умеет подставлять пользовательские значения в строки с помощью функции .format(). 
Синтаксис выглядит примерно так:
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))


#  ТОЛЬКО PYTHON >= 3.6
        Форматирование строк с помощью f-strings

https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36

Наиболее современный способ форматирования строк, который появился в Python3.6, носит название f-strings
Он позволяет исполнять выражения на Python прямо внутри строк, обладает еще большей лаконичностью и удобством использования.
Для использования возможностей f-strings нужно указывать символ f перед строкой в таком формате: 
f"ваша строка {my_var}".

В фигурных скобках указывается имя переменной, значение которой надо подставить в строку, или выражение, результат исполнения которого также требуется подставить в вашу строку.

Пример 1:
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")
#  Let's count together: one, then goes two, and then three

Пример 2:
actual_result = "abrakadabra"
f"Wrong text, got {actual_result}, something wrong"
#  Wrong text, got abrakadabra, something wrong

Пример 3:
>>> f"{2+3}"
'5'


#  !!! ВНИМАНИЕ !!!
Когда вы работаете с текстом элементов на странице или любым другим контентом,
который может измениться, всегда записывайте его в отдельную переменную для сравнения. 

# !!! НЕПРАВИЛЬНО !!!

assert self.catalog_lin.text == "Каталог", \
    f"Wrong language, got {self.catalog_ling.text} instead of 'Каталог'"

Дважды считывать атрибут — это плохая практика, потому что при повторном считывании текст на странице может измениться,
и вы получите неактуальный текст об ошибке. Результат выполнения такого теста сложно анализировать.

# !!! ПРАВИЛЬНО !!!

catalog_text = self.catalog_link.text  # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"


#  Дополнительно
assert "login" in browser.current_url, # сообщение об ошибке
