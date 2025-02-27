from base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_guide(self):
        click_guide = self.browser.find_element(*MainPageLocators.guide)
        click_guide.click()