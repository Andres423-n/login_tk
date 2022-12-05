#carlos andres marin

from cProfile import label
from tkinter import *
from tkinter import messagebox
import psycopg2

#############################################################
############# LOGIN ##########################################


def login():#creacion de ventana inicial
    ventana = Tk()
    ventana.title("LOGIN")
    ventana.geometry("400x400")
    verde ="#90EE90"#colores hexagesadecimales 
    rojo = "#FF4500"
    ventana.config(background=verde)
    ventana.resizable(0,0)#no deja cambiar el tamaño de las paginas

    password =StringVar()
    usuario = StringVar()

    
    def validacion_datos():

        #llamado de base de datos
        conexion= psycopg2.connect(
            database="Registros_login",
            user="postgres",
            password="12345678"
            )
        #utilizamos codigo SQL para llamar datos de la base de datos 
        cursor = conexion.cursor()#se utiliza .cursor para poder acceder a nuestra base de datos
        verif = "SELECT contraseña FROM registros WHERE email='"+usuario.get()+"' and contraseña='"+password.get()+"'"#select permite seleccionar un datos dandole una condicion
        cursor.execute(verif)# .execute ejecuta la variable que contiene la sentencia SQL
        #condiciones para que los entry no esten vacidos


        if usuario.get()=="" and password.get() == "" or usuario.get()=="" or password.get() == "":#condicional para saber si usuario y contraseña son correctos
            messagebox.showerror('ERROR',message='ingrese el correo y contraseña')#mensaje de error

        elif cursor.fetchall():
            messagebox.showinfo('Inicio de session',message='correo y contraseña correctos')
            ventana.destroy()#se destruye la ventana ya que el usuario y contraseña son validos en la base de datos
            inicio()#llamo la funcion inicio que es otra pagina del programa
        else:
            messagebox.showinfo('Inicio de session incorrecto',message='usuario y contraseña incorrectos')#mensaje de informacion
    
        conexion.close()    
    

    def Ventana_registro():#funcion de llamdo para  ventana para registro
        ventana.destroy()
        registro_date()
    def recup_contrasenia():#funcion de vllamado  para recuperar contraseña
        ventana.destroy()
        recuperar_password()

    imagen = PhotoImage(file="user_imagen.gif")#agrego una imagen
    Label(ventana,image=imagen,bg=verde).pack()

    Titulo = Label(ventana, text="Iniciar Sesión",bg=verde,font="Tahoma 20")
    Titulo.place(x=120,y=100)

    #usuario
    inicio_sesion = Label(ventana, text="Usuario",bg=verde,font="Tahoma 12")
    inicio_sesion.place(x=175,y=145)

    Entrada_sesion = Entry(ventana,bd=5,width=30,textvariable=usuario)
    Entrada_sesion.place(x=110,y=170)

    #contaseña
    contrasenia_inicio = Label(ventana,text="contraseña",bg=verde,font="Tahoma 12")
    contrasenia_inicio.place(x=165,y=205)

    Entrada_contrasenia = Entry(ventana,show="*" ,bd=5,width=30,textvariable=password)
    Entrada_contrasenia.place(x=110, y=235)

    #Login
    login_inicio = Button(ventana, text="Login",command=validacion_datos)
    login_inicio.place(x=185,y=278)

    #recuperar contraseña
    recuperar_contr = Button(ventana,text="Recuperar Contraseña",bg=verde,bd=0,fg=rojo,command=recup_contrasenia)
    recuperar_contr.place(x=145,y=318)

    #registrarse
    Registrarse = Button(ventana,text="Registrarse",bg=verde,bd=0,fg=rojo,command=Ventana_registro)
    Registrarse.place(x=170,y=340)

    ventana.mainloop()


######################################################################################################
######################  REGISTRO  ###################################################


