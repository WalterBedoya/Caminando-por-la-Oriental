class NoCalleSuficienteError(Exception):
    def __init__(self, message="No tienes suficiente EXP, Te falta calle pa"):
        self.message = message
        super().__init__(self.message)