import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class PrimeraVentana:
    def __init__(self, ventana):
        self.ventana_1 = ventana
        self.ventana_1.title('Hotel Luna')
        self.ventana_1.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.ventana_1.geometry('600x750')

        # Creacion de Frame Contenedor
        self.frame = Frame(self.ventana_1, background='white')
        self.frame.pack(fill=BOTH, expand=True)

        self.crear_imagen()
        self.crear_label_bienvenida()
        self.crear_boton()

    # Crear Imagen
    def crear_imagen(self):
        img = Image.open("Hotel_Luna/Imagenes/Imagen de WhatsApp 2024-04-23 a las 20.21.28_83c25263.jpg") 
        img = img.resize((400, 400))  
        imagen = ImageTk.PhotoImage(img)
        self.label = Label(self.frame, image=imagen)
        self.label.image = imagen 
        self.label.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    # Crear mensaje Bienvenida
    def crear_label_bienvenida(self):
        self.label_bienvenido = Label(self.frame, text='Bienvenido al Hotel Luna', font=('Arial', 18), bg='white')
        self.label_bienvenido.place(relx=0.5, rely=0.75, anchor=CENTER)
    
    # Crear boton
    def crear_boton(self):
        self.boton = tk.Button(self.frame, text='Ingresar', font= ('Arial',15), command=self.abrir_segunda_ventana)  
        self.boton.config(width=10, height=1)
        self.boton.place(relx=0.5, rely=0.9, anchor=CENTER)

    def abrir_segunda_ventana(self):
        ventana_segunda = SegundaVentana(self.ventana_1)

class SegundaVentana():
    def __init__(self, master):
        self.master = master
        self.ventana_2 = Toplevel(master)
        self.ventana_2.title('Hotel Luna')
        self.ventana_2.iconbitmap('Hotel_Luna/Imagenes/Icono/R.ico')
        self.ventana_2.geometry("800x750")

        self.frame = Frame(self.ventana_2, bg='white')
        self.frame.pack(fill=BOTH, expand=True)

        self.crear_widgets()

    def crear_widgets(self):
        # Añadimos el titulo de la ventana
        self.titulo_label = tk.Label(self.frame, text="         Reserva de habitación           ", font=('Arial', 12), bg='white')
        self.titulo_label.pack(pady=20)

        # Añadimos la imagen (Logo)
        self.img = Image.open("Hotel_Luna/Imagenes/Imagen de WhatsApp 2024-04-23 a las 20.21.28_83c25263.jpg")
        self.img = self.img.resize((300, 300))
        self.logo = ImageTk.PhotoImage(self.img)
        self.logo_label = Label(self.frame, image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.place(relx=0.75, rely=0.5, anchor=CENTER)

        # Agregamos los textos con sus casillas para ingresar la informaci0n
        self.nombre_label = Label(self.frame, text="Nombre: ", font=('Arial', 12), bg='white')
        self.nombre_label.place(x=10, y=100)
        self.nombre_entry = Entry(self.frame, fg="black")
        self.nombre_entry.place(x=130, y=100)

        self.rut_label = Label(self.frame, text="Rut: ", font=('Arial', 12), bg='white')
        self.rut_label.place(x=10, y=200)
        self.rut_entry = Entry(self.frame, fg="black")
        self.rut_entry.place(x=130, y=200)

        self.dias_label = Label(self.frame, text="día/s: ", font=('Arial', 12), bg='white')
        self.dias_label.place(x=10, y=300)

        self.dias_var = StringVar(self.ventana_2)
        self.dias_var.set("1 día")
        self.dias_opciones = ["1 día", "2 días", "3 días", "4 días"]
        self.dias_option_menu = OptionMenu(self.frame, self.dias_var, *self.dias_opciones)
        self.dias_option_menu.place(x=100, y=300)

        self.tipo_habitacion_label = Label(self.frame, text="Tipo de Habitación: ", font=('Arial', 12), bg='white')
        self.tipo_habitacion_label.place(x=10, y=400)

        self.tipo_habitacion_var = StringVar(self.ventana_2)
        self.tipo_habitacion_var.set("Habitación Normal")
        self.tipo_habitacion_opciones = ["Habitación Normal", "Habitación Mediana", "Habitación Grande", "Suite"]
        self.tipo_habitacion_option_menu = OptionMenu(self.frame, self.tipo_habitacion_var, *self.tipo_habitacion_opciones)
        self.tipo_habitacion_option_menu.place(x=190, y=400)

        # Agregamos el boton 'Reservar' para guardar toda la informaci0n elegida
        self.reservar_button = Button(self.frame, text="Reservar", font=('Arial', 10), command=self.reservar, state=DISABLED)
        self.reservar_button.place(x=120, y=550)

        # Creamos una funcion que verifique si los campos de texto estan vacios
        def verificar_campos():
            if self.nombre_entry.get()!= "" and self.rut_entry.get()!= "":
                self.reservar_button.config(state=NORMAL)
            else:
                self.reservar_button.config(state=DISABLED)

        # Asignamos la funcion 'verificar_campos' a los campos de texto
        self.nombre_entry.bind("<KeyRelease>", lambda event: verificar_campos())
        self.rut_entry.bind("<KeyRelease>", lambda event: verificar_campos())

    def reservar(self):
        messagebox.showinfo("Reserva", "Reserva exitosa")
        self.ventana_2.destroy()

        label_segunda_ventana = Label(self.ventana_2)
        label_segunda_ventana.pack()

if __name__ == '__main__':
    ventana = Tk()
    app = PrimeraVentana(ventana)
    ventana.mainloop()