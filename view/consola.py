import sys
from modelo.Oro_ERROR import NoSuficientesPesosError
from modelo.cantidadinvalidaderror import CantidadInvalidaError
from modelo.jugador import Player
from modelo.enemigo import Enemigo
from modelo.tienda import Store
from modelo.combate import Combate
from modelo.entrenamiento import Entrenar
from modelo.tabla_de_posiciones import Tabla_de_posiciones
from modelo.no_calle_suficienteerror import NoCalleSuficienteError
from modelo.No_insultos_suficientes import InsultosInsuficientesError
from view.interfaz import Interfaz
from modelo.no_pociones_suficiente_error import NoSacolError

class UIConsola:

    NAVAJAZO_VELOZ = "1"
    NAVAJAZO_ASPERO = "2"
    INSULTAR = "3"
    COSTAL = "4"
    HUIR = "5"


        
    def elegir_raza(self, jugador: Player):
        self.mostrar_menu_raza()
        eleccion = Interfaz.entrada("Ingrese su eleccion: ")
        while True:
            if eleccion == "1":
                jugador.razaMago()
                break

            elif eleccion == "2":
                jugador.razaLuchador()
                break
            else:
                Interfaz.salida("Seleccion no válida. Se usara la raza por defecto.")

    def nombrar_personaje(self):
        nombre = Interfaz.entrada("Ingrese el nombre de su personaje: ")
        return Player(nombre)
    
    def ir_a_tienda(self, jugador: Player):
        self.mostrar_menu_tienda()
        Cuantas_pociones_desea_comprar = int(Interfaz.entrada("Ingrese su eleccion: "))
        
        try:
            if Cuantas_pociones_desea_comprar!=6 and Cuantas_pociones_desea_comprar != 5 and Cuantas_pociones_desea_comprar != 4 \
                    and Cuantas_pociones_desea_comprar != 3 and Cuantas_pociones_desea_comprar != 2 \
                    and Cuantas_pociones_desea_comprar != 1:
                raise CantidadInvalidaError("Cantidad no válida. Debes elegir entre 1 y 5 tarritos de sacol.")
            if Cuantas_pociones_desea_comprar==6:
                Interfaz.salida("No se comprara sacol.")
            else:
                tienda1 = Store(Cuantas_pociones_desea_comprar, jugador)
                tienda1.comprar_objeto()

            
        except NoSuficientesPesosError as e:
            Interfaz.salida(e)
        
        except CantidadInvalidaError as e:
            Interfaz.salida(e)

    def crear_combate(self, jugador: Player, tabla:Tabla_de_posiciones):
        Interfaz.salida("Uy! ibas caminando por la oriental y te cuñó un ñero en la calle")
        enemigo = Enemigo(jugador.victorias)
        combate1 = Combate(jugador, enemigo)
        Interfaz.salida(f"{enemigo.nombre} tiene {enemigo.vida} de vida y lleva {enemigo.nivel} años robando")
        return self.ir_a_pelear(combate1, tabla)

    def modificar_tabla_de_posiciones(self, tabla: Tabla_de_posiciones, jugador: Player):
        tabla.agregar_jugador(jugador)
        tabla.guardar_tabla()

    def ir_a_pelear(self, combate: Combate, tabla: Tabla_de_posiciones):
        Wcombate = True
        while Wcombate:
            self.mostrar_menu_combate()
            eleccion = Interfaz.entrada("Ingrese su eleccion: ")
            if eleccion == UIConsola.NAVAJAZO_VELOZ:
                combate.atacar(eleccion)
                if self.verificar_si_enemigo_gano(combate):
                    self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                    self.perder()
                    return False
                if self.verificar_si_jugador_gano(combate):
                    self.gano_combate(combate)
                    return True
            elif eleccion == UIConsola.NAVAJAZO_ASPERO:
                combate.atacar(eleccion)
                if self.verificar_si_enemigo_gano(combate):
                    self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                    self.perder()
                    return False
                if self.verificar_si_jugador_gano(combate):
                    self.gano_combate(combate)
                    return True
            elif eleccion == UIConsola.INSULTAR:
                try:
                    combate.insultar(combate)
                except InsultosInsuficientesError as e:
                    Interfaz.salida(e)
                    continue  # Volver al menú de combate en lugar de salir
                if self.verificar_si_enemigo_gano(combate):
                    self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                    self.perder()
                    return False
                if self.verificar_si_jugador_gano(combate):
                    self.gano_combate(combate)
                    return True
            elif eleccion == UIConsola.COSTAL:
                try:
                    combate.jugador_pelea.curarVida()
                except NoSacolError as e:
                    Interfaz.salida(e)
                    continue  # Volver al menú de combate en lugar de salir
                if self.verificar_si_enemigo_gano(combate):
                    self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                    self.perder()
                    return False
                if self.verificar_si_jugador_gano(combate):
                    self.gano_combate(combate)
                    return True
            elif eleccion == UIConsola.HUIR:
                self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                self.huir()  
                return False
            else:
                print("Seleccion no válida. Se usará ataque básico.")
                combate.atacar(UIConsola.NAVAJAZO_VELOZ)
                if self.verificar_si_enemigo_gano(combate):
                    self.modificar_tabla_de_posiciones(tabla, combate.jugador_pelea)
                    self.perder()
                    return True

    def ir_a_entrenar(self, jugador: Player, eleccion: int):
        try:
            entrenamiento = Entrenar(jugador)
            if eleccion == "1":
                if jugador.xp < 100:
                    raise NoCalleSuficienteError()
                else:
                    entrenamiento.aumentar_multiplicador_basico()
            elif eleccion == "2":
                if jugador.xp < 100:
                    raise NoCalleSuficienteError()
                else:
                    entrenamiento.aumentar_multiplicador_poder()
            elif eleccion == "3":
                Interfaz.salida("No se entrenará.")
            else:
                Interfaz.salida("Selección no válida. No se entrenará.")
        except NoCalleSuficienteError as e:
            Interfaz.salida(e)

    def ver_mochila(self, jugador: Player):
        Interfaz.salida("Tienes", len(jugador.mochila.pociones), "tarritos de sacol")
        Interfaz.salida("Tienes", jugador.insultos_restantes, "insultos restantes")
        Interfaz.salida("Tienes", jugador.monedas, " pesos colombianos")
        Interfaz.salida("Tienes", jugador.xp, "de experiencia")


    def verificar_si_enemigo_gano(self, combate: Combate):
        return not combate.jugador_pelea.estar_vivo()
    
    def verificar_si_jugador_gano(self, combate: Combate):
        return not combate.enemigo.estar_vivo()



       

    def perder(self):
        Interfaz.salida("Perdiste la pelea con el ñerito")
        # guardar datos

    def huir(self):
        Interfaz.salida("------------------------------------------------")
        Interfaz.salida("Reeee locaa, te fuiste corriendo... pero")
        Interfaz.salida("------------------------------------------------")
        Interfaz.salida("No lograste huir, te hicieron un roto y no sabias cocer")
        Interfaz.salida("------------------------------------------------")
        Interfaz.salida("Perdiste la pelea con el ñerito, moriste")

    def gano_combate(self, combate:Combate):
        Interfaz.salida("------------------------------------------------")
        Interfaz.salida("Le ganaste al ñerito pa")
        combate.jugador_pelea.jugador_gano()
        Interfaz.salida("------------------------------------------------")
        Interfaz.salida("Le has ganado a ", combate.jugador_pelea.victorias, " ñeritos")
        Interfaz.salida("------------------------------------------------")
        Interfaz.salida("tienes", combate.jugador_pelea.xp, " de experiencia")
        Interfaz.salida("------------------------------------------------")
        Interfaz.salida("tienes", combate.jugador_pelea.monedas, " pesos colombianos")
        Interfaz.salida("------------------------------------------------")
        
       

    def __init__(self):

        self.opciones_menu_principal = {
            "1": self.ir_a_tienda,
            "2": self.crear_combate,
            "3": self.ir_a_entrenar,
            "4": self.ver_mochila,
            #"5": tabla.ver_tabla_de_posiciones,
            "6": self.salir
        }

    @staticmethod
    def salir():
        Interfaz.salida("\nGRACIAS POR JUGAR A ''CAMINANDO POR LA ORIENTAL''")
        Interfaz.salida("")
        sys.exit(0)
        

    @staticmethod
    def mostrar_menu_partidas():
        titulo = "¿Quieres caminar a las 9pm por la oriental?"
        Interfaz.salida(f"\n{titulo:_^30}")
        Interfaz.salida("1. Si")
        Interfaz.salida("2. No")
        Interfaz.salida("3. No, solo quiero ver la tabla de posiciones")
        Interfaz.salida("")

    @staticmethod
    def mostrar_menu_entrenamiento():
        titulo = "¿Que habilidad deseas aumentar?"
        Interfaz.salida(f"\n{titulo:_^30}")
        Interfaz.salida("Cada aumento de habilidad cuesta 100 de experiencia")
        Interfaz.salida("Puedes ganar experiencia bajandote a ñeritos")
        Interfaz.salida("")
        Interfaz.salida("1. Navajazo rapido pero suavezongo")
        Interfaz.salida("2. Navajazo lento pero aspero")
        Interfaz.salida("3. No quiero entrenar todavia pa")
        Interfaz.salida("")

    @staticmethod
    def mostrar_menu():
        titulo = "¿Que deseas hacer?"
        Interfaz.salida(f"\n{titulo:_^30}")
        Interfaz.salida("1. Ir a la ferreteria")
        Interfaz.salida("2. Arriesgarte a caminar y posiblemente pelear con un ñerito")
        Interfaz.salida("3. Ir a entrenar con esa lata")
        Interfaz.salida("4. Ver el costal")
        Interfaz.salida("5. Ver la tabla de posiciones")
        Interfaz.salida("6. Salir")
        Interfaz.salida("")
        Interfaz.salida(f"{'_':_^30}")

    @staticmethod
    def mostrar_menu_combate():
        titulo = "¿Que deseas hacer?"
        Interfaz.salida(f"\n{titulo:_^30}")
        Interfaz.salida("")
        Interfaz.salida("1. Navajazo rapido")
        Interfaz.salida("2. Navajazo aspero")
        Interfaz.salida("3. Insultar al enemigo (bajara su multiplicador de daño en 0.9 [ acumulable con limite de 0 ])")
        Interfaz.salida("4. Oler sacol (recuperaras 50 de vida)")
        Interfaz.salida("5. Huir")
        Interfaz.salida("")
        Interfaz.salida(f"{'_':_^30}")

    @staticmethod
    def mostrar_menu_tienda():
        titulo = "¿cuantos tarritos de sacol quieres comprar?"
        Interfaz.salida(f"\n{titulo:_^30}")
        Interfaz.salida("")
        Interfaz.salida("Cada tarrito de sacol cuesta 70 monedas")
        Interfaz.salida("")
        Interfaz.salida("1. Un tarro de sacol")
        Interfaz.salida("2. Dos tarros de sacol")
        Interfaz.salida("3. Tres tarros de sacol")
        Interfaz.salida("4. Cuatro tarros de sacol")
        Interfaz.salida("5. Cinco tarros de sacol")
        Interfaz.salida("6. No quiero sacol todavia pa")
        Interfaz.salida("")
        Interfaz.salida(f"{'_':_^30}")

    @staticmethod
    def mostrar_menu_raza():
        titulo = "¡Hola, que habilidad deseas elegir!"
        Interfaz.salida(f"\n{titulo:_^30}")
        Interfaz.salida("1. Navajear bien rapido pero mas suavezongo")
        Interfaz.salida("recibiras los siguientes atributos, 250 de vida, 70 pesos colombianos, 1 de multiplicador de velocidad y 4 de multiplicador de asperosidad")
        Interfaz.salida("")
        Interfaz.salida("2. Navajear bien aspero pero mas lento")
        Interfaz.salida("recibiras los siguientes atributos, 500 de vida, 210 pesos colombianos, 4 de multiplicador de velocidad y 1 de multiplicador de asperosidad")
        Interfaz.salida("")
        Interfaz.salida(f"{'_':_^30}")

    """def borrar_posicion_tabla(self, tabla: Tabla_de_posiciones):
        tabla.listado.pop(3)
        Interfaz.salida("hecho")"""

    def ejecutar_app(self):
        juego = True
        while juego:

            partida = True
            eleccion = True
            self.mostrar_menu_partidas()
            eleccion_usuario =Interfaz.entrada("")
            tabla_de_posiciones1= Tabla_de_posiciones()
            tabla_de_posiciones1.cargar_tabla()
            if eleccion_usuario == "1":
                while partida:
                    Jugador1 = self.nombrar_personaje()
                    self.elegir_raza(Jugador1)
                    while eleccion:
                        self.mostrar_menu()
                        opcion = Interfaz.entrada("Seleccione una opción: ")
                        if opcion == "1":
                            self.ir_a_tienda(Jugador1)
                        elif opcion == "2":
                            jugador_jugo=self.crear_combate(Jugador1, tabla_de_posiciones1)
                            if not jugador_jugo:
                                partida=False
                                eleccion=False
                        elif opcion == "3":
                            self.mostrar_menu_entrenamiento()
                            self.ir_a_entrenar(Jugador1, Interfaz.entrada("Ingrese su eleccion: "))
                        elif opcion == "4":
                            self.ver_mochila(Jugador1)
                        elif opcion == "5":
                            tabla_de_posiciones1.ver_tabla_de_posiciones()
                        elif opcion == "6":
                            self.modificar_tabla_de_posiciones(tabla_de_posiciones1, Jugador1)
                            partida = False
                            eleccion = False
                        else:
                            Interfaz.salida(f"{opcion} no es una opción válida")

            elif eleccion_usuario == "2":
                tabla_de_posiciones1.guardar_tabla()
                self.salir()

            elif eleccion_usuario=="3":
                tabla_de_posiciones1.ver_tabla_de_posiciones()
            
            
            
            else:
                Interfaz.salida("Opcion no valida")

    