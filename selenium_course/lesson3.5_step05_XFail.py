#       XFail: помечать тест как ожидаемо падающий

Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":

def test_guest_should_see_search_button_on_the_main_page(self, browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.favorite")

Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала.
Пока разработчики исправляют баг, мы хотим, чтобы результат прогона ﻿всех ﻿наших тестов был успешен,
но падающий тест помечался соответствующим образом, чтобы про него не забыть.

Добавим маркировку @pytest.mark.xfail для падающего теста.
Смотреть файл test_fixture10.py

Запустим наши тесты:
pytest -v test_fixture10.py

Наш упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный.

Когда баг починят, мы это узнаем, ﻿﻿так как теперь тест будет отмечен как XPASS (“unexpectedly passing” — неожиданно проходит).
После этого маркировку xfail для теста можно удалить.
К маркировке xfail можно добавлять параметр reason.
Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx.

Смотреть файл test_fixture10a.py

Запустим наши тесты:
pytest -rx -v test_fixture10a.py


#       XPASS-тесты

Поменяем селектор в последнем тесте, чтобы тест начал проходить.

Смотреть файл test_fixture10b.py

Запустите тесты. Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам:

pytest -rX -v test_fixture10b.py
