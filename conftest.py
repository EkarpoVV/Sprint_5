import pytest
from selenium import webdriver
import test_data as td


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver

