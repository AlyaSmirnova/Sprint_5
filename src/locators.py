from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    # registration
    NAME_FIELD = By.NAME, "name"  # input "Name"
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input"  # input "Email"
    PASSWORD_FIELD = By.NAME, "Пароль" # input "Password"
    SUBMIT_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']" # "Sign up" button on the registration page
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]" # "Login" button on the registration page
    PASSWORD_ERROR_MESSAGE = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]" # message "Incorrect password"

    # login
    ACCOUNT_LOGIN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']" # "Login to Account" button
    MAKE_AN_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']" # "Make an order" button
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[@href='/account']" # "Personal Account" button
    LOGIN_HEADER = By.XPATH, "//h2[text()='Вход']" # "Log in" header
    LOGIN_LINK = By.XPATH, "//a[@href='/login']"
    REGISTRATION_LINK = By.XPATH, "//a[@href='/register']" # "Sign Up" link on the login page
    RECOVERY_PASSWORD_LINK = By.XPATH, "//a[@href='/forgot-password']" # "Recover password" link on the login page
    LOGIN_LINK_ON_RECOVERY_PASSWORD_PAGE = By.XPATH, "//a[@href='/login']" # "Log In" link on the password recovery page
    MODAL_OVERLAY = By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"

    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]" # "Constructor" button on the personal account page
    LOGO = By.XPATH, "//*[local-name()='svg' and @width='290' and @height='50' and @viewBox='0 0 290 50']" # logo on the personal account page

    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']" # "Log Out" button on the personal account page

    BUNS_SECTION = By.XPATH, "//span[text()='Булки']/parent::div" # "Buns" button on the main page
    ACTIVE_BUNS_SECTION = By.XPATH, "//span[text()='Булки']/ancestor::div[contains(@class, 'current')]"
    SAUCES_SECTION = By.XPATH, "//span[text()='Соусы']" # "Sauces" button on the main page
    ACTIVE_SAUCES_SECTION = By.XPATH, "//span[text()='Соусы']/ancestor::div[contains(@class, 'current')]"
    ADDINGS_SECTION = By.XPATH, "//span[text()='Начинки']"  # "Fillings" button on the main page
    ACTIVE_ADDINGS_SECTION = By.XPATH, "//span[text()='Начинки']/ancestor::div[contains(@class, 'current')]"
