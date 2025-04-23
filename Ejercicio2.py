import tkinter as tk


    # Crar la ventana principal
ventana=tk.Tk()
ventana.title("Ejercicio2")
ventana.geometry("700x700")
ventana.configure(bg="lightblue")
    
    # Crear la etiqueta    
etiqueta = tk.Label(ventana, text="Ejercicio 2", font=("Arial", 16))
etiqueta.pack()  # Coloca la etiqueta en la ventana

    # Ejecutar la ventana
ventana.mainloop()
