import pytest
from pages.locators import sale_locators as sale_loc


@pytest.mark.smoke
def test_sale_page_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_title('Sale')


@pytest.mark.smoke
def test_sale_has_deals(sale_page):
    sale_page.open_page()
    sale_page.check_load_deals()


@pytest.mark.regress
def test_gear_link(sale_page):
    sale_page.open_page()
    sale_page.click(sale_loc.GEAR)
    sale_page.check_page_title('Gear')
