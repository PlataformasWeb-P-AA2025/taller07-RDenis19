from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa las clases del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Diccionario para almacenar los objetos Club
clubs = {}

# Lectura del archivo de datos de clubes
archivo_clubs = open("data/datos_clubs.txt", "r", encoding="utf-8")
for linea in archivo_clubs:
    datos = linea.strip().split(";")
    nombre = datos[0]
    deporte = datos[1]
    fundacion = int(datos[2])
    
    