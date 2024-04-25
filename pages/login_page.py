from base_page import BasePage
from locators import MainPageLocators

class LoginPage(BasePage):
    def get_click_guide_page(self):
        self.get_click_guide()

    def get_click_guide(self):
        assert MainPageLocators.guide.is_displayed(),"Button Guide is present"