def registro_date():#funcion de la ventana de registro
    ventana_2 = Tk()
    ventana_2.title("Registro")
    ventana_2.geometry("350x400")
    verde ="#90EE90"
    rojo = "#FF0000"
    ventana_2.config(background=verde)
    ventana_2.resizable(0,0)


    Titulo= Label(ventana_2,text="Registro",font="Tahoma 20", bg= verde, bd=5)
    Titulo.pack()

    nombre = StringVar()#le doy tipo de datos a variables que almacenan los datos dados por el
    apellido=StringVar()
    correo_elect = StringVar()
    usuario=StringVar()
    contra = StringVar()
    confir_contr=StringVar()
    



    def confirmacion_cont():

        if contra.get()=="":
            messagebox.showerror('ERROR', message='No ingreso ninguna contraseña')

        elif confir_contr.get() != contra.get():
            messagebox.showerror('ERROR',message='las contraseñas no coinciden')
        else:
            conexion()
    #funcion para conectar pase de datos y realizar el registro
    def conexion():

        conexion= psycopg2.connect(

            database="Registros_login",
            user="postgres",
            password="12345678"
    )
        cursor = conexion.cursor()
        query = ''' INSERT INTO registros(nombre,apellidos,email,usuario,contraseña) VALUES (%s, %s, %s, %s,%s)'''#INSERT INTO es para añadir datos, %s receteo de String
        cursor.execute(query,(nombre.get(),apellido.get(),correo_elect.get(),usuario.get(),contra.get()))#ejecuto el query y los datos en orden de las columnas y se añade al receteo de String
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Registro",message="Se realizo el registro correctamente")
        ventana_2.destroy()
        login()#una vez se registra vuelve a la evntana login
        
    
    def volver():
        ventana_2.destroy()
        login()


    #nombres
    nombres = Label(ventana_2, text="Nombre:", font="Tahoma 11",bg=verde)
    nombres.place(x=120,y=50)
    entrada_nombre = Entry(ventana_2,bd=4,textvariable=nombre)
    entrada_nombre.place(x=120,y=70)

    #apellidos
    Apellidos= Label(ventana_2, text="Apellidos:" ,font="Tahoma 11", bg= verde)
    Apellidos.place(x=120, y=98)
    entrada_apellidos = Entry(ventana_2,bd=4,textvariable=apellido)
    entrada_apellidos.place(x=120, y=120)

    #correo electronico
    correo = Label(ventana_2, text="Correo:",font="Tahoma 11", bg= verde)
    correo.place(x=120,y=145)
    correo_entry = Entry(ventana_2,bd=4,textvariable=correo_elect)
    correo_entry.place(x=120,y=170)

    #Nombre Usuario
    nombre_usuario= Label(ventana_2, text="Nombre Usuario:" ,font="Tahoma 11", bg= verde)
    nombre_usuario.place(x=120,y=195)
    entrada_nom_usuario = Entry(ventana_2,bd=4,textvariable=usuario)
    entrada_nom_usuario.place(x=120,y=220)

    #contraseña
    contrasenia = Label(ventana_2, text="contraseña",font="Tahoma 11", bg= verde)
    contrasenia.place(x=120,y=245)
    entrada_contra= Entry(ventana_2,bd=4,textvariable=contra,show='*')
    entrada_contra.place(x=120,y=270)

    #confirmacion contrasenia

    contrasenia_confi = Label(ventana_2, text="confirmar contraseña:",font="Tahoma 11", bg= verde)
    contrasenia_confi.place(x=115,y=295)
    confirmacion_contra= Entry(ventana_2,bd=4,textvariable=confir_contr,show='*')
    confirmacion_contra.place(x=120,y=320)

    #boton registrar 

    registar = Button(ventana_2, text="Registrar", command=confirmacion_cont)
    registar.place(x=150, y=360)

    #volver
    volver = Button(ventana_2,text='Volver',bd=6,command=volver)
    volver.place(x=0,y=0)
    ventana_2.mainloop()


####################################################################################################
########################## RECUPERAR PASSWORD ####################################

