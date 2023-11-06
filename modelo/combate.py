from queue import Empty
import random
from modelo.jugador import Player
from modelo.enemigo import Enemigo
from modelo.No_insultos_suficientes import InsultosInsuficientesError
from view.interfaz import Interfaz


class Combate:

    def __init__(self, jugador: Player, enemigo: Enemigo):
        self.jugador_pelea = jugador
        self.enemigo = enemigo
        self.eleccion = 0

    def comparar_si_jugador_esta_vivo(self)->bool:
        return self.jugador_pelea.estar_vivo()      
        

    def comparar_si_enemigo_esta_vivo(self):
        return self.enemigo.estar_vivo()     
    """
    class InsultoInsuficienteError(Exception):
        def __str__(self):
            return "No tienes insultos restantes. El combate continua."




    try:
        combate.insultar()
        Interfaz.salida("Insulto exitoso")
        Interfaz.salida("ROLO Hp")  
    except InsultosInsuficientesError as err:
        Interfaz.salida(err)


    """
    def insultar(self, combate: 'Combate'):
        if self.jugador_pelea.insultos_restantes > 0:
            self.jugador_pelea.insultos_restantes -= 1
            Interfaz.salida("Insulto exitoso")
            Interfaz.salida("ÑERO CATR*********A")
            if combate.jugador_pelea.victorias == 0:
                self.enemigo.nivel -= 0.9
            else:
                self.enemigo.nivel -= (0.9 * combate.jugador_pelea.victorias)
            if self.enemigo.nivel < 0:
                self.enemigo.nivel = 0
        else:
            raise InsultosInsuficientesError()

    

    def atacar(self, eleccion):
        # dependiendo de la raza los ataques tienen multiplicadores diferentes

        self.eleccion = eleccion
        if eleccion == "1":
            Interfaz.salida("Se navajeara rapidamente")
            daño = random.randint(5, 15) * self.jugador_pelea.multiplicador_basico
            self.enemigo.vida -= daño


            if self.enemigo.vida < 0:
                self.enemigo.vida = 0

            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito ha recibido", daño, "de daño")
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito tiene", self.enemigo.vida, "de vida")
            daño_enemigo = self.enemigo.atacar()
            self.jugador_pelea.vida -= daño_enemigo

            if self.jugador_pelea.vida < 0:
                self.jugador_pelea.vida = 0
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito te ha hecho", daño_enemigo, "de daño")
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("Tu tienes", self.jugador_pelea.vida, "de vida")
            Interfaz.salida("------------------------------------------------")
        elif eleccion == "2":
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("Se navajeara bien aspero")
            daño = random.randint(5, 15) * self.jugador_pelea.multiplicador_poder
            self.enemigo.vida -= daño

            if self.enemigo.vida < 0:
                self.enemigo.vida = 0

            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito ha recibido", daño, "de daño")
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito tiene", self.enemigo.vida, "de vida")
            daño_enemigo = self.enemigo.atacar()
            self.jugador_pelea.vida -= daño_enemigo

            if self.jugador_pelea.vida < 0:
                self.jugador_pelea.vida = 0
            
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito te ha hecho", daño_enemigo, "de daño")
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("Tu tienes", self.jugador_pelea.vida, "de vida")
        else:
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("Eleccion no valida, se atacara con el ataque basico")
            daño = random.randint(5, 15) * self.jugador_pelea.multiplicador_basico
            self.enemigo.vida -= daño

            if self.enemigo.vida < 0:    
                self.enemigo.vida = 0
            
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito ha recibido", daño, "de daño")
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito tiene", self.enemigo.vida, "de vida")
            daño_enemigo = self.enemigo.atacar()
            self.jugador_pelea.vida -= daño_enemigo

            if self.jugador_pelea.vida < 0:
                self.jugador_pelea.vida = 0

            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("El ñerito te ha hecho", daño_enemigo, "de daño")
            Interfaz.salida("------------------------------------------------")
            Interfaz.salida("Tu tienes", self.jugador_pelea.vida, "de vida")