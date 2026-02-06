from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import data.test_data as td
from config import *


class TestRegistration:

    def test_registration_valid_user(self, driver):

        driver.find_element(*MainPage.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((LoginPopUp.NO_ACCAUNT_BUTTON)))
        driver.find_element(*LoginPopUp.NO_ACCAUNT_BUTTON).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((RegistartionPopUp.EMAIL_FIELD)))
        driver.find_element(*RegistartionPopUp.EMAIL_FIELD).send_keys(td.random_email)
        driver.find_element(*RegistartionPopUp.PASSWORD_FIELD).send_keys(td.VALID_PASSWORD)
        driver.find_element(*RegistartionPopUp.REPEAT_PASSWORD_FIELD).send_keys(td.VALID_PASSWORD)
        driver.find_element(*RegistartionPopUp.BUTTON_CREATE).click()

        icon = WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((MainPage.USER_ICON)))
        user_name =  WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((MainPage.USER_NAME)))

        assert icon.is_displayed() and user_name.is_displayed()


    def test_registration_incorrect_format_email(self, driver):

        driver.find_element(*MainPage.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((LoginPopUp.NO_ACCAUNT_BUTTON)))
        driver.find_element(*LoginPopUp.NO_ACCAUNT_BUTTON).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((RegistartionPopUp.EMAIL_FIELD)))
        driver.find_element(*RegistartionPopUp.EMAIL_FIELD).send_keys("12Waiter.WAIT_TIME.ru")
        driver.find_element(*RegistartionPopUp.PASSWORD_FIELD).send_keys(td.VALID_PASSWORD)
        driver.find_element(*RegistartionPopUp.REPEAT_PASSWORD_FIELD).send_keys(td.VALID_PASSWORD)
        driver.find_element(*RegistartionPopUp.BUTTON_CREATE).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((RegistartionPopUp.ERROR)))
        error = driver.find_element(*RegistartionPopUp.ERROR)
        email_red_border = driver.find_element(*RegistartionPopUp.EMAIL_RED_BORDER)
        password_red_border = driver.find_element(*RegistartionPopUp.PASSWORD_RED_BORDER)
        password2_red_border = driver.find_element(*RegistartionPopUp.PASSWORD2_RED_BORDER)
        
        assert email_red_border.is_displayed() and password_red_border.is_displayed() and password2_red_border.is_displayed() and  error.is_displayed()

    def test_registration_exist_user(self, driver):

        driver.find_element(*MainPage.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((LoginPopUp.NO_ACCAUNT_BUTTON)))
        driver.find_element(*LoginPopUp.NO_ACCAUNT_BUTTON).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((RegistartionPopUp.EMAIL_FIELD)))
        email_for_test = td.random_email
        driver.find_element(*RegistartionPopUp.EMAIL_FIELD).send_keys(email_for_test)
        driver.find_element(*RegistartionPopUp.PASSWORD_FIELD).send_keys(td.VALID_PASSWORD)
        driver.find_element(*RegistartionPopUp.REPEAT_PASSWORD_FIELD).send_keys(td.VALID_PASSWORD)
        driver.find_element(*RegistartionPopUp.BUTTON_CREATE).click()

        WebDriverWait(driver,Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((MainPage.LOGOUT_BUTTON)))
        driver.find_element(*MainPage.LOGOUT_BUTTON).click()
        
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((MainPage.LOGIN_AND_REGISTRATION_BUTTON)))
        driver.find_element(*MainPage.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((LoginPopUp.NO_ACCAUNT_BUTTON)))
        driver.find_element(*LoginPopUp.NO_ACCAUNT_BUTTON).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((RegistartionPopUp.EMAIL_FIELD)))
        driver.find_element(*RegistartionPopUp.EMAIL_FIELD).send_keys(email_for_test)
        driver.find_element(*RegistartionPopUp.PASSWORD_FIELD).send_keys(td.VALID_PASSWORD)
        driver.find_element(*RegistartionPopUp.REPEAT_PASSWORD_FIELD).send_keys(td.VALID_PASSWORD)
        driver.find_element(*RegistartionPopUp.BUTTON_CREATE).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((RegistartionPopUp.ERROR)))
        error = driver.find_element(*RegistartionPopUp.ERROR)
        email_red_border = driver.find_element(*RegistartionPopUp.EMAIL_RED_BORDER)
        password_red_border = driver.find_element(*RegistartionPopUp.PASSWORD_RED_BORDER)
        password2_red_border = driver.find_element(*RegistartionPopUp.PASSWORD2_RED_BORDER)
        
        assert email_red_border.is_displayed() and password_red_border.is_displayed() and password2_red_border.is_displayed() and  error.is_displayed()
