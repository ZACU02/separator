import tkinter as tk
from tkinter import messagebox
#En Python, un separador se utiliza para dividir elementos en una cadena de texto, 
#lista u otra estructura de datos. El separador puede ser cualquier carácter
#cadena de caracteres que desees utilizar para dividir los elementos.
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Separator Horizontal entre Botones y Messagebox")


def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "has echo clik al boton." )

boton1 = tk.Button(ventana, text="Botón 1", command=mostrar_mensaje)
boton1.pack(pady=10)




boton4 = tk.Button(ventana, text="opccion", command=mostrar_mensaje, bg="blue", fg="white")
boton4.pack(padx=20, pady=20)

# Agregar un separator horizontal
separator = tk.Frame(height=2, bd=50, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=2, pady=2)


boton2 = tk.Button(ventana, text="Botón 2", command=mostrar_mensaje)
boton2.pack(pady=10)

boton3 = tk.Button(ventana, text="Botón 3", command=mostrar_mensaje)
boton3.pack(pady=10)

# Función para cerrar la ventana
def cerrar_ventana():
    ventana.destroy()

# Agregar un botón para cerrar la ventana
boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
