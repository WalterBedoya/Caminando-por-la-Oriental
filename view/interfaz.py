from .ui import UI


class Interfaz:
    ui = UI()

    @staticmethod
    def salida(*valores):
        # print(*valores)
        msg = ""
        for text in valores:
            msg += str(text) + " "

        Interfaz.ui.print(msg)

    @staticmethod
    def entrada(mensaje):
        return Interfaz.ui.input(mensaje)
        # return input(mensaje)
