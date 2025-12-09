import csv
import pathlib

def leer_csv_login(csv_file="login.csv"):
    csv_file = pathlib.Path(__file__).parent.parent / "datos" / csv_file
  
    with open(csv_file, newline='') as archivo:
        lector = csv.DictReader(archivo)

        return [
            (
                row["usuario"],
                row["clave"],
                row["debe_funcionar"].strip().lower() == "true",
                row["descripcion"]
            )
            for row in lector    
        ]
