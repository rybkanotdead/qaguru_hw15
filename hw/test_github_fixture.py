import pytest
from selene import browser, by

def show_screen_size(screen_size):
    return f"screen size: {screen_size[0]}x{screen_size[1]}"

@pytest.fixture(params=[(1920, 1080), (1600, 900), (1280, 720), (412, 914), (430, 932), (375, 667)], ids=show_screen_size)
def browser_setup(request):
    """Настраивает браузер в разных разрешениях."""
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

@pytest.mark.parametrize("browser_setup", [(1920, 1080), (1600, 900), (1280, 720)], indirect=True)
def test_github_desktop(browser_setup):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()

@pytest.mark.parametrize("browser_setup", [(412, 914), (430, 932), (375, 667)], indirect=True)
def test_github_mobile(browser_setup):
    browser.open("https://github.com/")
    browser.element(".Button-content").click()
    browser.element(".HeaderMenu-wrapper").element(by.text("Sign up")).click()
