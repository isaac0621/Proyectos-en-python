import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Gráfica")

        # Pantalla de resultados
        self.pantalla = tk.Entry(master, width=30, justify="right")
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        # Crear y posicionar botones
        row = 1
        col = 0
        for boton in botones:
            comando = lambda x=boton: self.click(x)
            tk.Button(master, text=boton, width=7, command=comando).grid(row=row, column=col, padx=2, pady=2)
            col += 1

            if col > 3:
                col = 0
                row += 1

        # Botón de igual
        tk.Button(master, text="=", width=7, command=self.calcular).grid(row=row, column=col, padx=2, pady=2)

    def click(self, key):
        if key == 'C':
            self.pantalla.delete(0, tk.END)
        else:
            self.pantalla.insert(tk.END, key)

    def calcular(self):
        try:
            resultado = eval(self.pantalla.get())
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, str(resultado))
        except:
            messagebox.showerror("Error", "Expresión inválida")
            self.pantalla.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()
