import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password, expected_error", [
    ("standart_user", "secret_sauce", None),
    # ("locked_out_user", "secret_sauce", 'Epic sadface: Sorry, this user has been locked out.'),
    # ("", "secret_sauce", 'Epic sadface: Username is required'),
    # ("standart_user", "", 'Epic sadface: Password is required'),
    # ("wrong_user", "wrong_pass", 'Epic sadface: Username and password do not match any user in this service')
])
@pytest.mark.parametrize("browser_context", ["chromium", "firefox", "webkit"], indirect=True)
def test_login(browser_context, username, password, expected_error):
    page = browser_context.new_page()
    login_page = LoginPage(page)
    login_page.goto("https://www.saucedemo.com/")
    login_page.login(username, password)

    if expected_error:
        assert login_page.get_error_message() == expected_error
    else:
        assert page.url == "https://www.saucedemo.com/inventory.html"

    page.close()
