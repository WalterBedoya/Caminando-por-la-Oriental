from modelo.jugador import Player
import pickle
from view.interfaz import Interfaz

class Tabla_de_posiciones:

    def __init__(self):
        self.listado: list[Player] = []

    def agregar_jugador(self, jugador: Player):
        self.listado.append(jugador)
        self.listado.sort(key=Player.comparar_victorias, reverse=True)

    def cargar_tabla(self):
        with open("tablaposiciones.txt", "rb") as archivo:
            self.listado = pickle.load(archivo)
            #Interfaz.salida("Tab cargado con exito!")

    def guardar_tabla(self):
        with open("tablaposiciones.txt", "wb") as archivo:
            pickle.dump(self.listado, archivo)


    def ver_tabla_de_posiciones(self):
        Interfaz.salida("Tabla de posiciones")
        Interfaz.salida("__________________________")
        for i in (self.listado):
            Interfaz.salida(i.nombre, " se ha bajado a ", i.victorias, " ñeritos en la oriental")
            Interfaz.salida("-")

    