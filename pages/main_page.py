from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, browser):
        # Вызываем конструктор родительского класса BasePage
        super().__init__(browser, "http://selenium1py.pythonanywhere.com/")
    
    # Можно добавить дополнительные методы для работы с главной страницей
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()