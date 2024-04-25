from pages.main_page import MainPage
from pages.base_page import BasePage

def test_guest_can_go_to_login_page(browser):
    url = "https://openweathermap.org/"
    page = MainPage(browser, url)
    page.open()
    page.go_to_guide()
