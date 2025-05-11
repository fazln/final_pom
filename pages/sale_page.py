from pages.base_page import BasePage
from pages.locators import sale_locators as sale_loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_deals_quantity_more_(self, quantity):
        deals = self.find_elements(sale_loc.DEALS)
        assert len(deals) > quantity, 'Not all deals are loaded'

    def click_gear_link(self):
        return self.click(sale_loc.GEAR)
