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

# Leemos el archivo de clubes
with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo_clubs:
    for linea in archivo_clubs:
        nombre, deporte, fundacion = linea.strip().split(";")
        fundacion = int(fundacion)

        club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
        session.add(club)

        # Guardamos el objeto club para usarlo al agregar jugadores
        clubs[nombre] = club

# Leemos el archivo de jugadores
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo_jugadores:
    for linea in archivo_jugadores:
        nombre_club, posicion, dorsal, nombre_jugador = linea.strip().split(";")
        dorsal = int(dorsal)

        # Obtenemos el club correspondiente desde el diccionario
        club = clubs[nombre_club]

        jugador = Jugador(nombre=nombre_jugador, dorsal=dorsal, posicion=posicion, club=club)
        session.add(jugador)

# Guardamos los cambios en la base de datos
session.commit()

