from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    # регистрация
    NAME_FIELD = By.NAME, "name"  #поле "Имя"
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input"  #поле "Email"
    PASSWORD_FIELD = By.NAME, "Пароль" #поле "Пароль"
    SUBMIT_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']" #кнопка "Зарегистрироваться" на странице регистрации
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]" #кнопка Войти" на странице регистрации
    PASSWORD_ERROR_MESSAGE = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]" #сообщение "Некорректный пароль"

    # вход
    ACCOUNT_LOGIN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']" #кнопка "Войти в аккаунт"
    MAKE_AN_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']" #кнопка "Оформить заказ"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[@href='/account']" #кнопка "Личный кабинет"
    LOGIN_HEADER = By.XPATH, "//h2[text()='Вход']" #заголовок "Вход"
    LOGIN_LINK = By.XPATH, "//a[@href='/login']"
    REGISTRATION_LINK = By.XPATH, "//a[@href='/register']" #ссылка "Зарегистрироваться" на странице входа
    RECOVERY_PASSWORD_LINK = By.XPATH, "//a[@href='/forgot-password']" #ссылка "Восстановить пароль" на странице входа
    LOGIN_LINK_ON_RECOVERY_PASSWORD_PAGE = By.XPATH, "//a[@href='/login']" #ссылка "Войти" на странице восстановления пароля

    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]" #кнопка "Конструктор" на странице Личного кабинета
    LOGO = By.XPATH, "//*[local-name()='svg' and @width='290' and @height='50' and @viewBox='0 0 290 50']" #лого на странице Личного кабинета

    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']" #кнопка "Выход" на странице Личного кабинет

    BUNS_SECTION = By.XPATH, "//span[text()='Булки']/parent::div" #кнопка "Булки" на главной странице
    ACTIVE_BUNS_SECTION = By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'current')]"
    SAUCES_SECTION = By.XPATH, "//span[text()='Соусы']" #кнопка "Соусы" на главной странице
    ACTIVE_SAUCES_SECTION = By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]"
    ADDINGS_SECTION = By.XPATH, "//span[text()='Начинки']"  # кнопка "Начинки" на главной странице
    ACTIVE_ADDINGS_SECTION = By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]"
