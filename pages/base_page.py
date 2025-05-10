from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def check_page_title(self, title):
        assert title == self.driver.title

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def move_mouse_to_element(self, locator):
        element = self.wait_for_element(locator)
        return ActionChains(self.driver).move_to_element(element).perform()

    def get_text_of_(self, locator):
        return self.wait_for_element(locator).text
