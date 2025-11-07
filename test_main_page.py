from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    # Создаем экземпляр MainPage
    page = MainPage(browser)
    # Открываем страницу
    page.open()
    # Переходим на страницу логина
    page.go_to_login_page()
    
    # Можно добавить проверку, что мы действительно перешли на страницу логина
    current_url = browser.current_url
    assert "login" in current_url, "Login page is not opened"