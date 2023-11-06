import tkinter as tk


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.entrada1 = tk.Entry(self.root)
        self.boton1 = tk.Button(self.root, text="Ok", command=self.click_en_boton1)
        self.texto_resultante = tk.Text(self.root, height=30, width=160)
        self.root.title("Caminando Por La Oriental")

        self.texto_resultante.config(state=tk.DISABLED)
        self.texto_resultante.pack()
        self.entrada1.pack()
        self.boton1.pack()

        # Se crea un StringVar para manejar el input, como si estuviese vacío para luego reemplazarlo por los datos
        self.input_var = tk.StringVar()
        self.input_var.set("")  # Inicializamos con un string vacío

    def print(self, text):
        self.texto_resultante.config(state=tk.NORMAL)
        self.texto_resultante.insert(tk.END, str(text) + "\n")
        self.texto_resultante.config(state=tk.DISABLED)
        # El texto resultante se deja deshabilitado para evitar que escriban o sobreescriban en el texto principal o el cuadro de texto/diálogo

    def input(self, mensaje):
        self.print(mensaje)
        self.input_var.set("")
        self.entrada1.config(state=tk.NORMAL)
        self.entrada1.focus_set()
        # TODO este código siempre espera por un cambio en input_var
        self.entrada1.wait_variable(self.input_var)
        self.entrada1.config(state=tk.DISABLED)

        return self.input_var.get()

    def click_en_boton1(self):
        input_text1 = self.entrada1.get()
        self.input_var.set(input_text1)
        self.entrada1.delete(0, tk.END)