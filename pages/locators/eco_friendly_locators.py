from selenium.webdriver.common.by import By
from random import randint

ITEMS = (By.XPATH, "//*[@class='item product product-item']")
item_number = randint(1, 12)
ITEM_CARD = (By.XPATH, f"//*[@class='item product product-item'][{item_number}]")
ITEM = (By.XPATH, f"(//*[@class='product name product-item-name'])[{item_number}]")
COMPARE_ITEM = (By.XPATH, "//*[@class='product-item-name']")
ADD_TO_COMPARE = (By.XPATH, f"(//a[@title='Add to Compare'])[{item_number}]")
ADD_TO_CART = (By.XPATH, f"(//button[@title='Add to Cart'])[{item_number}]")
WARNING_ADD = (By.XPATH, "//*[contains(text(), 'You need')]")
SUCCESS_COMPARE = (By.XPATH, "//*[contains(text(), 'You added product')]")
