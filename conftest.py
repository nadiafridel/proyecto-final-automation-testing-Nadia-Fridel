import os
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_html import extras

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import logging

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def credenciales_validas():
    return {"usuario": "standard_user", "password": "secret_sauce"}

@pytest.fixture
def usuario_logueado(driver, credenciales_validas):
    login_page = LoginPage(driver)
    login_page.abrir().login_completo(
        credenciales_validas["usuario"],
        credenciales_validas["password"]
    )
    return InventoryPage(driver)

# Hook de captura automática
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)

            driver.save_screenshot(screenshot_path)

            # Guardamos la ruta en el reporte
            rep.extra = getattr(rep, "extra", [])
            rep.extra.append(extras.image(screenshot_path))


@pytest.fixture(scope="session", autouse=True)
def configurar_logging():
    os.makedirs("reports/logs", exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("reports/logs/test_execution.log", mode="w")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("=== INICIO DE EJECUCIÓN DE TESTS ===")              
