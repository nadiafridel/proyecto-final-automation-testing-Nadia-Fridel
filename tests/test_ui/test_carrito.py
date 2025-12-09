import pytest
from pages.cart_page import CartPage

@pytest.mark.smoke
def test_navega_carrito(usuario_logueado):
    inventory_page = usuario_logueado
    carrito = inventory_page.ir_al_carrito()
    assert "cart.html" in carrito.driver.current_url

@pytest.mark.smoke    
def test_producto_correcto_en_carrito(usuario_logueado):
    inventory_page = usuario_logueado
    carrito = inventory_page.ir_al_carrito()

    nombres = carrito.obtener_nombres_productos()
    print(f"Producto(s) en el carrito: {nombres}")

   