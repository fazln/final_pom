from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as eco_loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_items_quantity(self, quantity):
        items = self.find_elements(eco_loc.ITEMS)
        assert len(items) == quantity, 'Not all items are loaded'

    def check_text_add_item_to_compare(self, text):
        success_compare = self.get_text_of_(eco_loc.SUCCESS_COMPARE)
        assert success_compare == text

    def check_add_item_to_compare(self, item_name):
        compare_item = self.get_text_of_(eco_loc.COMPARE_ITEM)
        assert item_name == compare_item, f"Expected '{item_name}' in cart, but got '{compare_item}'"

    def check_add_item_without_options(self, text):
        warning_message = self.wait_for_element(eco_loc.WARNING_ADD).text
        assert text == warning_message, f"Expected '{text}' in cart, but got '{warning_message}'"

    def move_mouse_to_item_card(self):
        return self.move_mouse_to_element(eco_loc.ITEM_CARD)

    def get_item_name(self):
        return self.get_text_of_(eco_loc.ITEM)

    def add_item_to_compare(self):
        return self.click(eco_loc.ADD_TO_COMPARE)

    def add_item_to_cart(self):
        return self.click(eco_loc.ADD_TO_CART)
