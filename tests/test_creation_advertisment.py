from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import test_data as td
import time
from config import *

class TestAdvertisment:

    def test_create_ad_unauthorized_user(self, driver):
        driver.find_element(*MainPage.CREATE_AD_BUTTON).click()
        popup = WebDriverWait(driver,Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((CreatingAd.UNAUTORISED_POPUP)))
        
        assert popup.is_displayed()

    def test_create_ad(self, driver):
        driver.find_element(*MainPage.LOGIN_AND_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((LoginPopUp.LOGIN_BUTTON)))
        driver.find_element(*LoginPopUp.EMAIL_FIELD).send_keys(td.REGISTRED_MAIL_USER)
        driver.find_element(*LoginPopUp.PASSWORD_FIELD).send_keys(td.REGISTRED_PASSWORD_USER)
        driver.find_element(*LoginPopUp.LOGIN_BUTTON).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((MainPage.USER_ICON)))
        driver.find_element(*MainPage.CREATE_AD_BUTTON).click() 

        driver.find_element(*CreatingAd.NAME_AD).send_keys(td.random_name_card)
        driver.find_element(*CreatingAd.PRODUCT_DESCRIPTION).send_keys(td.ad_description)
        driver.find_element(*CreatingAd.PRICE_AD).send_keys(int(777))
        driver.find_element(*Dropdwns.CATEGORY).click()
        driver.find_element(*Dropdwns.CATEGORY).click()
        driver.find_element(*Dropdwns.CITY).click()
        driver.find_element(*Dropdwns.CITY_CHOICE).click()
        driver.find_element(*RadioButton.RADIOBUTTON_USED).click()
        driver.find_element(*CreatingAd.PUBCLICATION_BUTTON).click()

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.element_to_be_clickable((MainPage.USER_ICON)))
        element = driver.find_element(*MainPage.USER_ICON)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.execute_script("arguments[0].click();", element) ## Я не понимаю почему  не происходит клик, просьба посдказать как составить локатор
      

        WebDriverWait(driver, Waiter.WAIT_TIME).until(expected_conditions.visibility_of_element_located((Profile.PROFILE_TITLE)))

        cards = driver.find_elements(*Profile.CARD_AD)

        assert len(cards) > 0
