import os
import csv
import pathlib

def get_file_path(file_name, folder="datos"):
    current_file = os.path.dirname(__file__)
    file_path = os.path.join(current_file,"..",folder,file_name)   #ruta relativa
    return os.path.abspath(file_path)                # se pasa a ruta absoluta


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

