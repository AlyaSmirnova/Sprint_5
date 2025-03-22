# UI-тесты для сайта Stellar Burgers

## Оглавление
1. [Описание] (#описание)
2. [Тестирование] (#тестирование)

## Описание

Этот проект включает автотесты для проверки UI различных элементов на сайте **Stellar Burgers**, включая: 

- регистрации нового пользователя 
- вход через формы регистрации и восстановления пароля
- Проверки кликов по кнопкам и ссылкам (например, на логотип, "Личный кабинет", "Конструктор")
- Проверка работы кнопки "Выход" в личном кабинете

## Тестирование
Все тесты написаны с использованием Selenium WebDriver и Pytest. тесты проверяют следующие функциональности и элементы: 
1. Успешную регистрацию новго пользователя; 
2. Проверку ошибки регистрации при вводе некорректного пароля; 
3. Проверку входа в аккаунт через кнопку "Войти в аккаунт" на главной странице сайта; 
4. Проверку входа в аккаунт через кнопку "Личный кабинет"; 
5. Проверку входа через кнопку в форме регистрации; 
6. Проверку входа через кнопку в форме восстановления пароля; 
7. Проверку перехода в аккаунт по по клику на кнопку "Личный кабинет"; 
8. Проверку перехода в раздел "Конструктор" из раздела "Личный кабинет";
9. Проверку перехода на главную страницу по клику на логотип из раздела "Личный кабинет";
10. Выход из аккаунта по кнопке "Выход";
11. Проверки перехода по разделам "Булки", "Соусы" и "Начинки".
