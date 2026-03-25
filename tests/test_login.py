from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import test_data as td
from config import *


class TestLogin:

    def test_user_login(self, driver):

        driver.find_element(*MainPage.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((LoginPopUp.LOGIN_BUTTON)))
        driver.find_element(*LoginPopUp.EMAIL_FIELD).send_keys(td.REGISTRED_MAIL_USER)
        driver.find_element(*LoginPopUp.PASSWORD_FIELD).send_keys(td.REGISTRED_PASSWORD_USER)
        driver.find_element(*LoginPopUp.LOGIN_BUTTON).click()

        icon = WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((MainPage.USER_ICON)))
        user_name =  WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((MainPage.USER_NAME)))

        assert icon.is_displayed() and user_name.is_displayed()

    

    def test_user_logout(self, driver):

        driver.find_element(*MainPage.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((LoginPopUp.LOGIN_BUTTON)))
        driver.find_element(*LoginPopUp.EMAIL_FIELD).send_keys(td.REGISTRED_MAIL_USER)
        driver.find_element(*LoginPopUp.PASSWORD_FIELD).send_keys(td.REGISTRED_PASSWORD_USER)
        driver.find_element(*LoginPopUp.LOGIN_BUTTON).click()

        WebDriverWait(driver,Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((MainPage.LOGOUT_BUTTON)))
        driver.find_element(*MainPage.LOGOUT_BUTTON).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.invisibility_of_element_located((MainPage.USER_ICON)))
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.invisibility_of_element_located((MainPage.USER_NAME)))
        
        assert driver.find_element(*MainPage.LOGIN_AND_REGISTRATION_BUTTON) and not driver.find_elements(*MainPage.USER_ICON) and not driver.find_elements(*MainPage.USER_NAME)

 