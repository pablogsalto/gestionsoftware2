from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Gui():

    def __init__(self):
        #-----------------Pantalla inicial
        
        self.ventana = Tk()
        self.ventana.title("Consultorio")
        self.ventana.geometry("800x640")
        self.ventana.resizable(0, 0)
        self.ventana.iconbitmap("dentist.ico")

        notebook = ttk.Notebook(self.ventana)
        notebook.pack(fill="both", expand="yes")
       
        #-----------------Pestaña agregar turno----------
        
        p_agregar = ttk.Frame(notebook)
        notebook.add(p_agregar, text="Agregar turno")
        
        #Nombre
        self.entry_nombre = Entry(p_agregar, width=75)
        self.entry_nombre.place(x=190, y=125)        
        label_nombre = Label(p_agregar, text="Nombre:").place(x=120, y=125)
        
        #Apellido
        self.entry_apellido = Entry(p_agregar, width=75)
        self.entry_apellido.place(x=190, y=155)        
        label_apellido = Label(p_agregar, text="Apellido:").place(x=120, y=155)
        
        #DNI
        self.entry_dni = Entry(p_agregar, width=75)
        self.entry_dni.place(x=190, y=185)        
        label_dni = Label(p_agregar, text="DNI:").place(x=120, y=185)
        
        #Telefono
        self.entry_tel = Entry(p_agregar, width=75)
        self.entry_tel.place(x=190, y=215)        
        label_tel = Label(p_agregar, text="Telefono:").place(x=120, y=215)
        
        #E-mail
        self.entry_mail = Entry(p_agregar, width=75)
        self.entry_mail.place(x=190, y=245)        
        label_mail = Label(p_agregar, text="E-mail:").place(x=120, y=245)
        
        #Fecha
        self.entry_time = Entry(p_agregar, width=75)
        self.entry_time.place(x=190, y=275)        
        label_time = Label(p_agregar, text="Fecha:").place(x=120, y=275)
        label_help = Label(p_agregar, text="Ingrese la fecha y hora del turno en el siguiente formato: AAAA/MM/DD HH:MM:SS", fg="gray")
        label_help.place(x=190, y=295)
        
        #Descripción
        self.entry_desc = Entry(p_agregar, width=75)
        self.entry_desc.place(x=190, y=325)        
        label_desc = Label(p_agregar, text="Descripción:").place(x=120, y=325)

        #self.entry_etiquetas = Entry(p_agregar, width=75)
        #self.entry_etiquetas.place(x=190, y=355)        
        #label_etiquetas = Label(p_agregar, text="Etiquetas:").place(x=120, y=355)
        #label_help2 = Label(p_agregar, text="Opcional", fg="gray")
        #label_help2.place(x=190, y=375)

        self.image9 = PhotoImage(file="checked.png")              
        boton_confirmar = Button(p_agregar, text="  Confirmar  ", image=self.image9, compound="left",
                                 command=self.confirmar_turno, cursor="hand2")
        boton_confirmar.place(x=350, y=510)

        #-----------------Pestaña turnos-----------------

        p_turnos = ttk.Frame(notebook)
        notebook.add(p_turnos, text="Turnos")
        
        #Modificar turno
        self.image1 = PhotoImage(file="edit.png")
        boton_modificar = Button(p_turnos, text="  Modificar turno  ", command=self.modificar_turno,
                                 image=self.image1, compound="left", cursor="hand2")
        boton_modificar.place(x=270, y=530)
        
        #Eliminar turno
        self.image2 = PhotoImage(file="clear.png")
        boton_eliminar = Button(p_turnos, text="  Eliminar turno  ", command=self.eliminar_turno,
                                image=self.image2, compound="left", cursor="hand2")
        boton_eliminar.place(x=420, y=530)

                   #---------treeview---------

        self.tv_turnos = ttk.Treeview(p_turnos)
        self.tv_turnos = ttk.Treeview(p_turnos, height=20, columns=("Descripción", "Fecha y hora", "Estado"))
        self.tv_turnos.heading("#0", text="Paciente")
        self.tv_turnos.heading("#1", text="Descripción")        
        self.tv_turnos.heading("#2", text="Fecha y hora")
        self.tv_turnos.heading("#3", text="Estado")
        self.tv_turnos.column("#3", minwidth=0, width="80")
        self.tv_turnos.place(x=55, y=60)

        #-----------------Pestaña informes---------------
        
        p_informes = ttk.Frame(notebook)
        notebook.add(p_informes, text="Informes")

        label_help3=Label(p_informes, text="Seleccione el tipo de informe").place(x=55, y=20)
        self.sel=IntVar() 
        
        #Turnos pendientes
        info_D=Radiobutton(p_informes, text="Turnos pendientes del dia", value=1,
                           variable=self.sel, command=self.tipo_informe, cursor="hand2")
        info_D.place(x=55, y=40)
        
        #Consultas del mes
        info_M=Radiobutton(p_informes, text="Consultas finalizadas del mes", value=2,
                           variable=self.sel, command=self.tipo_informe, cursor="hand2")
        info_M.place(x=55, y=60)

        #Pacientes pendientes
        info_P=Radiobutton(p_informes, text="Pacientes pendientes", value=3,
                           variable=self.sel, command=self.tipo_informe, cursor="hand2")
        info_P.place(x=55, y=80)

                   #---------treeview------------

        self.tv_informes = ttk.Treeview(p_informes)
        self.tv_informes = ttk.Treeview(p_informes, height=15, columns=("Descripción", "Fecha y hora", "Estado"))
        self.tv_informes.heading("#0", text="Paciente")
        self.tv_informes.heading("#1", text="Descripción")        
        self.tv_informes.heading("#2", text="Fecha y hora")
        self.tv_informes.heading("#3", text="Estado")
        self.tv_informes.column("#3", minwidth=0, width="80")
        self.tv_informes.place(x=55, y=125)

        #-----------------Ventana------------------------

        self.image4 = PhotoImage(file="logout.png")
        boton_salir = Button(self.ventana, text="  Salir  ", cursor="hand2",
                           image=self.image4, compound="left", command=self.salir)
        boton_salir.place(x=370, y=595)        

        #-----------------Funciones------------------------
        
    def tipo_informe(self):
        s = self.sel.get()
        if s == 1:
            print ("seleccionaste el primero") #El print es para indicar si funciona
        elif s == 2:
            print ("seleccionaste el segundo")
        elif s == 3:
            print ("seleccionaste el tercero")
            
    def confirmar_turno(self):
        pass
                
    def eliminar_turno(self):
        pass

    def modificar_turno(self):
        pass
    
    def salir(self):        
        rta = messagebox.askyesno(message="¿Desea salir? Se perderán los cambios no guardados",
                                  title="Atención")
        if rta == True:            
            self.ventana.destroy()
            exit()

if __name__ == "__main__":
    g = Gui()
    g.ventana.mainloop()
