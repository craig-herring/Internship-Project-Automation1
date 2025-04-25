from selenium.webdriver.common.by import By
from Pages.base_page import Page

class MainPage(Page):
    CONT_BTN = (By.XPATH, "//a[@wized='loginButton']")
    MARKET_BTN = (By.XPATH, "//a[@href='/market-companies']")
    FWRD_BTN = (By.XPATH, "//a[@wized='nextPageMarket']")
    BACK_BTN = (By.XPATH, "//div[@wized='previousPageMarket']")

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')

    def log_in(self):
        self.click(*self.CONT_BTN)

    def open_market(self):
        self.click(*self.MARKET_BTN)

    def page_forward(self):
        self.click(*self.FWRD_BTN)

    def page_back(self):
        self.click(*self.BACK_BTN)