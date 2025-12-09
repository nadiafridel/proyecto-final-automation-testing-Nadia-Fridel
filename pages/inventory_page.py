from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        return self.driver.find_element(*self._TITLE).text
 
    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTS)
    
    def obtiene_elementos_importantes(self):
         return (
        self.driver.find_element(By.ID, 'react-burger-menu-btn'),
        self.driver.find_element(By.CLASS_NAME, 'product_sort_container')
    )

    def obtiene_primer_producto(self):
        productos = self.driver.find_elements(*self._PRODUCTS)
        primer_producto = productos[0]    
        nombre = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_name').text
        precio = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_price').text
        return {"nombre": nombre, "precio": precio}
 
    def agregar_primer_producto(self):
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]
        primer_boton.click()
        return self
 
    def obtener_contador_carrito(self):
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0
 
    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()
  
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def hacer_logout(self):
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        logout_link.click()
        from pages.login_page import LoginPage
        return LoginPage(self.driver)
