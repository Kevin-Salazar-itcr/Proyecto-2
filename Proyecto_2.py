#=========================================================================
#=========================================================================
#Parte para la interfaz gráfica
#=========================================================================
#=========================================================================
import tkinter as tk
from tkinter import messagebox as mb
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Acepción de la contraseña
Entrada: la contraseña
Salida: acceso a la parte administrativa
"""
def paseAdmin():
    contraseña= tk.Tk()
    contraseña.title("Confirmar usuario")
     
    ancho_contraseña= 400
    alto_contraseña= 120
    #Porción de código para centrar la ventana a la pantalla 
    x_ventana=contraseña.winfo_screenwidth() // 2 - ancho_contraseña // 2
    y_ventana=contraseña.winfo_screenheight() // 2 - alto_contraseña // 2
    posicion=str(ancho_contraseña)+"x"+str(alto_contraseña)+"+"+str(x_ventana)+"+"+str(y_ventana)
    
    contraseña.geometry(posicion)
    contraseña.resizable(0,0)
    contraseña.iconbitmap("img.ico")
    contraseña.config(bg="#c4a660")
    
    def validar():
        entrada=contra.get()
        f=open("contraseña.txt", "r")
        codigo=f.read()
        f.close()
        while entrada!=codigo:
            error=mb.showerror(title="Error en la contraseña", message="La contraseña es inválida.")
            contraseña.destroy()
            return paseAdmin()
        permiso=mb.showinfo(title="Info", message="Acceso concedido")
        contraseña.destroy()
        return administrador()
      
            
    label=tk.Label(contraseña, text="Digite su contraseña", font=("Sans serif", 16, "italic"), bg="#c4a660" ,relief="sunken").pack()
    contra=tk.Entry(contraseña, font="Helvetica 12", show="*")
    contra.pack()
    valid=tk.Button(contraseña, text="Validar contraseña", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=validar, cursor="hand2").pack()
    contraseña.mainloop()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Funciones del administrador
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Empresas():
    GestionEmpresa= tk.Toplevel()
    #Porción de código para centrar la ventana a la pantalla 
    width= GestionEmpresa.winfo_screenwidth()  
    height= GestionEmpresa.winfo_screenheight() 
    GestionEmpresa.geometry("%dx%d" % (width, height))
    #====================Funciones Auxiliares de gestión de empresas====================#
    """
    IncluirEmpresa
    Como el nombre lo dice, sirve para agregar una empresa a la base de datos
    Entradas:
        La cédula jurídica de la empresa
        El nombre de la empresa
        Su ubicación
    Salida:
        Los datos obtenidos serán guardados en el archivo 'Empresas.txt'
    """
    def IncluirEmpresa():
        nuevaEmpresa=tk.Toplevel()
        #Porción de código para centrar la ventana a la pantalla 
        nuevaEmpresa.geometry("450x600")
        nuevaEmpresa.title("Incluir Empresa")
        nuevaEmpresa.iconbitmap("img.ico")
        Cedula=tk.Label(nuevaEmpresa,text="Cédula Jurídica", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=50)
        cedula=tk.IntVar()
        datoCedula=tk.Entry(nuevaEmpresa, width=14, relief="sunken", textvariable=cedula)
        datoCedula.place(x=200, y=64)
        def contarDigitos(num):
            if num==0:
                return 1
            else:
                res=0
                while num>0:
                    res+=1
                    num//=10
                return res
        def validarNuevaEmpresa(): #Valida que la cédula tenga 10 dígitos
            numCedula=datoCedula.get()
            if(contarDigitos(int(numCedula))!=10):
                error=tk.Label(nuevaEmpresa, text="Error: La cédula debe tener 10 dígitos", font=("Sans Serif", 10), width=30, height=1, fg="red").place(x=200, y=86)
            else:
                correcto=tk.Label(nuevaEmpresa, text="                                                            ", font=("Sans Serif", 10), width=30, height=1).place(x=200, y=86)
                if(SeEncuentra("Empresas.txt", numCedula)):
                    error=tk.Label(nuevaEmpresa, text="Error: La cédula ya se encuentra registrada", font=("Sans Serif", 10), width=32, height=1, fg="red").place(x=194, y=86)
                else:
                    Empresa=datoNombre.get()
                    provincia=provincias.get()
                    ubicacion=direccion.get("1.0", "end-1c")
                    f=open("Empresas.txt", "a")
                    f.write(str(numCedula)+"|"+str(Empresa)+"|"+str(provincia)+", "+str(ubicacion)+"\n")
                    f.close()
                    hecho=mb.showinfo(title="Información", message="La empresa se agregó exitosamente")
                    nuevaEmpresa.destroy()
                    
        """
        SeEncuentra
        E: un archivo y una palabra para buscarla en el archivo
        S: Si la palabra se encuentra en el archivo, retornará True, sino False
        """
        def SeEncuentra(archivo, palabra):
            archivo=open(archivo, "r")
            contexto= archivo.readlines()
            archivo.close()
            Datos=contarObjetos(contexto)
            largoPalabra=contarString(palabra)
            return buscarAux(palabra, contexto, Datos, largoPalabra)
        def contarObjetos(lista): #f.readlines convierte el texto a lista
            n=0
            while lista!=[]:
                n+=1
                lista=lista[1:]
            return n
        def contarString(texto):
            res=0
            while texto!="":
                res+=1
                texto=texto[1:]
            return res
        def buscarAux(palabra, contexto, Datos, largoPalabra):
            if Datos==0:
                return False
            else:
                return buscarAux2(palabra, contexto, contexto[0], Datos, largoPalabra, contarString(contexto[0]), contexto[0])
        def buscarAux2(palabra, contexto, texto, Datos, largoPalabra, i, res):
            if i<largoPalabra:
                return buscarAux(palabra, contexto[1:], Datos-1, largoPalabra)
            else:
                while palabra!=texto[:largoPalabra]:
                    return buscarAux2(palabra, contexto, texto[1:], Datos, largoPalabra, i-1, res)
                return True
        
        Nombre=tk.Label(nuevaEmpresa, text="Nombre de la empresa", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=120)
        datoNombre=tk.Entry(nuevaEmpresa, width=14, relief="sunken")
        datoNombre.place(x=200, y=136)
        from tkinter import ttk
        Ubic=tk.Label(nuevaEmpresa, text="-------------Ubicación-------------", font=("Sans Serif", 12), width=35, height= 2).place(x=55, y=170)
        Provincia=tk.Label(nuevaEmpresa, text= "Provincia", font=("Sans Serif", 12),width=15, height=2).place(x=15,y=210)
        provincias=ttk.Combobox(nuevaEmpresa)
        provincias.place(x=155, y=223)
        provincias["values"]=("San José", "Alajuela","Cartago","Heredia", "Guanacaste", "Puntarenas", "Limón")
        provincias.current(0)
        Direccion=tk.Label(nuevaEmpresa, text="Dirección exacta", font=("Sans Serif", 12), width=15, height=2).place(x=150, y=270)
        direccion=tk.Text(nuevaEmpresa, width=35, height=6, font=("Sans Serif", 12))
        direccion.place(x=61, y=320)
        validacion=tk.Button(nuevaEmpresa, text="Validar", font=("Sans Serif", 12), width=15, height=2, bg="grey", command=validarNuevaEmpresa).place(x=150, y=500)
        nuevaEmpresa.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    BorrarEmpresas
    Dada la cédula de una empresa, elimina la empresa que esté vinculada con dicha cédula
    E: la cédula
    S: Borra la empresa del archivo 'Empresas.txt'
    R: No puede borrarse aquella empresa que esté vinculada a un transporte
    """
    def BorrarEmpresas():
        borrarempresa= tk.Tk()
        borrarempresa.title("Borrar empresa")
             
        ancho_pantalla= 400
        alto_pantalla= 120
        #Porción de código para centrar la ventana a la pantalla 
        x_ventana=borrarempresa.winfo_screenwidth() // 2 - ancho_pantalla // 2
        y_ventana=borrarempresa.winfo_screenheight() // 2 - alto_pantalla // 2
        posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            
        borrarempresa.geometry(posicion)
        borrarempresa.resizable(0,0)
        borrarempresa.iconbitmap("img.ico")
            
        """
        buscarPalabra
        E: un archivo y una palabra para buscarla en el archivo
        S: Si la palabra se encuentra en el archivo, retornará la línea en la cual está ubicada
        """
        def buscarPalabra(archivo,palabra):
            archivo=open(archivo, "r")
            contexto= archivo.readlines()
            archivo.close()
            Datos=contarObjetos(contexto)
            largoPalabra=contarString(palabra)
            return buscarAux(palabra, contexto, Datos, largoPalabra)
        def contarObjetos(lista): 
            n=0
            while lista!=[]:
                n+=1
                lista=lista[1:]
            return n
        def contarString(texto):
            res=0
            while texto!="":
                res+=1
                texto=texto[1:]
            return res
        def buscarAux(palabra, contexto, Datos, largoPalabra):
            if Datos==0:
                return "Sin resultados"
            else:
                return buscarAux2(palabra, contexto, contexto[0], Datos, largoPalabra, contarString(contexto[0]), contexto[0])
        def buscarAux2(palabra, contexto, texto, Datos, largoPalabra, i, res):
            if i<largoPalabra:
                return buscarAux(palabra, contexto[1:], Datos-1, largoPalabra)
            else:
                while palabra!=texto[:largoPalabra]:
                    return buscarAux2(palabra, contexto, texto[1:], Datos, largoPalabra, i-1, res)
                return res
        """
        BorrarLinea
        Dada una palabra clave, borra una linea de un archivo en la cual se encuentra dicha palabra:
        """
        def borrarLinea():
            identif=empresa.get()
            lineaAborrar=buscarPalabra("Empresas.txt", identif)
            if lineaAborrar=="Sin resultados":
                info=mb.showerror(title="Error en entrada", message="No se encontraron coincidencias")
                borrarempresa.destroy()
                return BorrarEmpresas()
            else:
                f = open("Empresas.txt","r")
                lineas = f.readlines()
                f.close()
                f = open("Empresas.txt","w")
                while lineas!=[]:
                    if lineas[0]!=lineaAborrar:
                        f.write(lineas[0])
                        lineas=lineas[1:]
                    else:
                        lineas=lineas[1:]
                f.close()
                info=mb.showinfo(title="Estado", message="La empresa se eliminó exitosamente")
                borrarempresa.destroy()
                return Empresas()
                    
        label=tk.Label(borrarempresa, text="Digite la cédula de la empresa a borrar", font=("Sans serif", 14)).pack()
        empresa=tk.Entry(borrarempresa, font="Helvetica 12")
        empresa.pack()
        borrar=tk.Button(borrarempresa, text="Borrar", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=borrarLinea, cursor="hand2").pack()
        borrarempresa.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    MostrarEmpresas
    Como el nombre lo dice, sirve para mostrar las empresas
    Entrada:
        un botón (Mostrar Empresas)
    Salida:
        Muestra los datos del archivo'Empresas.txt'
    """
    def MostrarEmpresas():
        f=open("Empresas.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay empresas registradas")
            return Empresas()
        else:
            verEmpresas=tk.Toplevel()
            verEmpresas.geometry("400x400")
            verEmpresas.title("Ver Empresas")
            verEmpresas.iconbitmap("img.ico")
            verEmpresas.config(bg="grey")
            verEmpresas.resizable(0,0)
            ListaEmpresas=tk.Listbox(verEmpresas, width=150)
            ListaEmpresas.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barra=tk.Scrollbar(verEmpresas, command=ListaEmpresas.yview)
            barra.place(x=383, y=0, relheight=0.55)
            ListaEmpresas.config(yscrollcommand=barra)
            ListaEmpresas.insert(0, info[0])
            info=info[1:]
            n=1
            while info!=[]:
                ListaEmpresas.insert(n, info[0])
                info=info[1:]
                n+=1
            ListaEmpresas.pack()
            verEmpresas.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    GestionEmpresa.title("BestTraveller: Gestión de viajes")
    GestionEmpresa.iconbitmap("img.ico")
    imagen=tk.PhotoImage(file="f.png")
    fondo=tk.Label(GestionEmpresa, image=imagen).place(x=0, y=0)
    
    label = tk.Label(GestionEmpresa, text="Gestor de Empresas", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    IncluirEmp=tk.Button(GestionEmpresa, text="Incluir Empresas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=IncluirEmpresa).place(x=170, y=150)
    BorrarEmp=tk.Button(GestionEmpresa, text="Borrar Empresas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=BorrarEmpresas).place(x=170, y=200)
    ModificarEmp=tk.Button(GestionEmpresa, text="Modificar Empresas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=250)
    MostrarEmp=tk.Button(GestionEmpresa, text="Mostrar Empresas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2",command=MostrarEmpresas).place(x=170, y=300)
    Volver=tk.Button(GestionEmpresa, text="Volver", command=GestionEmpresa.destroy, font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=350)
    
    GestionEmpresa.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"Pantalla del administrador"
def administrador():
    admin= tk.Toplevel()
    #Porción de código para centrar la ventana a la pantalla 
    width= admin.winfo_screenwidth()  
    height= admin.winfo_screenheight() 
    admin.geometry("%dx%d" % (width, height))
    
    admin.title("BestTraveller: Gestión de viajes")
    admin.iconbitmap("img.ico")
    imagenAdmin=tk.PhotoImage(file="f.png")
    fondoAdmin=tk.Label(admin, image=imagenAdmin).place(x=0, y=0)

    label = tk.Label(admin, text="Bienvenido al control administrativo de BestTraveller", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    Empresa=tk.Button(admin, text="Gestión de empresas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Empresas).place(x=170, y=200)
    Transp=tk.Button(admin, text="Gestión de transporte", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=555, y=200)
    Viaje=tk.Button(admin, text="Gestión de viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=935, y=200)
    Historial=tk.Button(admin, text="Historial de reservas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=250)
    Estadist=tk.Button(admin, text="Estadísticas de viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=555, y=250)
    avanzado=tk.Button(admin, text="Funciones avanzadas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=FuncAvanzadas).place(x=935, y=250)
    Volver=tk.Button(admin, text="Volver", command=admin.destroy, font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=555, y=300)
    EasterEgg= tk.Label(admin, text="Una colaboración de", font=("Monotype Corsiva", 16, "italic"), bg="#c4a660" ,relief="sunken").place(x=599, y=400)
    
    admin.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import time
def formatear():
    pregunta=mb.askyesno(title="Atención", message="Este proceso no se puede deshacer.\n¿Desea continuar? ")
    if(pregunta==True):
        mensaje=mb.showinfo(message="Formateando")
        f = open ("Asientos.txt",'w')
        f.write("")
        f.close()
        f = open ("Empresas.txt",'w')
        f.write("")
        f.close()
        f = open ("Precios.txt",'w')
        f.write("")
        f.close()
        f = open ("Reservas.txt",'w')
        f.write("")
        f.close()
        f = open ("Transportes.txt",'w')
        f.write("")
        f.close()
        f = open ("Viajes.txt",'w')
        f.write("")
        f.close()
        time.sleep(3)
        formateado=mb.showinfo(message="Se ha eliminado toda la base de datos del programa")
        return FuncAvanzadas()
    else:  
        return FuncAvanzadas()
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

def FuncAvanzadas():
    pantallaAvanzado= tk.Toplevel()
    #Porción de código para centrar la ventana a la pantalla 
    width= pantallaAvanzado.winfo_screenwidth()  
    height= pantallaAvanzado.winfo_screenheight() 
    pantallaAvanzado.geometry("%dx%d" % (width, height))
    
    pantallaAvanzado.title("BestTraveller: Gestión de viajes")
    pantallaAvanzado.iconbitmap("img.ico")
    imagenAdmin=tk.PhotoImage(file="f.png")
    fondoAdmin=tk.Label(pantallaAvanzado, image=imagenAdmin).place(x=0, y=0)
    def acercaDe():
        label2=tk.Label(pantallaAvanzado,
                        text="BestTraveller es una aplicación desarrollada para\nla gestión de viajes y reservaciones. \n A través de esta, podrá gestionar:\n -Empresas\n -Viajes\n -Transportes \n -Generar estadísticas\n -Entre otras cosas\nEl programa posee una sencilla interfaz fácil de manipular,\nademás de poseer ciertas características que la vuelven\n en una herramienta confiable y segura.\n¡Gracias por usar BestTraveller!",
                        font=("Times New Roman", 12, "italic"), bg="#c4a660").place(x=600, y=200)

    label = tk.Label(pantallaAvanzado, text="Funciones avanzadas", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    CambioContra=tk.Button(pantallaAvanzado, text="Cambiar Contraseña", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=200)
    infoPrograma=tk.Button(pantallaAvanzado, text="Acerca de", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=acercaDe).place(x=170, y=250)
    formato=tk.Button(pantallaAvanzado, text="Formatear", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=formatear).place(x=170, y=300)
    volver=tk.Button(pantallaAvanzado, text="Volver", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=pantallaAvanzado.destroy).place(x=170, y=350)
    
    pantallaAvanzado.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"Pantalla del usuario"
def usuario():
    ventanaPrincipal.destroy()
    user= tk.Tk()
    #Porción de código para centrar la ventana a la pantalla 
    width= user.winfo_screenwidth()  
    height= user.winfo_screenheight() 
    user.geometry("%dx%d" % (width, height))
    
    user.title("BestTraveller: Gestión de viajes")
    user.iconbitmap("img.ico")
    imagenUser=tk.PhotoImage(file="f.png")
    fondoUser=tk.Label(user, image=imagenUser).place(x=0, y=0)

    label = tk.Label(user, text="Bienvenido a BestTraveller", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    label = tk.Label(user, text="Una aplicación hecha para su comfort", font=("Helvetica", 16, "bold"), bg="#6fafd8" ,relief="sunken").pack()
    consulta=tk.Button(user, text="Consulta de viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=200)
    Reserva=tk.Button(user, text="Reservar Viaje", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=555, y=200)
    CancelReserva=tk.Button(user, text="Cancelar Reserva", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=935, y=200)
    Salir=tk.Button(user, text="Salir", command=user.destroy, font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=555, y=250)
    EasterEgg=label = tk.Label(user, text="Una colaboración de", font=("Monotype Corsiva", 16, "italic"), bg="#c4a660" ,relief="sunken").place(x=599, y=400)
    
    user.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ventana principal
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def salir():
    salir=mb.showinfo(message="Hasta luego. Gracias por preferirnos")
    ventanaPrincipal.destroy()
    
ventanaPrincipal=tk.Tk()
#Porción de código para centrar la ventana a la pantalla 
width= ventanaPrincipal.winfo_screenwidth()  
height= ventanaPrincipal.winfo_screenheight() 
ventanaPrincipal.geometry("%dx%d" % (width, height))

ventanaPrincipal.title("BestTraveller: Gestión de viajes")
ventanaPrincipal.iconbitmap("img.ico")
imagen=tk.PhotoImage(file="f.png")
fondo=tk.Label(ventanaPrincipal, image=imagen).place(x=0, y=0)

label = tk.Label(ventanaPrincipal, text="Bienvenido a BestTraveller", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
Admin=tk.Button(ventanaPrincipal, text="Opciones del Administrador", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", command=paseAdmin, cursor="hand2").place(x=170, y=200)
Cliente=tk.Button(ventanaPrincipal, text="Opciones del Usuario", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", command=usuario, cursor="hand2").place(x=555, y=200)
Salir=tk.Button(ventanaPrincipal, text="Salir", command=salir, font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=935, y=200)
EasterEgg = tk.Label(ventanaPrincipal, text="Una colaboración de", font=("Monotype Corsiva", 16, "italic"), bg="#c4a660" ,relief="sunken").place(x=599, y=400)
  
ventanaPrincipal.mainloop()
