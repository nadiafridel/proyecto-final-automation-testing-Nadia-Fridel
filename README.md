Proyecto Final - Framework de Automatización de Pruebas

Propósito
Este proyecto implementa un framework de automatización que combina pruebas de UI usando Selenium WebDriver y pruebas de API utilizando Requests. Se aplica el patrón Page Object Model (POM) para mantener una estructura clara, escalable y fácil de mantener.

Tecnologías utilizadas
Python
Pytest
Selenium WebDriver
Requests
Pytest-HTML
Git / GitHub

Estructura del proyecto
proyecto-final-automation-testing/
├── pages/
├── tests/
│ ├── test_ui/
│ └── test_api/
├── utils/
├── datos/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

Instalación
pip install -r requirements.txt

Ejecución de pruebas
pytest -v --html=reports/report.html

Reportes
Los reportes HTML se generan automáticamente en la carpeta reports/. Cuando una prueba falla:

Se captura un screenshot automáticamente.
La imagen se guarda en reports/screenshots/.
El reporte HTML muestra la captura asociada a la prueba fallida.

Autor
Nadia Fridel
