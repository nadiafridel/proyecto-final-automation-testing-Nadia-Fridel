import pytest
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_productos_visibles(usuario_logueado):
    inventory_page = usuario_logueado
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0
    print(f'--- Cantidad de productos visibles: {len(productos)}.')

@pytest.mark.smoke
def test_elementos_importantes(usuario_logueado):
    inventory_page = usuario_logueado
    menu_btn, filtro = inventory_page.obtiene_elementos_importantes()
    assert menu_btn.is_displayed()
    assert filtro.is_displayed()
    print('--- Elementos principales presentes (Menú y Filtros).')

def test_primer_producto(usuario_logueado):
    inventory_page = usuario_logueado
    primer_producto = inventory_page.obtiene_primer_producto()  
    nombre = primer_producto['nombre']
    precio = primer_producto['precio']  
    print(f"--- El primer producto es '{nombre}' y el precio es {precio}.")  
    
def test_producto_carrito(usuario_logueado):    
    inventory_page = usuario_logueado
    inventory_page.agregar_primer_producto()
        
def test_contador_carrito(usuario_logueado):
    inventory_page = usuario_logueado
    inventory_page.agregar_primer_producto()
    contador = inventory_page.obtener_contador_carrito()
    assert contador == 1
    print('--- El carrito tiene un elemento.')

