        Alerts

Alert является модальным окном:
пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert.

Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды accept()

alert1 = browser.switch_to.alert
alert1.accept()

Чтобы получить текст из alert, используйте свойство text объекта alert:

alert2 = browser.switch_to.alert
alert2_text = alert2.text

Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm.
Для переключения на окно confirm используется та же команда, что и в случае с alert:

confirm1 = browser.switch_to.alert
confirm1.accept()

Для confirm-окон можно использовать следующий метод для отказа:
То же самое, что и при нажатии пользователем кнопки "Отмена". 
confirm1.dismiss()


Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста.
Чтобы ввести текст, используйте метод send_keys():

prompt1 = browser.switch_to.alert
prompt1.send_keys("My answer")

prompt1.accept()

prompt1.dismiss()