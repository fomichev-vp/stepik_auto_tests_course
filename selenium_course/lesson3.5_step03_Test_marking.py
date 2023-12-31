#        Маркировка тестов

#    Инверсия
Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию.
Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:

pytest -s -v -m "not smoek" test_fixture8.py

#   Объединение тестов с разными маркировками
Для запуска тестов с разными метками можно использовать логическое ИЛИ.
Запустим smoke и regression-тесты:

pytest -s -v - "smoke or regression" test_fixture8.py

#   Выбор тестов, имеющих несколько маркировок
Предположим, у нас есть smoke-тесты, которые нужно запускать только для определенной операционной системы, например, для Windows 10.
Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:

pytest -s -v -m "smoke and win10" test_fixture8.py


#       Пропуск тестов
В PyTest есть стандартные метки, которые позволяют пропустить тест при сборе тестов для запуска (то есть не запускать тест)
или запустить, но отметить особенным статусом тот тест, который ожидаемо упадёт из-за наличия бага,
чтобы он не влиял на результаты прогона всех тестов.

Эти метки не требуют дополнительного объявления в pytest.ini.

Итак, чтобы пропустить тест, его отмечают в коде так:
@pytest.mark.skip

В результатах теста мы увидим, что один тест был пропущен, а другой успешно прошёл: "1 passed, 1 skipped".

# ! ВНИМАНИЕ !
Если маркировка skip добавляется к функции, где уже есть другие маркировки,
то skip должен быть последним маркером, иначе пропускаться не будет.

@pytest.mark.regression
@pytest.mark.win10
@pytest.mark.skip 

Также можно добавить строку "addopts = --strict-markers"  в pytest.ini,
благодаря ей при указании маркера отсутствующего в файле мы будем проинформированы ошибкой.

[pytest]
addopts = --strict-markers
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
    win 10: only for win10 OS