def recuperar_password():
    verde ="#90EE90"
    rojo = "#FF0000"

    recuperar = Tk()
    recuperar.title("Recuperar contraseña")
    recuperar.geometry("300x200")
    recuperar.config(background=verde)
    recuperar.resizable(0,0)

    users = StringVar()
    def new_password():

        conexion= psycopg2.connect(
            database="Registros_login",
            user="postgres",
            password="12345678"
            )
    
        try:#try ejecuta el codigo y si no se ejecuta bien se va al except
            cursor = conexion.cursor()
            verif = "SELECT email FROM registros WHERE email='"+users.get()+"'"#SELECT seleciona un elemento de la base de datos
            cursor.execute(verif)
            date = cursor.fetchall()#fetchall toma el dato seleccionado de la base de datos
            for i in date:
                usuario=i[0]

            if usuario ==users.get():
                recuperar.destroy()
                actuali_pass()#llama una funcion para actualizar la contraseña

        except:#si el codigo del try no se ejecuta bien, dentra en la exepcion
            messagebox.showerror('ERROR',message='email no se encuentra registrado')

    def actuali_pass():

        verde ="#90EE90"
        rojo = "#FF0000"
        new_pass = Tk()
        new_pass.title('Nueva contraseña')
        new_pass.geometry('400x250')
        new_pass.config(background=verde)
        new_pass.resizable(0,0)
        new_contr = StringVar()
        confirm_contr = StringVar()

        def confirmacion():
            if new_contr.get()== confirm_contr.get():
                update()#si son igules llama otra funcion
            else:
                messagebox.showerror('Error',message='contraseñas no coinciden')

        def update():
            conexion= psycopg2.connect(
                database="Registros_login",
                user="postgres",
                password="12345678"
            )

            try: 
                cursor = conexion.cursor()
                upda = 'UPDATE registros SET contraseña =%s WHERE email=%s'#update es el metodo para actualizar datos en la base de datos
                date=(new_contr.get(),users.get())
                cursor.execute(upda,date)
                conexion.commit()#guarda los cambios de la base de datos
                messagebox.showinfo('actualizacion', message='Cambio de contraseña correcto')
                new_pass.destroy()
                login()
            
            except:
                messagebox.showerror('ERROR',message='no se actualizo contraseña')
        


        #label y entry para nueva contraseña
        nueva_pass = Label(new_pass, text='Digite su nueva contraseña',bg=verde,font="Tahoma 15")
        nueva_pass.place(x=85,y=50)
        nueva_pass_entry = Entry(new_pass,width=30,show='*',textvariable=new_contr)
        nueva_pass_entry.place(x=115,y=90)

        #confirmacion de nueva contraseña
        confirm_pass= Label(new_pass, text='confirme su contraseña',bg=verde,font="Tahoma 15")
        confirm_pass.place(x=100,y=130)
        confirm_pass_entry = Entry(new_pass,width=30,show='*',textvariable=confirm_contr)
        confirm_pass_entry.place(x=115,y=170)

        #boton para actualizar contraseña
        actualizar = Button(new_pass,text='actualizar contraseña',command=confirmacion)
        actualizar.place(x=140,y=210)
        new_pass.mainloop()



    titulo = Label(recuperar, text="Restablecer Contraseña",bg=verde,font="Tahoma 20")
    titulo.pack()

    Nombre_usuario = Label(recuperar,text="Ingrese su email",bg=verde,font="Tahoma")
    Nombre_usuario.place(x=55,y=70)

    entrada_usuario = Entry(recuperar,width=40,textvariable=users)
    entrada_usuario.place(x=35,y=110)

    boton_1 = Button(recuperar, text="recuperar contraseña",command=new_password)
    boton_1.place(x=90,y=150)

    recuperar.mainloop()

########################################################################################################
############################## INICIO ##################################
def inicio():
    verde ="#90EE90"
    rojo = "#FF0000"
    inicio = Tk()
    inicio.title('INICIO')
    inicio.geometry("300x300")
    inicio.config(background=verde)
    inicio.resizable(0,0)

    def cerrar():
        messagebox.showinfo('SESION', message='Sesion cerrada correctamente')
        inicio.destroy()
        login()
        
    Nombre_usuer=StringVar()
    Nombre_usuer.set('name user')

    imagen = PhotoImage(file='img_1.png')
    Label(inicio,image=imagen,bg=verde).place(x=235,y=1)


    titulo = Label(inicio, text="Bienvenido",font="Tahoma 20", bg= verde, bd=5)
    titulo.place(x=20,y=30)


    cerrar_cesion=Button(inicio,text='cerrar sesion',command=cerrar)
    cerrar_cesion.place(x=0,y=0)

    inicio.mainloop()
