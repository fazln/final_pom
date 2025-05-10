from selenium.webdriver.common.by import By

FIRST_NAME = (By.ID, "firstname")
LAST_NAME = (By.XPATH, "//*[@title='Last Name']")
EMAIL = (By.ID, "email_address")
PASSWORD = (By.ID, "password")
CONFIRM_PASSWORD = (By.ID, "password-confirmation")
SUBMIT = (By.CSS_SELECTOR, "button.submit")
PASSWORD_ERROR = (By.ID, "password-error")
CONTACT_INFO = (By.XPATH, "//*[@class='box-content']/p")
