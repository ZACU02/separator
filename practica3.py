import tkinter as tk
from tkinter import messagebox

def mostrar_aceptar():
    messagebox.showinfo("Mensaje", "¡Hiciste clic en el Primer Botón!")

def mostrar_negar():
    messagebox.showinfo("Mensaje", "¡Hiciste clic en el Segundo Botón!")

ventana = tk.Tk()
ventana.title("Separator Vertical en tkinter entre Dos Botones con MessageBox")

# Crear un marco para contener los widgets
marco = tk.Frame(ventana)
marco.pack(padx=50, pady=50)

# Agregar el primer botón
boton1 = tk.Button(marco, text="acerpar", command=mostrar_aceptar)
boton1.grid(row=0, column=0, padx=20, pady=20)

# Agregar un separador vertical
#separator = tk.Frame(marco, width=3, bd=1, relief=tk.SUNKEN): En esta línea, se está creando un objeto de tipo Frame (marco) en la ventana de la interfaz gráfica llamada marco. El marco tiene un ancho de 3 unidades, un borde de 1 píxel (bd=1) y tiene un estilo de relieve hundido (relief=tk.SUNKEN).
#En esta línea, se está creando un objeto de tipo Frame (marco) en la ventana
#de la interfaz gráfica llamada marco. El marco tiene un ancho de 3 unidades,
#un borde de 1 píxel (bd=1) y tiene un estilo de relieve hundido (relief=tk.SUNKEN). 

separator.grid(row=0, column=1, padx=1, pady=1, sticky="ns")
separator = tk.Frame(marco, width=3, bd=1, relief=tk.SUNKEN)
separator.grid(row=0, column=1, padx=1, pady=1, sticky="ns")



# Agregar el segundo botón
boton2 = tk.Button(marco, text="negar", command=mostrar_negar)
boton2.grid(row=0, column=2, padx=10, pady=10)

ventana.mainloop()