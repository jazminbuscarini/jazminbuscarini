import tkinter as tk
def main():
    global ventana
    ventana = tk.Tk()
    ventana.title("Ingresa tu nombre")
    ventana.geometry("300x200")

    boton = tk.Button(ventana,text="Saludar", command=funcion)
    boton.pack(pady=5)
    
    etiqueta =tk.Label(ventana, text="¡Hola,[nombre], te saluda Jazmin", font=("Arial", 16))
    etiqueta.pack()

    ventana.mainloop()
if __name__=="__main__":
    main()
