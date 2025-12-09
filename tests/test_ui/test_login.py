import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login
from utils.logger import logger

CASOS_LOGIN = leer_csv_login('login.csv')

@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    login = LoginPage(driver)
    login.abrir().login_completo(usuario, clave)

    if debe_funcionar:
        assert "inventory.html" in driver.current_url, f"Falló login válido: {descripcion}"
    else:
        assert login.esta_error_visible(), f"Error esperado no apareció: {descripcion}"


@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    logger.info("Iniciando test de login exitoso")
    
    login = LoginPage(driver)
    login.abrir().login_completo("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url
    logger.info("Login exitoso completado")



