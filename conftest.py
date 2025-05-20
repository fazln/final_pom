from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.locators import cookie_locators as loc
from selenium.common import TimeoutException
from pages.base_page import BasePage
from pages.register_page import RegisterPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def accept_cookie(base_page):
    """launching via VPN"""
    try:
        base_page.wait_for_element(loc.ACCEPT_COOKIE).click()
    except TimeoutException:
        pass


@pytest.fixture()
def base_page(driver):
    return BasePage(driver)


@pytest.fixture()
def register_page(driver):
    return RegisterPage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
