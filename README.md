# Proyecto Final - Framework de Automatización de Pruebas

## Propósito
Este proyecto implementa un framework de automatización de pruebas que combina pruebas de UI (Selenium WebDriver) y pruebas de API (Requests), utilizando el patrón Page Object Model (POM).

## Tecnologías utilizadas
- Python
- Pytest
- Selenium WebDriver
- Requests
- Git / GitHub
- Pytest-HTML

## Estructura del proyecto
pages/
tests/
utils/
datos/
reports/
conftest.py
pytest.ini
requirements.txt

## Instalación
pip install -r requirements.txt

## Ejecución de pruebas
pytest -v --html=reports/report.html

## Reportes
Los reportes HTML se generan en la carpeta `reports/`.  
Cuando una prueba falla, se capturan screenshots automáticamente y se adjuntan al reporte.

## CI/CD
El proyecto incluye integración con GitHub Actions, que ejecuta las pruebas automáticamente al hacer push al repositorio.

## Autor
Nadia Fridel
