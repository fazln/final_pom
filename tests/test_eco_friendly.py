import pytest
from data.expected_results import WARN_MESSAGES
from pages.locators import eco_friendly_locators as loc


@pytest.mark.smoke
def test_eco_friendly_page_title(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_page_title('Eco Friendly')


@pytest.mark.smoke
def test_load_items(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_load_items()


@pytest.mark.smoke
def test_add_item_to_compare(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.move_mouse_to_element(loc.ITEM_CARD)
    eco_friendly_page.click(loc.ADD_TO_COMPARE)
    item_name = eco_friendly_page.get_text_of_(loc.ITEM)
    eco_friendly_page.check_text_add_item_to_compare(item_name)
    eco_friendly_page.check_add_item_to_compare(item_name)


@pytest.mark.regress
def test_add_item_to_cart_without_options(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.move_mouse_to_element(loc.ITEM_CARD)
    eco_friendly_page.click(loc.ADD_TO_CART)
    eco_friendly_page.check_add_item_without_options(WARN_MESSAGES['add_to_cart'])
