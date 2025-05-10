from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as eco_loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_load_items(self):
        items = self.find_elements(eco_loc.ITEMS)
        assert len(items) == 12, 'Not all products are loaded'

    def check_text_add_item_to_compare(self, item_name):
        success_compare = self.get_text_of_(eco_loc.SUCCESS_COMPARE)
        assert success_compare == f'You added product {item_name} to the comparison list.', \
                                    'The text not match for successful registration'

    def check_add_item_to_compare(self, item_name):
        compare_item = self.get_text_of_(eco_loc.COMPARE_ITEM)
        assert item_name == compare_item, f"Expected '{item_name}' in cart, but got '{compare_item}'"

    def check_add_item_without_options(self, text):
        warning_message = self.wait_for_element(eco_loc.WARNING_ADD).text
        assert text == warning_message, f"Expected '{text}' in cart, but got '{warning_message}'"
