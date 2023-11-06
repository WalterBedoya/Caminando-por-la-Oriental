from modelo.jugador import Player
from view.interfaz import Interfaz

class Entrenar:
    def __init__(self, jugador: Player):
        self.jugador = jugador

    def aumentar_multiplicador_basico(self):
        self.jugador.xp -= 100
        self.jugador.multiplicador_basico += 1
        Interfaz.salida(
            f"Tu multiplicador de velocidad ha aumentado a {self.jugador.multiplicador_basico}.")

    def aumentar_multiplicador_poder(self):
        self.jugador.xp -= 100
        self.jugador.multiplicador_poder += 1
        Interfaz.salida(
            f"Tu multiplicador de asperosidad ha aumentado a {self.jugador.multiplicador_poder}.")
