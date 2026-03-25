from selenium.webdriver.common.by import By

class MainPage:
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, ".//div[@class = 'header_flexRow__Xdqv1']/button[text() = 'Вход и регистрация']")
    USER_ICON = (By.CSS_SELECTOR, "button.circleSmall") ## Я не понимаю почему  не происходит клик, просьба посдказать как составить локатор
    USER_NAME = (By.XPATH,"//div[@class = 'columnSmall']//h3[text()='User.']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выйти']") 
    CREATE_AD_BUTTON = (By.XPATH, "//button[text() = 'Разместить объявление']")

class LoginPopUp:  
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    NO_ACCAUNT_BUTTON = (By.XPATH, "//button[text() = 'Нет аккаунта']")
    REGISTRATION_POPUP = (By.XPATH, "//div[@class = 'popUp_titleRow__M7tGg']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME,"password")

class RegistartionPopUp:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME,"password")
    REPEAT_PASSWORD_FIELD = (By.NAME,"submitPassword")
    BUTTON_CREATE = (By.XPATH,"//div[@class = 'popUp_buttonRow__+W8JD']/button[text() = 'Создать аккаунт']")
    ERROR = (By.XPATH, ".//span[text() = 'Ошибка']") 
    EMAIL_RED_BORDER = (By.XPATH, "//input[@name = 'email']/parent::div[@class = 'input_inputError__fLUP9']")
    PASSWORD_RED_BORDER = (By.XPATH, "//input[@name = 'password']/parent::div[@class = 'input_inputError__fLUP9']")
    PASSWORD2_RED_BORDER = (By.XPATH, "//input[@name = 'submitPassword']/parent::div[@class = 'input_inputError__fLUP9']")

class CreatingAd:
    UNAUTORISED_POPUP = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    NAME_AD = (By.NAME, "name")
    PRICE_AD = (By.NAME, "price")
    PRODUCT_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    PUBCLICATION_BUTTON = (By.XPATH, "//button[text() = 'Опубликовать']")

class Dropdwns:
    CATEGORY = (By.CSS_SELECTOR, 'div.dropDownMenu_input__itKtw input[name="category"] + button')
    CITY = (By.CSS_SELECTOR, 'div.dropDownMenu_input__itKtw input[name="city"] + button')
    CITY_CHOICE = (By.XPATH, "//button[.//span[text() = 'Казань']]")
    CATEGORY_CHOICE = (By.XPATH, "//button[.//span[text() = 'Книги']]")

class Profile:
    PROFILE_TITLE = (By.XPATH, '//h1[text()="Мой профиль"]')
    CARD_AD = (By.XPATH, "//div[@class='card']")

class RadioButton:
    ##Я не понимаю почему закомиченные не работают
    ##RADIOBUTTON_USED = (By.XPATH, '//div[@class="radioUnput_shell__Wtdwe"][.//label[text()="Б/У"]]')
    ##RADIOBUTTON_USED = (By.XPATH,"//label[text()='Б/У']")
    RADIOBUTTON_USED = (By.CLASS_NAME, "radioUnput_inputRegular__FbVbr")

