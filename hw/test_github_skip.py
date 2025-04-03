import pytest
from selene import browser, by


def show_screen_size(screen_size):
    return f"screen size: {screen_size[0]}x{screen_size[1]}"


@pytest.fixture(
    params=[(1920, 1080), (1600, 900), (375, 667), (412, 914)], ids=show_screen_size
)
def browser_setting(request):
    """Настраивает браузер и возвращает разрешение экрана."""
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield width, height
    browser.quit()


def test_github_desktop(browser_setting):
    width, _ = browser_setting
    if width <= 500:  # Если ширина экрана <= 500, значит это мобилка
        pytest.skip("Пропуск по причине мобильного разрешения")

    browser.open("https://github.com/")
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()


def test_github_mobile(browser_setting):
    width, _ = browser_setting
    if width > 500:  # Если ширина экрана больше 500, значит это десктоп
        pytest.skip("Пропуск по причине десктопного разрешения")

    browser.open("https://github.com/")
    browser.element(".Button-content").click()
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()
