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
      # Recorro cada línea del archivo (cada club)
    for linea in archivo_clubs:
        # Quito el salto de línea y separo los datos por el punto y coma (;)
        nombre, deporte, fundacion = linea.strip().split(";")
        # Convierto el año de fundación a número entero
        fundacion = int(fundacion)

        # Creo un objeto Club con los datos leídos
        club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
        # Agrego ese club a la sesión para guardarlo en la base de datos
        session.add(club)

        # Guardo este objeto club en un diccionario usando su nombre como clave
        # Esto me servirá luego para asignar los jugadores al club correcto
        clubs[nombre] = club

# Leemos el archivo de jugadores
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo_jugadores:
    # Recorro cada línea del archivo (cada jugador)
    for linea in archivo_jugadores:
        # Quito el salto de línea y separo los datos
        nombre_club, posicion, dorsal, nombre_jugador = linea.strip().split(";")
        # Convierto el dorsal a número entero
        dorsal = int(dorsal)

        # Busco el objeto Club correspondiente al nombre leído
        club = clubs[nombre_club]

        # Creo un objeto Jugador con los datos y lo relaciono con el club
        jugador = Jugador(nombre=nombre_jugador, dorsal=dorsal, posicion=posicion, club=club)
        # Agrego el jugador a la sesión para guardarlo en la base de datos
        session.add(jugador)

# Guardamos los cambios en la base de datos
session.commit()

