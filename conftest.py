from playwright.sync_api import sync_playwright
from utils.config_reader import load_config
from utils.data_loader import load_test_data
from pages.login_page import LoginPage
import os,time,pytest


@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture
def page(config):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=config["headless"])
    context = browser.new_context()
    page = context.new_page()

    page.goto(config["base_url"], wait_until="domcontentloaded")

    yield page

    browser.close()
    playwright.stop()

@pytest.fixture
def login_page(page):
    data = load_test_data()

    login = LoginPage(page)
    login.login(
        data["valid_login"]["username"],
        data["valid_login"]["password"]
    )
    return login

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when== "call" and report.failed:
        os.makedirs("screenshots", exist_ok=True)
        page = item.funcargs.get("page")
        timestamp = int(time.time())
        page.screenshot(path = f"screenshots/{item.name}_{timestamp}.png")
