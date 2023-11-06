from modelo.jugador import Player
from modelo.mochila import Pocion
from modelo.cantidadinvalidaderror import CantidadInvalidaError
from modelo.Oro_ERROR import NoSuficientesPesosError
from view.interfaz import Interfaz
from modelo.pocion import Pocion


class Store:

    def __init__(self,cantidad, jugador: Player):
        self.cantidad = int(cantidad)
        self.jugador = jugador

    def comprar_objeto(self) -> None:
        try:
            if self.cantidad < 1 or self.cantidad > 5:
                raise CantidadInvalidaError()

            if len(self.jugador.mochila.pociones) == 5:
                Interfaz.salida("Tu costal ya contiene 5 tarritos de sacol. No puedes comprar más.")
            else:
                costo_total = self.cantidad * 70
                if self.jugador.monedas >= costo_total:
                    for _ in range(self.cantidad):
                        if len(self.jugador.mochila.pociones) < 5:
                            self.jugador.mochila.pociones.append(Pocion())
                            self.jugador.monedas -= 70
                    Interfaz.salida(
                        f"Has comprado {self.cantidad} tarritos de sacol. Ahora tienes {len(self.jugador.mochila.pociones)} tarritos de sacol y {self.jugador.monedas} pesos colombianos.")
                else:
                    raise NoSuficientesPesosError()
        except CantidadInvalidaError as e:
            Interfaz.salida(e)
        except NoSuficientesPesosError as e:
            Interfaz.salida(e)