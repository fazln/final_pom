from pages.base_page import BasePage
from pages.locators import sale_locators as sale_loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_load_deals(self):
        deals = self.find_elements(sale_loc.DEALS)
        assert len(deals) > 0
