import pytest
from selene import browser, by

# Функция для отображения разрешений в отчете
def show_screen_size(screen_size):
    return f"screen size: {screen_size[0]}x{screen_size[1]}"

# Фикстура для настройки браузера с разрешениями
@pytest.fixture(params=[(1920, 1080), (1600, 900), (375, 667), (412, 914)], ids=show_screen_size)
def browser_setting(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

# Тест для десктопных разрешений
@pytest.mark.parametrize("browser_setting", [(1920, 1080), (1600, 900)], indirect=True)
def test_github_desktop(browser_setting):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()

# Тест для мобильных разрешений
@pytest.mark.parametrize("browser_setting", [(375, 667), (412, 914)], indirect=True)
def test_github_mobile(browser_setting):
    browser.open("https://github.com/")
    browser.element(".Button-content").click()
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()
