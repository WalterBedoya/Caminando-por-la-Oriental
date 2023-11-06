class InsultosInsuficientesError(Exception):
    def __init__(self, message="No tienes insultos suficientes. El combate continúa."):
        self.message = message
        super().__init__(self.message)