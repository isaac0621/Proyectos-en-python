import tkinter as tk
from tkinter import messagebox

class GestorTareas:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Tareas")

        # Lista para almacenar las tareas
        self.tareas = []

        # Campo de entrada para nuevas tareas
        self.nueva_tarea = tk.Entry(master, width=40)
        self.nueva_tarea.grid(row=0, column=0, padx=5, pady=5)

        # Botón para añadir tarea
        self.boton_anadir = tk.Button(master, text="Añadir Tarea", command=self.anadir_tarea)
        self.boton_anadir.grid(row=0, column=1, padx=5, pady=5)

        # Listbox para mostrar las tareas
        self.lista_tareas = tk.Listbox(master, width=50)
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Botón para completar tarea
        self.boton_completar = tk.Button(master, text="Completar Tarea", command=self.completar_tarea)
        self.boton_completar.grid(row=2, column=0, padx=5, pady=5)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=5, pady=5)

    def anadir_tarea(self):
        tarea = self.nueva_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)
            self.nueva_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def completar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(indice)
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, f"✓ {tarea}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para completar.")

    def eliminar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(indice)
            del self.tareas[indice]
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    gestor_tareas = GestorTareas(root)
    root.mainloop()
