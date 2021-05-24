"Proyecto programado#2: Kevin Salazar"
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
    contraseña.resizable(0,1)
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
    GestionEmpresa.resizable(0,1)
    #====================Funciones Auxiliares de gestión de empresas====================#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
        nuevaEmpresa.geometry("450x600")
        nuevaEmpresa.title("Incluir Empresa")
        nuevaEmpresa.iconbitmap("img.ico")
        nuevaEmpresa.resizable(0,1)
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
                    return Empresas()
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
        borrarempresa.resizable(0,1)
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
            return buscarPalabraAux(palabra, contexto, Datos, largoPalabra)
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
        def buscarPalabraAux(palabra, contexto, Datos, largoPalabra):
            if Datos==0:
                return "Sin resultados"
            else:
                return buscarPalabraAux2(palabra, contexto, contexto[0], Datos, largoPalabra, contarString(contexto[0]), contexto[0])
        def buscarPalabraAux2(palabra, contexto, texto, Datos, largoPalabra, i, res):
            if i<largoPalabra:
                return buscarPalabraAux(palabra, contexto[1:], Datos-1, largoPalabra)
            else:
                while palabra!=texto[:largoPalabra]:
                    return buscarPalabraAux2(palabra, contexto, texto[1:], Datos, largoPalabra, i-1, res)
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
            if(SeEncuentra("Transportes.txt", identif)):
                info=mb.showerror(title="Error en entrada", message="No se puede borrar.\nLa empresa está asociada a un transporte")
                borrarempresa.destroy()
                return Empresas()
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
                    
        label=tk.Label(borrarempresa, text="Digite la cédula de la empresa a borrar", font=("Sans serif", 14)).pack()
        empresa=tk.Entry(borrarempresa, font="Helvetica 12")
        empresa.pack()
        borrar=tk.Button(borrarempresa, text="Borrar", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=borrarLinea, cursor="hand2").pack()
        borrarempresa.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    ModificarEmpresas
    Se selecciona una empresa de la lista de empresas, para posteriormente modificar sus campos
    Entrada:
        la empresa seleccionada (se buscará por cédula y se editará los campos de Nombre y ubicación)
    Salida:
        Los cambios se registrarán en el archivo 'Empresas.txt'
    """
    def modificarEmpresas():
        f=open("Empresas.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay empresas registradas")
            return Empresas()
        else:
            modifEmpresa=tk.Toplevel()
            ancho_pantalla= 400
            alto_pantalla= 400
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=modifEmpresa.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=modifEmpresa.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            modifEmpresa.geometry(posicion)
            modifEmpresa.title("Ver Empresas")
            modifEmpresa.iconbitmap("img.ico")
            modifEmpresa.config(bg="grey")
            modifEmpresa.resizable(0,1)
            def modifCamposEmpresa():
                num=int(emp.get())
                Datos=ListaEmpresas.get(num)
                Cedulaempresa=Datos[3:13]
                RestoDeDatos=recopilarDatos(Datos[14:-4])
                NombreAntiguo=RestoDeDatos[0]
                UbicAntigua=RestoDeDatos[1]
                modifEmpresa.destroy()
                return modifCamposEmpresaAux(Cedulaempresa, NombreAntiguo, UbicAntigua)
            def modifCamposEmpresaAux(Cedulaempresa, NombreAntiguo, UbicAntigua):
                modifEmpresa2=tk.Toplevel()
                #Porción de código para centrar la ventana a la pantalla
                ancho_pantalla= 450
                alto_pantalla= 600
                x_ventana=modifEmpresa2.winfo_screenwidth() // 2 - ancho_pantalla // 2
                y_ventana=modifEmpresa2.winfo_screenheight() // 2 - alto_pantalla // 2
                posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
                modifEmpresa2.geometry(posicion)
                modifEmpresa2.title("Modificar Empresa")
                modifEmpresa2.iconbitmap("img.ico")
                modifEmpresa2.resizable(0,1)
                
                Cedula=tk.Label(modifEmpresa2,text="Cédula Jurídica", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=50)
                datoCedula=tk.Entry(modifEmpresa2, width=14, relief="sunken")
                datoCedula.place(x=200, y=64)
                datoCedula.insert(0, Cedulaempresa)
                datoCedula.config(state=tk.DISABLED)
                def AgregarEmpresaModificada(): #Función para agregar la empresa modificada
                    Cedula=datoCedula.get()
                    Empresa=datoNombre.get()
                    provincia=provincias.get()
                    ubicacion=direccion.get("1.0", "end-1c")
                    lineaAmodificar=buscarPalabra("Empresas.txt", Cedula)
                    f = open("Empresas.txt","r")
                    lineas = f.readlines()
                    f.close()
                    f = open("Empresas.txt","w")
                    while lineas!=[]:
                        if lineas[0]!=lineaAmodificar:
                            f.write(lineas[0])
                            lineas=lineas[1:]
                        else:
                            f.write(str(Cedula)+"|"+str(Empresa)+"|"+str(provincia)+", "+str(ubicacion))
                            lineas=lineas[1:]
                    f.close()
                    info=mb.showinfo(title="Estado", message="La empresa se modificó exitosamente")
                    modifEmpresa2.destroy()
                    return Empresas()
                def buscarPalabra(archivo,palabra):
                    archivo=open(archivo, "r")
                    contexto= archivo.readlines()
                    archivo.close()
                    Datos=contarObjetos(contexto)
                    largoPalabra=contarString(palabra)
                    return buscarPalabraAux(palabra, contexto, Datos, largoPalabra)
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
                def buscarPalabraAux(palabra, contexto, Datos, largoPalabra):
                    if Datos==0:
                        return "Sin resultados"
                    else:
                        return buscarPalabraAux2(palabra, contexto, contexto[0], Datos, largoPalabra, contarString(contexto[0]), contexto[0])
                def buscarPalabraAux2(palabra, contexto, texto, Datos, largoPalabra, i, res):
                    if i<largoPalabra:
                        return buscarPalabraAux(palabra, contexto[1:], Datos-1, largoPalabra)
                    else:
                        while palabra!=texto[:largoPalabra]:
                            return buscarPalabraAux2(palabra, contexto, texto[1:], Datos, largoPalabra, i-1, res)
                        return res
                                       
                Nombre=tk.Label(modifEmpresa2, text="Nombre de la empresa", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=120)
                datoNombre=tk.Entry(modifEmpresa2, width=14, relief="sunken")
                datoNombre.place(x=200, y=136)
                datoNombre.insert(0, NombreAntiguo)
                from tkinter import ttk
                Ubic=tk.Label(modifEmpresa2, text="-------------Ubicación-------------", font=("Sans Serif", 12), width=35, height= 2).place(x=55, y=170)
                Provincia=tk.Label(modifEmpresa2, text= "Provincia", font=("Sans Serif", 12),width=15, height=2).place(x=15,y=210)
                provincias=ttk.Combobox(modifEmpresa2)
                provincias.place(x=155, y=223)
                provincias["values"]=("San José", "Alajuela","Cartago","Heredia", "Guanacaste", "Puntarenas", "Limón")
                provincias.current(0)
                Direccion=tk.Label(modifEmpresa2, text="Dirección exacta", font=("Sans Serif", 12), width=15, height=2).place(x=150, y=270)
                direccion=tk.Text(modifEmpresa2, width=35, height=6, font=("Sans Serif", 12))
                direccion.place(x=61, y=320)
                direccion.insert("1.0", UbicAntigua)
                AgregarModif=tk.Button(modifEmpresa2, text="Modificar", font=("Sans Serif", 12), width=15, height=2, bg="grey", command=AgregarEmpresaModificada).place(x=150, y=500)
                modifEmpresa2.mainloop()
            def recopilarDatos(String): #Cada que la función se encuentre con un " | ", recopilará lo que esté antes de éste y lo almacena en una lista
                if isinstance(String, str):
                    if String=="":
                        return []
                    else:
                        res=[]
                        sub=""
                        while String!="":
                            if String[0]!="|":
                                sub+=String[0]
                                String=String[1:]
                            else:
                                res+=[sub]
                                sub=""
                                String=String[1:]
                        return res+[sub]
                    
            ListaEmpresas=tk.Listbox(modifEmpresa, width=150)
            ListaEmpresas.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(modifEmpresa, command=ListaEmpresas.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaEmpresas.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(modifEmpresa, command=ListaEmpresas.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaEmpresas.config(xscrollcommand=barraX)
            ListaEmpresas.insert(0, "Cédula jurídica | Empresa | Ubicación     |")
            n=1
            i=1
            while info!=[]:
                ListaEmpresas.insert(n, str(i)+") "+info[0]+"____")
                info=info[1:]
                n+=1
                i+=1
            ListaEmpresas.pack()
            Emp=tk.Label(modifEmpresa, text="Empresa #", font=("Sans Serif", 12), bg="grey", width=15, height=2).pack(pady=2)
            dato=tk.IntVar()
            emp=tk.Entry(modifEmpresa, font="Helvetica 12", textvariable=dato)
            emp.pack(pady=2)
            seleccionar=tk.Button(modifEmpresa, text="Seleccionar", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=modifCamposEmpresa, cursor="hand2").pack(pady=2)
            modifEmpresa.mainloop()
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
            ancho_pantalla= 400
            alto_pantalla= 400
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=verEmpresas.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=verEmpresas.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            verEmpresas.geometry(posicion)
            verEmpresas.title("Ver Empresas")
            verEmpresas.iconbitmap("img.ico")
            verEmpresas.config(bg="grey")
            verEmpresas.resizable(0,1)
            ListaEmpresas=tk.Listbox(verEmpresas, width=150)
            ListaEmpresas.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(verEmpresas, command=ListaEmpresas.yview)
            barraY.place(x=693, y=0, relheight=0.55)
            ListaEmpresas.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(verEmpresas, command=ListaEmpresas.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaEmpresas.config(xscrollcommand=barraX)
            ListaEmpresas.insert(0, "Cédula jurídica | Empresa | Ubicación     |")
            n=1
            i=1
            while info!=[]:
                ListaEmpresas.insert(n, str(i)+") "+info[0]+"____")
                info=info[1:]
                n+=1
                i+=1
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
    ModificarEmp=tk.Button(GestionEmpresa, text="Modificar Empresas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=modificarEmpresas).place(x=170, y=250)
    MostrarEmp=tk.Button(GestionEmpresa, text="Mostrar Empresas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2",command=MostrarEmpresas).place(x=170, y=300)
    Volver=tk.Button(GestionEmpresa, text="Volver", command=GestionEmpresa.destroy, font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=350)
    
    GestionEmpresa.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Transportes():
    GestionTransporte= tk.Toplevel()
    width= GestionTransporte.winfo_screenwidth()  
    height= GestionTransporte.winfo_screenheight() 
    GestionTransporte.geometry("%dx%d" % (width, height))
    GestionTransporte.resizable(0,1)
    #====================Funciones Auxiliares de gestión de Transportes====================#
    """
    IncluirTransporte
    Como el nombre lo dice, sirve para agregar un transporte a la base de datos
    Entradas:
        La placa
        El tipo de transporte
        Su marca
        Modelo
        Año
        Empresa (Por Cédula)
        Cantidad de asientos:
            -VIP
            -Normales
            -Económicos
    Salida:
        Los datos obtenidos serán guardados en el archivo 'Transportes.txt'
    Restricciones:
        No pueden existir transportes con el mismo número de matrícula
    """
    def IncluirTransporte():
        nuevoTransporte=tk.Toplevel()
        ancho_pantalla= 450
        alto_pantalla= 600
        #Porción de código para centrar la ventana a la pantalla 
        x_ventana=nuevoTransporte.winfo_screenwidth() // 2 - ancho_pantalla // 2
        y_ventana=nuevoTransporte.winfo_screenheight() // 2 - alto_pantalla // 2
        posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            
        nuevoTransporte.geometry(posicion)
        nuevoTransporte.title("Incluir Transporte")
        nuevoTransporte.iconbitmap("img.ico")
        nuevoTransporte.resizable(0,1)
        Placa=tk.Label(nuevoTransporte, text="N° de matrícula", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=50)
        placa=tk.IntVar()
        datoPlaca=tk.Entry(nuevoTransporte, width=14, relief="sunken", textvariable=placa)
        datoPlaca.place(x=200, y=64)
        def contarDigitos(num):
            if num==0:
                return 1
            else:
                res=0
                while num>0:
                    res+=1
                    num//=10
                return res
        def validarNuevoTransporte(): #Valida que la placa tenga 6 dígitos
            numPlaca=datoPlaca.get()
            if(contarDigitos(int(numPlaca))!=6):
                error=tk.Label(nuevoTransporte, text="Error: El número de matrícula debe tener 6 dígitos", font=("Sans Serif", 10), width=41, height=1, fg="red").place(x=140, y=86)
            else:
                correcto=tk.Label(nuevoTransporte, text="                                                            ", font=("Sans Serif", 10), width=41, height=1).place(x=140, y=86)
                if(SeEncuentra("Transportes.txt", numPlaca)):
                    error=tk.Label(nuevoTransporte, text="Error: La placa ya se encuentra registrada", font=("Sans Serif", 10), width=32, height=1, fg="red").place(x=194, y=86)
                else:
                    placa=str(datoPlaca.get())
                    tipo=str(datoTipo.get())
                    Marca=str(marca.get())
                    Modelo=str(modelo.get())
                    Año=str(año.get())
                    empresa=str(ElegirEmpresa.get())
                    aVIP=str(VIP.get())
                    aNORMAL=str(NORMAL.get())
                    aECONOM=str(ECONOM.get())
                    filas=str(Filas.get())
                    
                    f=open("Transportes.txt", "a")
                    f.write(placa+"|"+tipo+"|"+Marca+"|"+Modelo+"|"+Año+"|"+empresa+"|"+aVIP+"-"+aNORMAL+"-"+aECONOM+"|"+filas+"\n")
                    f.close()
                    f = open ("Asientos.txt",'a')
                    f.write(placa+"|"+aVIP+"|"+aNORMAL+"|"+aECONOM+"|"+filas+"\n")
                    f.close()
                    hecho=mb.showinfo(title="Información", message="El transporte se agregó exitosamente")
                    nuevoTransporte.destroy()
                    return Transportes()
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

        Tipo=tk.Label(nuevoTransporte, text="Tipo de vehículo", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=110)
        datoTipo=tk.Entry(nuevoTransporte, relief="sunken", font=("Sans Serif", 12))
        datoTipo.place(x=200, y=126)
        from tkinter import ttk
        Marca=tk.Label(nuevoTransporte, text= "Marca", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=150)
        marca=tk.Entry(nuevoTransporte, font=("Sans Serif", 12))
        marca.place(x=200, y=166)
        Modelo=tk.Label(nuevoTransporte, text= "Modelo", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=193)
        modelo=tk.Entry(nuevoTransporte, font=("Sans Serif", 12))
        modelo.place(x=200, y=206)
        Año=tk.Label(nuevoTransporte, text= "Año", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=230) 
        año=tk.Entry(nuevoTransporte, font=("Sans Serif", 12))
        año.place(x=200, y=243)
        Empresa=tk.Label(nuevoTransporte, text= "Empresa", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=268)
        ElegirEmpresa=ttk.Combobox(nuevoTransporte)
        ElegirEmpresa.place(x=200, y=280)
        f=open("Empresas.txt", "r")
        lineas=f.readlines()
        f.close()
        if lineas==[]:
            error=mb.showerror(title="Error", message="No hay empresas registradas en el sistema\n No se puede proceder")
            nuevoTransporte.destroy()
            return Transportes()
        else:
            empresas=[]
            while lineas!=[]:
                empresas+=[str(lineas[0])[:10]]
                lineas=lineas[1:]
            ElegirEmpresa["values"]=empresas
            ElegirEmpresa.current(0)
        Asientos=tk.Label(nuevoTransporte, text="-------------Asientos-------------", font=("Sans Serif", 12), width=35, height= 2).place(x=55, y=301)
        vip=tk.Label(nuevoTransporte, text="VIP", font=("Sans Serif", 12), width=10, height= 2).place(x=11, y=354)
        VIP=tk.Entry(nuevoTransporte, font=("Sans Serif", 12), width=8)
        VIP.place(x=18, y=390)
        normal=tk.Label(nuevoTransporte, text="Normales", font=("Sans Serif", 12), width=10, height= 2).place(x=167, y=354)
        NORMAL=tk.Entry(nuevoTransporte, font=("Sans Serif", 12), width=8)
        NORMAL.place(x=177, y=390)
        econom=tk.Label(nuevoTransporte, text="Económicos", font=("Sans Serif", 12), width=10, height= 2).place(x=320, y=354)
        ECONOM=tk.Entry(nuevoTransporte, font=("Sans Serif", 12), width=8)
        ECONOM.place(x=330, y=390)
        filas=tk.Label(nuevoTransporte, text="Asientos por fila", font=("Sans Serif", 12), width=15, height= 2).place(x=147, y=400)
        Filas=tk.Entry(nuevoTransporte, font=("Sans Serif", 12), width=8)
        Filas.place(x=177, y=440)
        
        validacion=tk.Button(nuevoTransporte, text="Validar", font=("Sans Serif", 12), width=15, height=2, bg="grey", command=validarNuevoTransporte).place(x=150, y=500)
        nuevoTransporte.mainloop()                       
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    BorrarTransportes
    Dada la cédula de una empresa, elimina la empresa que esté vinculada con dicha cédula
    E: la cédula
    S: Borra la empresa del archivo 'Empresas.txt'
    R: No puede borrarse aquella empresa que esté vinculada a un transporte
    """
    def BorrarTransportes():
        borrartransporte= tk.Tk()
        borrartransporte.title("Borrar empresa")
             
        ancho_pantalla= 400
        alto_pantalla= 120
        #Porción de código para centrar la ventana a la pantalla 
        x_ventana=borrartransporte.winfo_screenwidth() // 2 - ancho_pantalla // 2
        y_ventana=borrartransporte.winfo_screenheight() // 2 - alto_pantalla // 2
        posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            
        borrartransporte.geometry(posicion)
        borrartransporte.resizable(0,1)
        borrartransporte.iconbitmap("img.ico")
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
            return buscarPalabraAux(palabra, contexto, Datos, largoPalabra)
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
        def buscarPalabraAux(palabra, contexto, Datos, largoPalabra):
            if Datos==0:
                return "Sin resultados"
            else:
                return buscarPalabraAux2(palabra, contexto, contexto[0], Datos, largoPalabra, contarString(contexto[0]), contexto[0])
        def buscarPalabraAux2(palabra, contexto, texto, Datos, largoPalabra, i, res):
            if i<largoPalabra:
                return buscarPalabraAux(palabra, contexto[1:], Datos-1, largoPalabra)
            else:
                while palabra!=texto[:largoPalabra]:
                    return buscarPalabraAux2(palabra, contexto, texto[1:], Datos, largoPalabra, i-1, res)
                return res
        """
        BorrarLinea
        Dada una palabra clave, borra una linea de un archivo en la cual se encuentra dicha palabra:
        """
        def borrarLinea():
            identif=transporte.get()
            lineaAborrar=buscarPalabra("Transportes.txt", identif)
            AsientosABorrar=buscarPalabra("Asientos.txt", identif)
            if lineaAborrar=="Sin resultados":
                info=mb.showerror(title="Error en entrada", message="No se encontraron coincidencias")
                borrartransporte.destroy()
                return BorrarTransportes()
            if(SeEncuentra("Viajes.txt", identif)):
                info=mb.showerror(title="Error en entrada", message="No se puede borrar.\nEl transporte se encuentra registrado en un viaje")
                borrartransporte.destroy()
                return Transportes()
            else:
                f = open("Transportes.txt","r")
                lineas = f.readlines()
                f.close()
                g=open("Asientos.txt", "r")
                asientos=g.readlines()
                g.close()
                f = open("Transportes.txt","w")
                g=open("Asientos.txt", "w")
                while lineas!=[]:
                    if lineas[0]!=lineaAborrar:
                        g.write(asientos[0])
                        f.write(lineas[0])
                        lineas=lineas[1:]
                        asientos=asientos[1:]
                    else:
                        asientos=asientos[1:]
                        lineas=lineas[1:]
                f.close()
                g.close()
                info=mb.showinfo(title="Estado", message="El transporte se eliminó exitosamente")
                borrartransporte.destroy()
                return Transportes()
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
                    
        label=tk.Label(borrartransporte, text="Digite el número de matrícula a borrar", font=("Sans serif", 14)).pack()
        transporte=tk.Entry(borrartransporte, font="Helvetica 12")
        transporte.pack()
        borrar=tk.Button(borrartransporte, text="Borrar", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=borrarLinea, cursor="hand2").pack()
        borrartransporte.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    ModificarTransportes
    Se selecciona un transporte de la lista de transportes, para posteriormente modificar sus campos
    Entrada:
        el transporte seleccionada (Se selecciona por posición y se modifican todos sus campos, exceptuando la placa)
    Salida:
        Los cambios se registrarán en el archivo 'Transportes.txt'
    """
    def modificarTransportes():
        f=open("Transportes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay transportes registrados")
            return Transportes()
        else:
            modifTransporte=tk.Toplevel()
            ancho_pantalla= 700
            alto_pantalla= 400
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=modifTransporte.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=modifTransporte.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            modifTransporte.geometry(posicion)
            modifTransporte.title("Ver Transportes")
            modifTransporte.iconbitmap("img.ico")
            modifTransporte.config(bg="grey")
            modifTransporte.resizable(0,1)
            def modifCamposTransporte():
                num=int(trp.get())
                Datos=ListaTransportes.get(num)
                PlacaVHC=Datos[3:9]
                RestoDeDatos=recopilarDatos(Datos[10:-4])
                TipoAntiguo=RestoDeDatos[0]
                MarcaAntigua=RestoDeDatos[1]
                ModeloAntiguo=RestoDeDatos[2]
                AñoAntiguo=RestoDeDatos[3]
                VIPAntiguo=RestoDeDatos[5]
                NormalAntiguo=RestoDeDatos[6]
                EconomAntiguo=RestoDeDatos[7]
                modifTransporte.destroy()                
                return modifCamposTransporteAux(PlacaVHC, TipoAntiguo, MarcaAntigua, ModeloAntiguo, AñoAntiguo, VIPAntiguo, NormalAntiguo, EconomAntiguo)
            def modifCamposTransporteAux(PlacaVHC, TipoAntiguo, MarcaAntigua, ModeloAntiguo, AñoAntiguo, VIPAntiguo, NormalAntiguo, EconomAntiguo):
                modifTransporte2=tk.Toplevel()
                ancho_pantalla= 450
                alto_pantalla= 600
                #Porción de código para centrar la ventana a la pantalla 
                x_ventana=modifTransporte2.winfo_screenwidth() // 2 - ancho_pantalla // 2
                y_ventana=modifTransporte2.winfo_screenheight() // 2 - alto_pantalla // 2
                posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
                modifTransporte2.geometry(posicion)
                modifTransporte2.title("Modificar transporte")
                modifTransporte2.iconbitmap("img.ico")
                modifTransporte2.resizable(0,1)

                Placa=tk.Label(modifTransporte2, text="N° de matrícula", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=50)
                datoPlaca=tk.Entry(modifTransporte2, width=14, relief="sunken")
                datoPlaca.place(x=200, y=64)
                datoPlaca.insert(0, PlacaVHC)
                datoPlaca.config(state=tk.DISABLED)
                def AgregarTransporteModificado(): #Función para agregar el transporte modificado
                    Placa=str(datoPlaca.get())
                    tipo=str(datoTipo.get())
                    Nuevamarca=str(marca.get())
                    Nuevomodelo=str(modelo.get())
                    nuevoAño=str(año.get())
                    NuevaEmp=str(ElegirEmpresa.get())
                    NuevoVIP=str(VIP.get())
                    NuevoNormal=str(NORMAL.get())
                    NuevoEconom=str(ECONOM.get())
                    filas=str(Filas.get())
                    lineaAmodificar=buscarPalabra("Transportes.txt", Placa)
                    asientosAmodificar=buscarPalabra("Asientos.txt", Placa)
                    f = open("Transportes.txt","r")
                    lineas = f.readlines()
                    f.close()
                    g=open("Asientos.txt", "r")
                    asientos = g.readlines()
                    g.close()
                    f = open("Transportes.txt","w")
                    g=open("Asientos.txt", "w")
                    while lineas!=[]:
                        if lineas[0]!=lineaAmodificar:
                            f.write(lineas[0])
                            g.write(asientos[0])
                            lineas=lineas[1:]
                            asientos=asientos[1:]
                        else:
                            f.write(Placa+"|"+tipo+"|"+Nuevamarca+"|"+Nuevomodelo+"|"+nuevoAño+"|"+NuevaEmp+"|"+NuevoVIP+"-"+NuevoNormal+"-"+NuevoEconom+"|"+filas)
                            g.write(Placa+"|"+NuevoVIP+"|"+NuevoNormal+"|"+NuevoEconom+"|"+filas)
                            lineas=lineas[1:]
                            asientos=asientos[1:]
                    f.close()
                    g.close()
                    info=mb.showinfo(title="Estado", message="El transporte se modificó exitosamente")
                    modifTransporte2.destroy()
                    return Transportes()
                
                def buscarPalabra(archivo,palabra):
                    archivo=open(archivo, "r")
                    contexto= archivo.readlines()
                    archivo.close()
                    Datos=contarObjetos(contexto)
                    largoPalabra=contarString(palabra)
                    return buscarPalabraAux(palabra, contexto, Datos, largoPalabra)
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
                def buscarPalabraAux(palabra, contexto, Datos, largoPalabra):
                    if Datos==0:
                        return "Sin resultados"
                    else:
                        return buscarPalabraAux2(palabra, contexto, contexto[0], Datos, largoPalabra, contarString(contexto[0]), contexto[0])
                def buscarPalabraAux2(palabra, contexto, texto, Datos, largoPalabra, i, res):
                    if i<largoPalabra:
                        return buscarPalabraAux(palabra, contexto[1:], Datos-1, largoPalabra)
                    else:
                        while palabra!=texto[:largoPalabra]:
                            return buscarPalabraAux2(palabra, contexto, texto[1:], Datos, largoPalabra, i-1, res)
                        return res
                Tipo=tk.Label(modifTransporte2, text="Tipo de vehículo", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=110)
                datoTipo=tk.Entry(modifTransporte2, relief="sunken", font=("Sans Serif", 12))
                datoTipo.place(x=200, y=126)
                datoTipo.insert(0, TipoAntiguo)
                from tkinter import ttk
                Marca=tk.Label(modifTransporte2, text= "Marca", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=150)
                marca=tk.Entry(modifTransporte2, font=("Sans Serif", 12))
                marca.place(x=200, y=166)
                marca.insert(0, MarcaAntigua)
                Modelo=tk.Label(modifTransporte2, text= "Modelo", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=193)
                modelo=tk.Entry(modifTransporte2, font=("Sans Serif", 12))
                modelo.place(x=200, y=206)
                modelo.insert(0, ModeloAntiguo)
                Año=tk.Label(modifTransporte2, text= "Año", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=230) 
                año=tk.Entry(modifTransporte2, font=("Sans Serif", 12))
                año.place(x=200, y=243)
                año.insert(0, AñoAntiguo)
                Empresa=tk.Label(modifTransporte2, text= "Empresa", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=268)
                ElegirEmpresa=ttk.Combobox(modifTransporte2)
                ElegirEmpresa.place(x=200, y=280)
                f=open("Empresas.txt", "r")
                lineas=f.readlines()
                f.close()
                empresas=[]
                while lineas!=[]:
                    empresas+=[str(lineas[0])[:10]]
                    lineas=lineas[1:]
                ElegirEmpresa["values"]=empresas
                ElegirEmpresa.current(0)
                Asientos=tk.Label(modifTransporte2, text="-------------Asientos-------------", font=("Sans Serif", 12), width=35, height= 2).place(x=55, y=301)
                vip=tk.Label(modifTransporte2, text="VIP", font=("Sans Serif", 12), width=10, height= 2).place(x=11, y=354)
                VIP=tk.Entry(modifTransporte2, font=("Sans Serif", 12), width=8)
                VIP.place(x=18, y=390)
                VIP.insert(0, VIPAntiguo)
                normal=tk.Label(modifTransporte2, text="Normales", font=("Sans Serif", 12), width=10, height= 2).place(x=167, y=354)
                NORMAL=tk.Entry(modifTransporte2, font=("Sans Serif", 12), width=8)
                NORMAL.place(x=177, y=390)
                NORMAL.insert(0, NormalAntiguo)
                econom=tk.Label(modifTransporte2, text="Económicos", font=("Sans Serif", 12), width=10, height= 2).place(x=320, y=354)
                ECONOM=tk.Entry(modifTransporte2, font=("Sans Serif", 12), width=8)
                ECONOM.place(x=330, y=390)
                ECONOM.insert(0, EconomAntiguo)
                filas=tk.Label(modifTransporte2, text="Asientos por fila", font=("Sans Serif", 12), width=15, height= 2).place(x=147, y=410)
                Filas=tk.Entry(modifTransporte2, font=("Sans Serif", 12), width=8)
                Filas.place(x=177, y=450)
                validacion=tk.Button(modifTransporte2, text="Modificar", font=("Sans Serif", 12), width=15, height=2, bg="grey", command=AgregarTransporteModificado).place(x=150, y=500)
                modifTransporte2.mainloop()
            def recopilarDatos(String): #Cada que la función se encuentre con un " | " o un guión, recopilará lo que esté antes de éste y lo almacena en una lista
                if isinstance(String, str):
                    if String=="":
                        return []
                    else:
                        res=[]
                        sub=""
                        while String!="":
                            if String[0]!="|" and String[0]!="-":
                                sub+=String[0]
                                String=String[1:]
                            else:
                                res+=[sub]
                                sub=""
                                String=String[1:]
                        return res+[sub]

            ListaTransportes=tk.Listbox(modifTransporte, width=150)
            ListaTransportes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(modifTransporte, command=ListaTransportes.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaTransportes.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(modifTransporte, command=ListaTransportes.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaTransportes.config(xscrollcommand=barraX)
            ListaTransportes.insert(0, " Placa  |  Tipo  | Marca  | Modelo | Año |  Empresa  | Asientos VIP - Normales - Económicos | Asientos por fila    |")
            n=1
            i=1
            while info!=[]:
                ListaTransportes.insert(n, str(i)+") "+info[0]+"____")
                info=info[1:]
                i+=1
                n+=1
            ListaTransportes.pack()
            Trp=tk.Label(modifTransporte, text="Transporte #", font=("Sans Serif", 12), bg="grey", width=15, height=2).pack(pady=2)
            dato_trp=tk.IntVar()
            trp=tk.Entry(modifTransporte, font="Helvetica 12", textvariable=dato_trp)
            trp.pack(pady=2)
            seleccionar=tk.Button(modifTransporte, text="Seleccionar", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=modifCamposTransporte, cursor="hand2").pack(pady=2)
            modifTransporte.mainloop()
##    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
##    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    MostrarTransportes
    Como el nombre lo dice, sirve para mostrar los transportes
    Entrada:
        un botón (Mostrar Transportes)
    Salida:
        Muestra los datos del archivo'Transportes.txt'
    """
    def MostrarTransportes():
        f=open("Transportes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay transportes registrados")
            return Transportes()
        else:
            verTransportes=tk.Toplevel()
            ancho_pantalla= 700
            alto_pantalla= 400
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=verTransportes.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=verTransportes.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            verTransportes.geometry(posicion)
            verTransportes.title("Ver Empresas")
            verTransportes.iconbitmap("img.ico")
            verTransportes.config(bg="grey")
            verTransportes.resizable(0,1)
            ListaTransportes=tk.Listbox(verTransportes, width=150)
            ListaTransportes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(verTransportes, command=ListaTransportes.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaTransportes.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(verTransportes, command=ListaTransportes.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaTransportes.config(xscrollcommand=barraX)
            ListaTransportes.insert(0, " Placa  |  Tipo  | Marca  | Modelo | Año |  Empresa  | Asientos VIP - Normales - Económicos | Asientos por fila")
            n=1
            i=1
            while info!=[]:
                ListaTransportes.insert(n, str(i)+") "+info[0]+"____")
                info=info[1:]
                i+=1
                n+=1
            ListaTransportes.pack()
            verTransportes.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    GestionTransporte.title("BestTraveller: Gestión de viajes")
    GestionTransporte.iconbitmap("img.ico")
    imagen=tk.PhotoImage(file="f.png")
    fondo=tk.Label(GestionTransporte, image=imagen).place(x=0, y=0)
    
    label = tk.Label(GestionTransporte, text="Gestor de Transportes", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    IncluirTrp=tk.Button(GestionTransporte, text="Incluir Transportes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=IncluirTransporte).place(x=170, y=150)
    BorrarTrp=tk.Button(GestionTransporte, text="Borrar Transportes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=BorrarTransportes).place(x=170, y=200)
    ModificarTrp=tk.Button(GestionTransporte, text="Modificar Transportes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=modificarTransportes).place(x=170, y=250)
    MostrarTrp=tk.Button(GestionTransporte, text="Mostrar Transportes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2",command=MostrarTransportes).place(x=170, y=300)
    Volver=tk.Button(GestionTransporte, text="Volver", command=GestionTransporte.destroy, font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=350)
    
    GestionTransporte.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Viajes():
    GestionViaje= tk.Toplevel()
    width= GestionViaje.winfo_screenwidth()  
    height= GestionViaje.winfo_screenheight() 
    GestionViaje.geometry("%dx%d" % (width, height))
    GestionViaje.resizable(0,1)
    #====================Funciones Auxiliares de gestión de Viajes====================#
    """
    IncluirViaje
    Como el nombre lo dice, sirve para agregar un viaje a la base de datos
    Entradas:
        Número de viaje
        Provincia y lugar de salida
        Fecha y hora de salida
        Provincia y lugar de llegada
        Fecha y hora de llegada
        Empresa y transporte
        Monto de asientos:
            -VIP
            -Normales
            -Económicos
    Salida:
        Los datos obtenidos serán guardados en el archivo 'Viajes.txt'
    Restricciones:
        No pueden existir viajes con el mismo número de viaje
    """
    def IncluirViaje():
        nuevoViaje=tk.Toplevel()
        ancho_pantalla= 450
        alto_pantalla= 650
        #Porción de código para centrar la ventana a la pantalla 
        x_ventana=nuevoViaje.winfo_screenwidth() // 2 - ancho_pantalla // 2
        y_ventana=nuevoViaje.winfo_screenheight() // 2 - alto_pantalla // 2
        posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            
        nuevoViaje.geometry(posicion)
        nuevoViaje.title("Incluir viaje")
        nuevoViaje.iconbitmap("img.ico")
        nuevoViaje.resizable(0,1)
        numViaje=tk.Label(nuevoViaje, text="N° de viaje", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=20)
        numViaje=tk.Entry(nuevoViaje, width=14, relief="sunken")
        numViaje.place(x=200, y=34)
        import random
        NumViaje=str(random.randint(1000, 9999))
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
        while SeEncuentra("Viajes.txt", NumViaje):
            NumViaje=random.randint(1000, 9999)
        numViaje.insert(0, NumViaje)
        numViaje.config(state=tk.DISABLED)
        
        def contarDigitos(num):
            if num==0:
                return 1
            else:
                res=0
                while num>0:
                    res+=1
                    num//=10
                return res
        def agregarNuevoViaje(): 
            viajeNum=str(numViaje.get())
            Salida=str(LUGSalida.get())+","+str(provincias.get())
            FechaSalida=str(DiaSalida.get())+"/"+str(MesSalida.get())+"/"+str(AñoSalida.get())+","+str(HoraSalida.get())+":"+str(MinSalida.get())+str(TiempoSalida.get())
            Llegada=str(LUGLlegada.get())+","+str(provincias2.get())
            FechaLlegada=str(DiaLlegada.get())+"/"+str(MesLlegada.get())+"/"+str(AñoLlegada.get())+","+str(HoraLlegada.get())+":"+str(MinLlegada.get())+str(TiempoLlegada.get())
            empresa=str(ElegirEmpresa.get())
            trp=str(ElegirTRP.get())
            mVIP=str(VIP.get())
            mNORMAL=str(NORMAL.get())
            mECONOM=str(ECONOM.get())
                    
            f=open("Viajes.txt", "a")
            f.write(viajeNum+"|"+Salida+"|"+FechaSalida+"|"+Llegada+"|"+FechaLlegada+"|"+empresa+","+trp+"|"+mVIP+"-"+mNORMAL+"-"+mECONOM+"\n")
            f.close()
            f.close()
            hecho=mb.showinfo(title="Información", message="El viaje se agregó exitosamente")
            nuevoViaje.destroy()
            return Viajes()
       
        from tkinter import ttk
        infoSalida=tk.Label(nuevoViaje, text= "-----Datos de Salida-----", font=("Sans Serif", 12),width=35, height=2).place(x=50,y=50)
        Provincia=tk.Label(nuevoViaje, text= "Provincia", font=("Sans Serif", 12),width=20, height=2).place(x=27,y=84)
        provincias=ttk.Combobox(nuevoViaje)
        provincias.place(x=184, y=96)
        provincias["values"]=("San José", "Alajuela","Cartago","Heredia", "Guanacaste", "Puntarenas", "Limón")
        provincias.current(0)
        LugSalida=tk.Label(nuevoViaje, text= "Ciudad de Salida", font=("Sans Serif", 12),width=15, height=2).place(x=25,y=116)
        LUGSalida=tk.Entry(nuevoViaje, relief="sunken", font=("Sans Serif", 12))
        LUGSalida.place(x=185, y=128)
        fechaSalida=tk.Label(nuevoViaje, text= "Fecha Salida", font=("Sans Serif", 12),width=15, height=2).place(x=27,y=149)
        DiaSalida=tk.Spinbox(nuevoViaje, from_=1, to=31, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
        DiaSalida.place(x=30, y=190)
        DiaSalida["state"] = "readonly"
        MesSalida=tk.Spinbox(nuevoViaje, from_=1, to=12, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
        MesSalida.place(x=70, y=190)
        MesSalida["state"] = "readonly"
        AñoSalida=tk.Spinbox(nuevoViaje, from_=2021, to=2030, relief="raise", font=("Sans Serif", 12), width=5, wrap=True)
        AñoSalida.place(x=110, y=190)
        AñoSalida["state"] = "readonly"
        horaSalida=tk.Label(nuevoViaje, text= "Hora Salida", font=("Sans Serif", 12),width=15, height=2).place(x=194,y=149)
        horas=["01","02","03","04","05","06","07","08","09","10","11","12"]
        HoraSalida=tk.Spinbox(nuevoViaje, values=horas, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
        HoraSalida.place(x=200, y=190)
        HoraSalida["state"] = "readonly"
        mins=["00", "01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
        MinSalida=tk.Spinbox(nuevoViaje, values=mins, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
        MinSalida.place(x=240, y=190)
        MinSalida["state"] = "readonly"
        TiempoSalida=tk.Spinbox(nuevoViaje, values=("AM","PM"), relief="raise", font=("Sans Serif", 12), width=3, wrap=True)
        TiempoSalida.place(x=280, y=190)
        TiempoSalida["state"] = "readonly"

        
        infoLlegada=tk.Label(nuevoViaje, text= "-----Datos de llegada-----", font=("Sans Serif", 12),width=35, height=2).place(x=50,y=230)
        Provincia2=tk.Label(nuevoViaje, text= "Provincia", font=("Sans Serif", 12),width=20, height=2).place(x=27,y=260)
        provincias2=ttk.Combobox(nuevoViaje)
        provincias2.place(x=184, y=274)
        provincias2["values"]=("San José", "Alajuela","Cartago","Heredia", "Guanacaste", "Puntarenas", "Limón")
        provincias2.current(0)
        LugLlegada=tk.Label(nuevoViaje, text= "Ciudad de Llegada", font=("Sans Serif", 12),width=15, height=2).place(x=25,y=290)
        LUGLlegada=tk.Entry(nuevoViaje, relief="sunken", font=("Sans Serif", 12))
        LUGLlegada.place(x=185, y=304)
        fechaLlegada=tk.Label(nuevoViaje, text= "Fecha Llegada", font=("Sans Serif", 12),width=15, height=2).place(x=27,y=329)
        DiaLlegada=tk.Spinbox(nuevoViaje, from_=1, to=31, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
        DiaLlegada.place(x=30, y=370)
        DiaLlegada["state"] = "readonly"
        MesLlegada=tk.Spinbox(nuevoViaje, from_=1, to=12, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
        MesLlegada.place(x=70, y=370)
        MesLlegada["state"] = "readonly"
        AñoLlegada=tk.Spinbox(nuevoViaje, from_=2021, to=2030, relief="raise", font=("Sans Serif", 12), width=5, wrap=True)
        AñoLlegada.place(x=110, y=370)
        AñoLlegada["state"] = "readonly"
        horaLlegada=tk.Label(nuevoViaje, text= "Hora Llegada", font=("Sans Serif", 12),width=15, height=2).place(x=194,y=329)
        HoraLlegada=tk.Spinbox(nuevoViaje, values=horas, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
        HoraLlegada.place(x=200, y=370)
        HoraLlegada["state"] = "readonly"
        MinLlegada=tk.Spinbox(nuevoViaje, values=mins, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
        MinLlegada.place(x=240, y=370)
        MinLlegada["state"] = "readonly"
        TiempoLlegada=tk.Spinbox(nuevoViaje, values=("AM","PM"), relief="raise", font=("Sans Serif", 12), width=3, wrap=True)
        TiempoLlegada.place(x=280, y=370)
        TiempoLlegada["state"] = "readonly"
        
        Empresa=tk.Label(nuevoViaje, text= "Empresa", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=400)
        ElegirEmpresa=ttk.Combobox(nuevoViaje)
        ElegirEmpresa.place(x=45, y=440)
        f=open("Empresas.txt", "r")
        lineas=f.readlines()
        f.close()
        if lineas==[]:
            error=mb.showerror(title="Error", message="No hay empresas registradas en el sistema\n No se puede proceder")
            nuevoViaje.destroy()
            return Viajes()
        else:
            empresas=[]
            while lineas!=[]:
                empresas+=[str(lineas[0])[:10]]
                lineas=lineas[1:]
            ElegirEmpresa["values"]=empresas
            ElegirEmpresa.current(0)
            
        Transporte=tk.Label(nuevoViaje, text= "Transporte", font=("Sans Serif", 12),width=25, height=2).place(x=200,y=400)
        ElegirTRP=ttk.Combobox(nuevoViaje)
        ElegirTRP.place(x=245, y=440)
        f=open("Transportes.txt", "r")
        lineas=f.readlines()
        f.close()
        if lineas==[]:
            error=mb.showerror(title="Error", message="No hay transportes registradas en el sistema\n No se puede proceder")
            nuevoViaje.destroy()
            return Viajes()
        else:
            transportes=[]
            while lineas!=[]:
                transportes+=[str(lineas[0])[:6]]
                lineas=lineas[1:]
            ElegirTRP["values"]=transportes
            ElegirTRP.current(0)
        Precios=tk.Label(nuevoViaje, text="-------------Precios-------------", font=("Sans Serif", 12), width=35, height= 2).place(x=55, y=470)
        vip=tk.Label(nuevoViaje, text="VIP", font=("Sans Serif", 12), width=10, height= 2).place(x=11, y=500)
        VIP=tk.Entry(nuevoViaje, font=("Sans Serif", 12), width=8)
        VIP.place(x=18, y=540)
        normal=tk.Label(nuevoViaje, text="Normales", font=("Sans Serif", 12), width=10, height= 2).place(x=167, y=500)
        NORMAL=tk.Entry(nuevoViaje, font=("Sans Serif", 12), width=8)
        NORMAL.place(x=177, y=540)
        econom=tk.Label(nuevoViaje, text="Económicos", font=("Sans Serif", 12), width=10, height= 2).place(x=320, y=500)
        ECONOM=tk.Entry(nuevoViaje, font=("Sans Serif", 12), width=8)
        ECONOM.place(x=330, y=540)
        
        validacion=tk.Button(nuevoViaje, text="Agregar", font=("Sans Serif", 12), width=15, height=2, bg="grey", command=agregarNuevoViaje).place(x=140, y=580)
        nuevoViaje.mainloop()                       
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    BorrarViajes
    Dado un número de viaje, elimina el que esté vinculado con dicho número
    E: el número de viaje
    S: Borra el viaje del archivo 'Viajes.txt'
    """
    def BorrarViajes():
        borrarviaje= tk.Tk()
        borrarviaje.title("Borrar viaje")
             
        ancho_pantalla= 400
        alto_pantalla= 120
        #Porción de código para centrar la ventana a la pantalla 
        x_ventana=borrarviaje.winfo_screenwidth() // 2 - ancho_pantalla // 2
        y_ventana=borrarviaje.winfo_screenheight() // 2 - alto_pantalla // 2
        posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            
        borrarviaje.geometry(posicion)
        borrarviaje.resizable(0,1)
        borrarviaje.iconbitmap("img.ico")
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
            return buscarPalabraAux(palabra, contexto, Datos, largoPalabra)
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
        def buscarPalabraAux(palabra, contexto, Datos, largoPalabra):
            if Datos==0:
                return "Sin resultados"
            else:
                return buscarPalabraAux2(palabra, contexto, contexto[0], Datos, largoPalabra, contarString(contexto[0]), contexto[0])
        def buscarPalabraAux2(palabra, contexto, texto, Datos, largoPalabra, i, res):
            if i<largoPalabra:
                return buscarPalabraAux(palabra, contexto[1:], Datos-1, largoPalabra)
            else:
                while palabra!=texto[:largoPalabra]:
                    return buscarPalabraAux2(palabra, contexto, texto[1:], Datos, largoPalabra, i-1, res)
                return res
        """
        BorrarLinea
        Dada una palabra clave, borra una linea de un archivo en la cual se encuentra dicha palabra:
        """
        def borrarLinea():
            identif=viaje.get()
            lineaAborrar=buscarPalabra("Viajes.txt", identif)
            if lineaAborrar=="Sin resultados":
                info=mb.showerror(title="Error en entrada", message="No se encontraron coincidencias")
                borrarviaje.destroy()
                return BorrarViajes()
            else:
                f = open("Viajes.txt","r")
                lineas = f.readlines()
                f.close()
                f = open("Viajes.txt","w")
                while lineas!=[]:
                    if lineas[0]!=lineaAborrar:
                        f.write(lineas[0])
                        lineas=lineas[1:]
                    else:
                        lineas=lineas[1:]
                f.close()
                info=mb.showinfo(title="Estado", message="El viaje se eliminó exitosamente")
                borrarviaje.destroy()
                return Viajes()
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
                    
        label=tk.Label(borrarviaje, text="Digite el número del viaje a borrar", font=("Sans serif", 14)).pack()
        viaje=tk.Entry(borrarviaje, font="Helvetica 12")
        viaje.pack()
        borrar=tk.Button(borrarviaje, text="Borrar", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=borrarLinea, cursor="hand2").pack()
        borrarviaje.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    modificarViajes
    Se selecciona un viaje de la lista de viajes, para posteriormente modificar sus campos
    Entrada:
        el viaje seleccionado (Se selecciona por posición y se modifican sus campos)
    Salida:
        Los cambios se registrarán en el archivo 'Viajes.txt'
    """
    def modificarViajes():
        f=open("Viajes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay Viajes registrados")
            return Viajes()
        else:
            modifViaje=tk.Toplevel()
            ancho_pantalla= 700
            alto_pantalla= 400
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=modifViaje.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=modifViaje.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            modifViaje.geometry(posicion)
            modifViaje.title("Ver Viajes")
            modifViaje.iconbitmap("img.ico")
            modifViaje.config(bg="grey")
            modifViaje.resizable(0,1)
            def modifCamposViaje():
                num=int(viaje.get())
                Datos=ListaViajes.get(num)
                numViaje=Datos[3:7]
                RestoDeDatos=recopilarDatos(Datos[8:-4])
                salidaAntigua=RestoDeDatos[0]
                llegadaAntigua=RestoDeDatos[4]
                VIPAntiguo=RestoDeDatos[10]
                NormalAntiguo=RestoDeDatos[11]
                EconomAntiguo=RestoDeDatos[12]
                modifViaje.destroy()                
                return modifCamposViajeAux(numViaje, salidaAntigua, llegadaAntigua, VIPAntiguo, NormalAntiguo, EconomAntiguo)
            def modifCamposViajeAux(numViaje, salidaAntigua, llegadaAntigua, VIPAntiguo, NormalAntiguo, EconomAntiguo):
                modifViaje2=tk.Toplevel()
                ancho_pantalla= 450
                alto_pantalla= 650
                #Porción de código para centrar la ventana a la pantalla 
                x_ventana=modifViaje2.winfo_screenwidth() // 2 - ancho_pantalla // 2
                y_ventana=modifViaje2.winfo_screenheight() // 2 - alto_pantalla // 2
                posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
                modifViaje2.geometry(posicion)
                modifViaje2.title("Modificar Viaje")
                modifViaje2.iconbitmap("img.ico")
                modifViaje2.resizable(0,1)
                Viaje=tk.Label(modifViaje2, text="N° de viaje", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=20)
                NumViaje=tk.Entry(modifViaje2, width=14, relief="sunken")
                NumViaje.place(x=200, y=34)
                NumViaje.insert(0, numViaje)
                NumViaje.config(state=tk.DISABLED)
                def AgregarViajeModificado(): #Función para agregar el viaje modificado
                    viajeNum=str(NumViaje.get())
                    Salida=str(LUGSalida.get())+","+str(provincias.get())
                    FechaSalida=str(DiaSalida.get())+"/"+str(MesSalida.get())+"/"+str(AñoSalida.get())+","+str(HoraSalida.get())+":"+str(MinSalida.get())+str(TiempoSalida.get())
                    Llegada=str(LUGLlegada.get())+","+str(provincias2.get())
                    FechaLlegada=str(DiaLlegada.get())+"/"+str(MesLlegada.get())+"/"+str(AñoLlegada.get())+","+str(HoraLlegada.get())+":"+str(MinLlegada.get())+str(TiempoLlegada.get())
                    empresa=str(ElegirEmpresa.get())
                    trp=str(ElegirTRP.get())
                    mVIP=str(VIP.get())
                    mNORMAL=str(NORMAL.get())
                    mECONOM=str(ECONOM.get())
                    lineaAmodificar=buscarPalabra("Viajes.txt", viajeNum)
                    f = open("Viajes.txt","r")
                    lineas = f.readlines()
                    f.close()
                    f = open("Viajes.txt","w")
                    while lineas!=[]:
                        if lineas[0]!=lineaAmodificar:
                            f.write(lineas[0])
                            lineas=lineas[1:]
                        else:
                            f.write(viajeNum+"|"+Salida+"|"+FechaSalida+"|"+Llegada+"|"+FechaLlegada+"|"+empresa+","+trp+"|"+mVIP+"-"+mNORMAL+"-"+mECONOM)
                            lineas=lineas[1:]
                    f.close()
                    info=mb.showinfo(title="Estado", message="El viaje se modificó exitosamente")
                    modifViaje2.destroy()
                    return Viajes()
                
                def buscarPalabra(archivo,palabra):
                    archivo=open(archivo, "r")
                    contexto= archivo.readlines()
                    archivo.close()
                    Datos=contarObjetos(contexto)
                    largoPalabra=contarString(palabra)
                    return buscarPalabraAux(palabra, contexto, Datos, largoPalabra)
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
                def buscarPalabraAux(palabra, contexto, Datos, largoPalabra):
                    if Datos==0:
                        return "Sin resultados"
                    else:
                        return buscarPalabraAux2(palabra, contexto, contexto[0], Datos, largoPalabra, contarString(contexto[0]), contexto[0])
                def buscarPalabraAux2(palabra, contexto, texto, Datos, largoPalabra, i, res):
                    if i<largoPalabra:
                        return buscarPalabraAux(palabra, contexto[1:], Datos-1, largoPalabra)
                    else:
                        while palabra!=texto[:largoPalabra]:
                            return buscarPalabraAux2(palabra, contexto, texto[1:], Datos, largoPalabra, i-1, res)
                        return res
                from tkinter import ttk
                infoSalida=tk.Label(modifViaje2, text= "-----Datos de Salida-----", font=("Sans Serif", 12),width=35, height=2).place(x=50,y=50)
                Provincia=tk.Label(modifViaje2, text= "Provincia", font=("Sans Serif", 12),width=20, height=2).place(x=27,y=84)
                provincias=ttk.Combobox(modifViaje2)
                provincias.place(x=184, y=96)
                provincias["values"]=("San José", "Alajuela","Cartago","Heredia", "Guanacaste", "Puntarenas", "Limón")
                provincias.current(0)
                LugSalida=tk.Label(modifViaje2, text= "Ciudad de Salida", font=("Sans Serif", 12),width=15, height=2).place(x=25,y=116)
                LUGSalida=tk.Entry(modifViaje2, relief="sunken", font=("Sans Serif", 12))
                LUGSalida.place(x=185, y=128)
                LUGSalida.insert(0, salidaAntigua)
                fechaSalida=tk.Label(modifViaje2, text= "Fecha Salida", font=("Sans Serif", 12),width=15, height=2).place(x=27,y=149)
                DiaSalida=tk.Spinbox(modifViaje2, from_=1, to=31, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
                DiaSalida.place(x=30, y=190)
                DiaSalida["state"] = "readonly"
                MesSalida=tk.Spinbox(modifViaje2, from_=1, to=12, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
                MesSalida.place(x=70, y=190)
                MesSalida["state"] = "readonly"
                AñoSalida=tk.Spinbox(modifViaje2, from_=2021, to=2030, relief="raise", font=("Sans Serif", 12), width=5, wrap=True)
                AñoSalida.place(x=110, y=190)
                AñoSalida["state"] = "readonly"
                horaSalida=tk.Label(modifViaje2, text= "Hora Salida", font=("Sans Serif", 12),width=15, height=2).place(x=194,y=149)
                horas=["01","02","03","04","05","06","07","08","09","10","11","12"]
                HoraSalida=tk.Spinbox(modifViaje2, values=horas, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
                HoraSalida.place(x=200, y=190)
                HoraSalida["state"] = "readonly"
                mins=["00", "01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
                MinSalida=tk.Spinbox(modifViaje2, values=mins, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
                MinSalida.place(x=240, y=190)
                MinSalida["state"] = "readonly"
                TiempoSalida=tk.Spinbox(modifViaje2, values=("AM","PM"), relief="raise", font=("Sans Serif", 12), width=3, wrap=True)
                TiempoSalida.place(x=280, y=190)
                TiempoSalida["state"] = "readonly"

                
                infoLlegada=tk.Label(modifViaje2, text= "-----Datos de llegada-----", font=("Sans Serif", 12),width=35, height=2).place(x=50,y=230)
                Provincia2=tk.Label(modifViaje2, text= "Provincia", font=("Sans Serif", 12),width=20, height=2).place(x=27,y=260)
                provincias2=ttk.Combobox(modifViaje2)
                provincias2.place(x=184, y=274)
                provincias2["values"]=("San José", "Alajuela","Cartago","Heredia", "Guanacaste", "Puntarenas", "Limón")
                provincias2.current(0)
                LugLlegada=tk.Label(modifViaje2, text= "Ciudad de Llegada", font=("Sans Serif", 12),width=15, height=2).place(x=25,y=290)
                LUGLlegada=tk.Entry(modifViaje2, relief="sunken", font=("Sans Serif", 12))
                LUGLlegada.place(x=185, y=304)
                LUGLlegada.insert(0, llegadaAntigua)
                fechaLlegada=tk.Label(modifViaje2, text= "Fecha Llegada", font=("Sans Serif", 12),width=15, height=2).place(x=27,y=329)
                DiaLlegada=tk.Spinbox(modifViaje2, from_=1, to=31, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
                DiaLlegada.place(x=30, y=370)
                DiaLlegada["state"] = "readonly"
                MesLlegada=tk.Spinbox(modifViaje2, from_=1, to=12, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
                MesLlegada.place(x=70, y=370)
                MesLlegada["state"] = "readonly"
                AñoLlegada=tk.Spinbox(modifViaje2, from_=2021, to=2030, relief="raise", font=("Sans Serif", 12), width=5, wrap=True)
                AñoLlegada.place(x=110, y=370)
                AñoLlegada["state"] = "readonly"
                horaLlegada=tk.Label(modifViaje2, text= "Hora Llegada", font=("Sans Serif", 12),width=15, height=2).place(x=194,y=329)
                HoraLlegada=tk.Spinbox(modifViaje2, values=horas, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
                HoraLlegada.place(x=200, y=370)
                HoraLlegada["state"] = "readonly"
                MinLlegada=tk.Spinbox(modifViaje2, values=mins, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
                MinLlegada.place(x=240, y=370)
                MinLlegada["state"] = "readonly"
                TiempoLlegada=tk.Spinbox(modifViaje2, values=("AM","PM"), relief="raise", font=("Sans Serif", 12), width=3, wrap=True)
                TiempoLlegada.place(x=280, y=370)
                TiempoLlegada["state"] = "readonly"
                
                Empresa=tk.Label(modifViaje2, text= "Empresa", font=("Sans Serif", 12),width=25, height=2).place(x=0,y=400)
                ElegirEmpresa=ttk.Combobox(modifViaje2)
                ElegirEmpresa.place(x=45, y=440)
                f=open("Empresas.txt", "r")
                lineas=f.readlines()
                f.close()
                if lineas==[]:
                    error=mb.showerror(title="Error", message="No hay empresas registradas en el sistema\n No se puede proceder")
                    modifViaje2.destroy()
                    return Viajes()
                else:
                    empresas=[]
                    while lineas!=[]:
                        empresas+=[str(lineas[0])[:10]]
                        lineas=lineas[1:]
                    ElegirEmpresa["values"]=empresas
                    ElegirEmpresa.current(0)
                    
                Transporte=tk.Label(modifViaje2, text= "Transporte", font=("Sans Serif", 12),width=25, height=2).place(x=200,y=400)
                ElegirTRP=ttk.Combobox(modifViaje2)
                ElegirTRP.place(x=245, y=440)
                f=open("Transportes.txt", "r")
                lineas=f.readlines()
                f.close()
                if lineas==[]:
                    error=mb.showerror(title="Error", message="No hay transportes registradas en el sistema\n No se puede proceder")
                    modifViaje2.destroy()
                    return Viajes()
                else:
                    transportes=[]
                    while lineas!=[]:
                        transportes+=[str(lineas[0])[:6]]
                        lineas=lineas[1:]
                    ElegirTRP["values"]=transportes
                    ElegirTRP.current(0)
                Precios=tk.Label(modifViaje2, text="-------------Precios-------------", font=("Sans Serif", 12), width=35, height= 2).place(x=55, y=470)
                vip=tk.Label(modifViaje2, text="VIP", font=("Sans Serif", 12), width=10, height= 2).place(x=11, y=500)
                VIP=tk.Entry(modifViaje2, font=("Sans Serif", 12), width=8)
                VIP.place(x=18, y=540)
                VIP.insert(0, VIPAntiguo)
                normal=tk.Label(modifViaje2, text="Normales", font=("Sans Serif", 12), width=10, height= 2).place(x=167, y=500)
                NORMAL=tk.Entry(modifViaje2, font=("Sans Serif", 12), width=8)
                NORMAL.place(x=177, y=540)
                NORMAL.insert(0, NormalAntiguo)
                econom=tk.Label(modifViaje2, text="Económicos", font=("Sans Serif", 12), width=10, height= 2).place(x=320, y=500)
                ECONOM=tk.Entry(modifViaje2, font=("Sans Serif", 12), width=8)
                ECONOM.place(x=330, y=540)
                ECONOM.insert(0, EconomAntiguo)
                validacion=tk.Button(modifViaje2, text="Modificar", font=("Sans Serif", 12), width=15, height=2, bg="grey", command=AgregarViajeModificado).place(x=140, y=580)
                modifViaje2.mainloop()
            def recopilarDatos(String): 
                if isinstance(String, str):
                    if String=="":
                        return []
                    else:
                        res=[]
                        sub=""
                        while String!="":
                            if String[0]!="|" and String[0]!="-" and String[0]!=",":
                                sub+=String[0]
                                String=String[1:]
                            else:
                                res+=[sub]
                                sub=""
                                String=String[1:]
                        return res+[sub]


            
            viajenum=tk.Label(modifViaje, text="Viaje #", font=("Sans Serif", 12), bg="grey", width=15, height=2).pack(pady=2)
            dato_trp=tk.IntVar()
            viaje=tk.Entry(modifViaje, font="Helvetica 12", textvariable=dato_trp)
            viaje.pack(pady=2)
            seleccionar=tk.Button(modifViaje, text="Seleccionar", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=modifCamposViaje, cursor="hand2").pack(pady=2)
            modifViaje.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    MostrarViajes
    Como el nombre lo dice, sirve para mostrar los viajes
    Entrada:
        un botón (Mostrar Viajes)
    Salida:
        Muestra los datos del archivo'Viajes.txt'
    """
    def MostrarViajes():
        f=open("Viajes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay viajes registrados")
            return Viajes()
        else:
            verViajes=tk.Toplevel()
            ancho_pantalla= 700
            alto_pantalla= 400
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=verViajes.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=verViajes.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            verViajes.geometry(posicion)
            verViajes.title("Ver Viajes")
            verViajes.iconbitmap("img.ico")
            verViajes.config(bg="grey")
            verViajes.resizable(0,1)
            ListaViajes=tk.Listbox(verViajes, width=150)
            ListaViajes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(verViajes, command=ListaViajes.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaViajes.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(verViajes, command=ListaViajes.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaViajes.config(xscrollcommand=barraX)
            ListaViajes.insert(0, " Nº Viaje  |  Lugar Salida  | Fecha-Hora Salida | Lugar Llegada  | Fecha-Hora Llegada | Empresa  | Transporte |Montos VIP - Normales - Económicos   |")
            n=1
            i=1
            while info!=[]:
                ListaViajes.insert(n, str(i)+") "+info[0]+"____")
                info=info[1:]
                i+=1
                n+=1
            ListaViajes.pack()
            verViajes.mainloop()
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    GestionViaje.title("BestTraveller: Gestión de viajes")
    GestionViaje.iconbitmap("img.ico")
    imagen=tk.PhotoImage(file="f.png")
    fondo=tk.Label(GestionViaje, image=imagen).place(x=0, y=0)
    
    label = tk.Label(GestionViaje, text="Gestor de Viajes", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    IncluirVj=tk.Button(GestionViaje, text="Incluir viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=IncluirViaje).place(x=170, y=150)
    BorrarVj=tk.Button(GestionViaje, text="Borrar viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=BorrarViajes).place(x=170, y=200)
    ModificarVj=tk.Button(GestionViaje, text="Modificar viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=modificarViajes).place(x=170, y=250)
    MostrarVj=tk.Button(GestionViaje, text="Mostrar viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2",command=MostrarViajes).place(x=170, y=300)
    Volver=tk.Button(GestionViaje, text="Volver", command=GestionViaje.destroy, font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=350)
    
    GestionViaje.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Estadísticas
Esta función dará al administrador 2 opciones de estadísticas: de viajes y de empresas
Entradas:
    En la primera instancia, se selecciona un viaje de la lista de viajes.
    En la otra, se selecciona una empresa
Salidas:
    En la primera opción:
        Nº viaje
        Empresa, transporte
        Lugar, fecha y hora salida
        Lugar, fecha y hora llegada
        Cantidad de asientos reservados y disponibles en cada categoría
        Costo por boleto VIP, normal y económico
        Monto total recaudado
        *Se crea un reporte en un archivo
    En la segunda:
        Cédula jurídica
        Nombre de empresa
        Cantidad de transporte (Con detalle de matrícula)
        Cantidad de viajes (Con detalle de identificador)
        *Se crea un reporte
"""
def Estadisticas():
    Seleccione=tk.Toplevel()
    ancho_pantalla=400
    alto_pantalla= 300
    #Porción de código para centrar la ventana a la pantalla 
    x_ventana=Seleccione.winfo_screenwidth() // 2 - ancho_pantalla // 2
    y_ventana=Seleccione.winfo_screenheight() // 2 - alto_pantalla // 2
    posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
    Seleccione.geometry(posicion)
    Seleccione.iconbitmap("img.ico")
    imagen=tk.PhotoImage(file="f.png")
    def EstadisticaViaje():
        pass
    def EstadisticaEmpresa():
        f=open("Empresas.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay empresas registradas")
            return administrador()
        else:
            SelecEmpresa=tk.Toplevel()
            ancho_pantalla= 400
            alto_pantalla= 400
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=SelecEmpresa.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=SelecEmpresa.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            SelecEmpresa.geometry(posicion)
            SelecEmpresa.title("Ver Empresas")
            SelecEmpresa.iconbitmap("img.ico")
            SelecEmpresa.config(bg="grey")
            SelecEmpresa.resizable(0,1)
            def RecopilarEstadisticaEmpresa():
                num=int(emp.get())
                Datos=ListaEmpresas.get(num)
                Cedulaempresa=Datos[3:13]
                RestoDeDatos=recopilarDatos(Datos[14:-4])
                Nombre=RestoDeDatos[0]
                f=open("Transportes.txt", "r")
                transportes=f.readlines()
                f.close()
                cantTransportes=[]
                def SeEncuentra(linea, palabra):
                    largoPalabra=contarString(palabra)
                    return buscarAux(palabra, linea, largoPalabra, contarString(linea))
                def contarString(texto):
                    res=0
                    while texto!="":
                        res+=1
                        texto=texto[1:]
                    return res
                def buscarAux(palabra, linea, largoPalabra, i):
                    if i<largoPalabra:
                        return False
                    else:
                        while palabra!=linea[:largoPalabra]:
                            return buscarAux(palabra, linea[1:], largoPalabra, i-1)
                        return True
                while transportes!=[]:
                    if SeEncuentra(transportes[0], Cedulaempresa):
                        cantTransportes+=[transportes[0][:6]]
                        transportes=transportes[1:]
                    else:
                        transportes=transportes[1:]
                print("este",cantTransportes)
                f=open("Viajes.txt", "r")
                viajes=f.readlines()
                f.close()
                cantViajes=[]
                while viajes!=[]:
                    if SeEncuentra(viajes[0], Cedulaempresa):
                        cantViajes+=[viajes[0][:4]]
                        viajes=viajes[1:]
                    else:
                        viajes=viajes[1:]
                return MostrarEstadisticaEmpresa(Cedulaempresa, Nombre, cantTransportes, cantViajes)
            def recopilarDatos(String): #Cada que la función se encuentre con un " | ", recopilará lo que esté antes de éste y lo almacena en una lista
                if isinstance(String, str):
                    if String=="":
                        return []
                    else:
                        res=[]
                        sub=""
                        while String!="":
                            if String[0]!="|":
                                sub+=String[0]
                                String=String[1:]
                            else:
                                res+=[sub]
                                sub=""
                                String=String[1:]
                        return res+[sub]
            
            def MostrarEstadisticaEmpresa(Cedulaempresa, Nombre, cantTransportes, cantViajes):
                mostrarEstadEmpresa=tk.Toplevel()
                #Porción de código para centrar la ventana a la pantalla
                ancho_pantalla= 450
                alto_pantalla= 600
                x_ventana=mostrarEstadEmpresa.winfo_screenwidth() // 2 - ancho_pantalla // 2
                y_ventana=mostrarEstadEmpresa.winfo_screenheight() // 2 - alto_pantalla // 2
                posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
                mostrarEstadEmpresa.geometry(posicion)
                mostrarEstadEmpresa.title("Estadísiticas de la Empresa")
                mostrarEstadEmpresa.iconbitmap("img.ico")
                mostrarEstadEmpresa.resizable(0,1)
                Cedula=tk.Label(mostrarEstadEmpresa,text="Cédula Jurídica", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=50)
                datoCedula=tk.Label(mostrarEstadEmpresa, text=str(Cedulaempresa),width=14, relief="sunken").place(x=200, y=64)
                nombre=tk.Label(mostrarEstadEmpresa, text="Nombre de la empresa", font=("Sans Serif", 12), width=25, height=2). place(x=0, y=120)
                datoNombre=tk.Label(mostrarEstadEmpresa, text=str(Nombre), width=14, relief="sunken").place(x=200, y=136)
                trp=tk.Label(mostrarEstadEmpresa, text="Transportes de la empresa", font=("Sans Serif", 12), width=25, height=2). place(x=120, y=160)
                ListaTransportes=tk.Listbox(mostrarEstadEmpresa, width=40, height=4)
                ListaTransportes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
                barraY=tk.Scrollbar(mostrarEstadEmpresa, command=ListaTransportes.yview)
                barraY.place(x=358, y=202, relheight=0.17)
                ListaTransportes.config(yscrollcommand=barraY)
                n=0
                x=1
                m=cantTransportes
                while cantTransportes!=[]:
                    ListaTransportes.insert(n, str(x)+") "+cantTransportes[0])
                    cantTransportes=cantTransportes[1:]
                    n+=1
                    x+=1
                if n==0:
                    ListaTransportes.insert(n, "Cantidad de transportes registrados:", 0)
                else:
                    ListaTransportes.insert(n, "Cantidad de transportes registrados:", x-1)
                ListaTransportes.place(x=85, y=205)
                label=tk.Label(mostrarEstadEmpresa, text="Viajes de la empresa", font=("Sans Serif", 12), width=25, height=2). place(x=120, y=300)
                ListaViajes=tk.Listbox(mostrarEstadEmpresa, width=40, height=4)
                ListaViajes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
                barraY=tk.Scrollbar(mostrarEstadEmpresa, command=ListaViajes.yview)
                barraY.place(x=358, y=330, relheight=0.17)
                ListaViajes.config(yscrollcommand=barraY)
                b=0
                i=1
                a=cantViajes
                while cantViajes!=[]:
                    ListaViajes.insert(n, str(i)+") "+cantViajes[0])
                    cantViajes=cantViajes[1:]
                    n+=1
                    i+=1
                if n==0:
                    ListaViajes.insert(n, "Cantidad de viajes registrados:", 0)
                else:
                    ListaViajes.insert(n, "Cantidad de viajes registrados:", i-1)
                ListaViajes.place(x=85, y=330)
                def crearReporteEmpresa(): #Función para agregar el reporte de la empresa
                    f=open(str(Cedulaempresa)+".txt", "w")
                    f.write("Cédula Empresa: "+str(Cedulaempresa)+"\n"+"Nombre: "+str(Nombre)+"\n"+"Transportes registrados: "+str(x-1)+"\n"+str(m)+"\n"+"Viajes registrados: "+str(i-1)+"\n"+str(a))
                    print("Cédula Empresa: "+str(Cedulaempresa)+"\n"+"Nombre: "+str(Nombre)+"\n"+"Transportes registrados: "+str(x-1)+"\n"+str(m)+"\n"+"Viajes registrados: "+str(i-1)+"\n"+str(a))
                    f.close()
                    ya=mb.showinfo(title="información", message="El reporte ha sido creado")
                    mostrarEstadEmpresa.destroy()
                    return administrador()
                
                AgregarModif=tk.Button(mostrarEstadEmpresa, text="Crear reporte", font=("Sans Serif", 12), width=15, height=2, bg="grey", command=crearReporteEmpresa).place(x=150, y=500)
                mostrarEstadEmpresa.mainloop()
                
            def recopilarDatos(String): #Cada que la función se encuentre con un " | ", recopilará lo que esté antes de éste y lo almacena en una lista
                if isinstance(String, str):
                    if String=="":
                        return []
                    else:
                        res=[]
                        sub=""
                        while String!="":
                            if String[0]!="|":
                                sub+=String[0]
                                String=String[1:]
                            else:
                                res+=[sub]
                                sub=""
                                String=String[1:]
                        return res+[sub]
            
            ListaEmpresas=tk.Listbox(SelecEmpresa, width=150)
            ListaEmpresas.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(SelecEmpresa, command=ListaEmpresas.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaEmpresas.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(SelecEmpresa, command=ListaEmpresas.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaEmpresas.config(xscrollcommand=barraX)
            ListaEmpresas.insert(0, "Cédula jurídica | Empresa | Ubicación     |")
            n=1
            i=1
            while info!=[]:
                ListaEmpresas.insert(n, str(i)+") "+info[0]+"____")
                info=info[1:]
                n+=1
                i+=1
            ListaEmpresas.pack()
            Emp=tk.Label(SelecEmpresa, text="Empresa #", font=("Sans Serif", 12), bg="grey", width=15, height=2).pack(pady=2)
            dato=tk.IntVar()
            emp=tk.Entry(SelecEmpresa, font="Helvetica 12", textvariable=dato)
            emp.pack(pady=2)
            seleccionar=tk.Button(SelecEmpresa, text="Seleccionar", font=("Helvetica",14), bg="#6ee2ff", width="16",height="1",relief="groove", command=RecopilarEstadisticaEmpresa, cursor="hand2").pack(pady=2)
            SelecEmpresa.mainloop()
        
    fondo=tk.Label(Seleccione, image=imagen).place(x=0, y=0)
    label=tk.Label(Seleccione, text="Seleccione una de las opciones", bg="#6ee2ff", font=("Sans serif", 14)).pack(pady=4)
    viaje=tk.Button(Seleccione, cursor="hand2", text="Viajes", font=("Sans Serif", 14), width=10, bg="#c4a660").pack(pady=4)
    emp=tk.Button(Seleccione, cursor="hand2", text="Empresas", font=("Sans Serif", 14), width=10, bg="#c4a660", command=EstadisticaEmpresa).pack(pady=4)
    Seleccione.mainloop()
            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

"Pantalla del administrador"
def administrador():
    admin= tk.Toplevel()
    #Porción de código para pantalla completa
    width= admin.winfo_screenwidth()  
    height= admin.winfo_screenheight() 
    admin.geometry("%dx%d" % (width, height))
    admin.resizable(0,1)
    admin.title("BestTraveller: Gestión de viajes")
    admin.iconbitmap("img.ico")
    imagenAdmin=tk.PhotoImage(file="f.png")
    fondoAdmin=tk.Label(admin, image=imagenAdmin).place(x=0, y=0)

    label = tk.Label(admin, text="Bienvenido al control administrativo de BestTraveller", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    Empresa=tk.Button(admin, text="Gestión de empresas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Empresas).place(x=170, y=200)
    Transp=tk.Button(admin, text="Gestión de transporte", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Transportes).place(x=555, y=200)
    Viaje=tk.Button(admin, text="Gestión de viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Viajes).place(x=935, y=200)
    Historial=tk.Button(admin, text="Historial de reservas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=170, y=250)
    Estadist=tk.Button(admin, text="Estadísticas", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Estadisticas).place(x=555, y=250)
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
    pantallaAvanzado.resizable(0,1)
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
#Funciones del usuario
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Consulta de viajes
Esta función le permite al usuario realizar busquedas en la lista de viajes del sistema
Al dar clic en el botón, aparecerá una pantalla con diferentes filtros de búsqueda.
"""
def Filtro1():
    ventanaX=tk.Toplevel()
    ancho_pantalla= 400
    alto_pantalla= 200
    #Porción de código para centrar la ventana a la pantalla 
    x_ventana=ventanaX.winfo_screenwidth() // 2 - ancho_pantalla // 2
    y_ventana=ventanaX.winfo_screenheight() // 2 - alto_pantalla // 2
    posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
    ventanaX.geometry(posicion)
    ventanaX.resizable(0,1)
    
    def buscarInfoViaje():
        dato=str(filtro1.get())
        f=open("Viajes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay viajes registrados")
            return user()
        else:
            resultadosViajes=tk.Toplevel()
            resultadosViajes.title("Ver viajes")
            ancho_pantalla= 700
            alto_pantalla= 270
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=resultadosViajes.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=resultadosViajes.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            resultadosViajes.geometry(posicion)
            resultadosViajes.resizable(0,1)
            ListaViajes=tk.Listbox(resultadosViajes, width=150)
            ListaViajes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(resultadosViajes, command=ListaViajes.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaViajes.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(resultadosViajes, command=ListaViajes.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaViajes.config(xscrollcommand=barraX)
            ListaViajes.insert(0, " Nº Viaje  |  Lugar Salida  | Fecha-Hora Salida | Lugar Llegada  | Fecha-Hora Llegada | Empresa  | Transporte |Montos VIP - Normales - Económicos   |")
            def SeEncuentra(linea, palabra):
                largoPalabra=contarString(palabra)
                return buscarAux(palabra, linea, largoPalabra, contarString(linea))
            def contarString(texto):
                res=0
                while texto!="":
                    res+=1
                    texto=texto[1:]
                return res
            def buscarAux(palabra, linea, largoPalabra, i):
                if i<largoPalabra:
                    return False
                else:
                    while palabra!=linea[:largoPalabra]:
                        return buscarAux(palabra, linea[1:], largoPalabra, i-1)
                    return True
            n=1
            i=1
            while info!=[]:
                if SeEncuentra(info[0], dato):
                    ListaViajes.insert(n, str(i)+") "+info[0]+"____")
                    info=info[1:]
                    i+=1
                    n+=1
                else:
                    info=info[1:]
            ListaViajes.insert(n, "Total de coincidencias:"+str(i-1))
            ListaViajes.pack()
            resultadosViajes.mainloop()
    FiltroElegido=tk.Label(ventanaX, text="Empresa", font=("Helvetica", 12), width=20, height=2).place(x=0, y=50)
    filtro1=tk.Entry(ventanaX, width=14, relief="sunken")
    filtro1.place(x=170, y=64)
    boton2=tk.Button(ventanaX, text="Buscar", width=8, height=1,font=("Helvetica", 12), command=buscarInfoViaje).place(x=155, y=100)
    ventanaX.mainloop()
            
def Filtro2():
    ventanaX=tk.Toplevel()
    ancho_pantalla= 400
    alto_pantalla= 200
    #Porción de código para centrar la ventana a la pantalla 
    x_ventana=ventanaX.winfo_screenwidth() // 2 - ancho_pantalla // 2
    y_ventana=ventanaX.winfo_screenheight() // 2 - alto_pantalla // 2
    posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
    ventanaX.geometry(posicion)
    ventanaX.resizable(0,1)
    def buscarInfoViaje():
        dato=str(filtro1.get())
        f=open("Viajes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay viajes registrados")
            return user()
        else:
            resultadosViajes=tk.Toplevel()
            resultadosViajes.title("Ver viajes")
            ancho_pantalla= 700
            alto_pantalla= 270
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=resultadosViajes.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=resultadosViajes.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            resultadosViajes.geometry(posicion)
            resultadosViajes.resizable(0,1)
            ListaViajes=tk.Listbox(resultadosViajes, width=150)
            ListaViajes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(resultadosViajes, command=ListaViajes.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaViajes.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(resultadosViajes, command=ListaViajes.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaViajes.config(xscrollcommand=barraX)
            ListaViajes.insert(0, " Nº Viaje  |  Lugar Salida  | Fecha-Hora Salida | Lugar Llegada  | Fecha-Hora Llegada | Empresa  | Transporte |Montos VIP - Normales - Económicos   |")
            def SeEncuentra(linea, palabra):
                largoPalabra=contarString(palabra)
                return buscarAux(palabra, linea, largoPalabra, contarString(linea))
            def contarString(texto):
                res=0
                while texto!="":
                    res+=1
                    texto=texto[1:]
                return res
            def buscarAux(palabra, linea, largoPalabra, i):
                if i<largoPalabra:
                    return False
                else:
                    while palabra!=linea[:largoPalabra]:
                        return buscarAux(palabra, linea[1:], largoPalabra, i-1)
                    return True
            n=1
            i=1
            while info!=[]:
                if SeEncuentra(info[0], dato):
                    ListaViajes.insert(n, str(i)+") "+info[0]+"____")
                    info=info[1:]
                    i+=1
                    n+=1
                else:
                    info=info[1:]
            ListaViajes.insert(n, "Total de coincidencias:"+str(i-1))
            ListaViajes.pack()
            resultadosViajes.mainloop()
    FiltroElegido=tk.Label(ventanaX, text="Lugar de salida", font=("Helvetica", 12), width=20, height=2).place(x=0, y=50)
    filtro1=tk.Entry(ventanaX, width=14, relief="sunken")
    filtro1.place(x=180, y=64)
    boton2=tk.Button(ventanaX, text="Buscar", width=8, height=1,font=("Helvetica", 12), command=buscarInfoViaje).place(x=155, y=100)
    ventanaX.mainloop()
def Filtro4():
    ventanaX=tk.Toplevel()
    ancho_pantalla= 400
    alto_pantalla= 200
    #Porción de código para centrar la ventana a la pantalla 
    x_ventana=ventanaX.winfo_screenwidth() // 2 - ancho_pantalla // 2
    y_ventana=ventanaX.winfo_screenheight() // 2 - alto_pantalla // 2
    posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
    ventanaX.geometry(posicion)
    ventanaX.resizable(0,1)
    def buscarInfoViaje():
        dato=str(DiaSalida.get())+"/"+str(MesSalida.get())+"/"+str(AñoSalida.get())
        f=open("Viajes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay viajes registrados")
            return user()
        else:
            resultadosViajes=tk.Toplevel()
            resultadosViajes.title("Ver viajes")
            ancho_pantalla= 400
            alto_pantalla= 270
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=resultadosViajes.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=resultadosViajes.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            resultadosViajes.geometry(posicion)
            resultadosViajes.resizable(0,1)
            ListaViajes=tk.Listbox(resultadosViajes, width=150)
            ListaViajes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(resultadosViajes, command=ListaViajes.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaViajes.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(resultadosViajes, command=ListaViajes.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaViajes.config(xscrollcommand=barraX)
            ListaViajes.insert(0, " Nº Viaje  |  Lugar Salida  | Fecha-Hora Salida | Lugar Llegada  | Fecha-Hora Llegada | Empresa  | Transporte |Montos VIP - Normales - Económicos   |")
            def SeEncuentra(linea, palabra):
                largoPalabra=contarString(palabra)
                return buscarAux(palabra, linea, largoPalabra, contarString(linea))
            def contarString(texto):
                res=0
                while texto!="":
                    res+=1
                    texto=texto[1:]
                return res
            def buscarAux(palabra, linea, largoPalabra, i):
                if i<largoPalabra:
                    return False
                else:
                    while palabra!=linea[:largoPalabra]:
                        return buscarAux(palabra, linea[1:], largoPalabra, i-1)
                    return True
            n=1
            i=1
            while info!=[]:
                if SeEncuentra(info[0], dato):
                    ListaViajes.insert(n, str(i)+") "+info[0]+"____")
                    info=info[1:]
                    i+=1
                    n+=1
                else:
                    info=info[1:]
            ListaViajes.insert(n, "Total de coincidencias:"+str(i-1))
            ListaViajes.pack()
            resultadosViajes.mainloop()
    FiltroElegido=tk.Label(ventanaX, text="Fecha de salida", font=("Helvetica", 12), width=20, height=2).place(x=0, y=50)
    DiaSalida=tk.Spinbox(ventanaX, from_=1, to=31, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
    DiaSalida.place(x=170, y=64)
    DiaSalida["state"] = "readonly"
    MesSalida=tk.Spinbox(ventanaX, from_=1, to=12, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
    MesSalida.place(x=210, y=64)
    MesSalida["state"] = "readonly"
    AñoSalida=tk.Spinbox(ventanaX, from_=2021, to=2030, relief="raise", font=("Sans Serif", 12), width=5, wrap=True)
    AñoSalida.place(x=250, y=64)
    AñoSalida["state"] = "readonly"
    boton2=tk.Button(ventanaX, text="Buscar", width=8, height=1,font=("Helvetica", 12), command=buscarInfoViaje).place(x=155, y=100)
    ventanaX.mainloop()
def Filtro3():
    ventanaX=tk.Toplevel()
    ancho_pantalla= 400
    alto_pantalla= 200
    #Porción de código para centrar la ventana a la pantalla 
    x_ventana=ventanaX.winfo_screenwidth() // 2 - ancho_pantalla // 2
    y_ventana=ventanaX.winfo_screenheight() // 2 - alto_pantalla // 2
    posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
    ventanaX.geometry(posicion)
    ventanaX.resizable(0,1)
    def buscarInfoViaje():
        dato=str(filtro1.get())
        f=open("Viajes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay viajes registrados")
            return user()
        else:
            resultadosViajes=tk.Toplevel()
            resultadosViajes.title("Ver viajes")
            ancho_pantalla= 700
            alto_pantalla= 270
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=resultadosViajes.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=resultadosViajes.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            resultadosViajes.geometry(posicion)
            resultadosViajes.resizable(0,1)
            ListaViajes=tk.Listbox(resultadosViajes, width=150)
            ListaViajes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(resultadosViajes, command=ListaViajes.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaViajes.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(resultadosViajes, command=ListaViajes.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaViajes.config(xscrollcommand=barraX)
            ListaViajes.insert(0, " Nº Viaje  |  Lugar Salida  | Fecha-Hora Salida | Lugar Llegada  | Fecha-Hora Llegada | Empresa  | Transporte |Montos VIP - Normales - Económicos   |")
            def SeEncuentra(linea, palabra):
                largoPalabra=contarString(palabra)
                return buscarAux(palabra, linea, largoPalabra, contarString(linea))
            def contarString(texto):
                res=0
                while texto!="":
                    res+=1
                    texto=texto[1:]
                return res
            def buscarAux(palabra, linea, largoPalabra, i):
                if i<largoPalabra:
                    return False
                else:
                    while palabra!=linea[:largoPalabra]:
                        return buscarAux(palabra, linea[1:], largoPalabra, i-1)
                    return True
            n=1
            i=1
            while info!=[]:
                if SeEncuentra(info[0], dato):
                    ListaViajes.insert(n, str(i)+") "+info[0]+"____")
                    info=info[1:]
                    i+=1
                    n+=1
                else:
                    info=info[1:]
            ListaViajes.insert(n, "Total de coincidencias:"+str(i-1))
            ListaViajes.pack()
            resultadosViajes.mainloop()
    FiltroElegido=tk.Label(ventanaX, text="Lugar de llegada", font=("Helvetica", 12), width=20, height=2).place(x=0, y=50)
    filtro1=tk.Entry(ventanaX, width=14, relief="sunken")
    filtro1.place(x=180, y=64)
    boton2=tk.Button(ventanaX, text="Buscar", width=8, height=1,font=("Helvetica", 12), command=buscarInfoViaje).place(x=155, y=100)
    ventanaX.mainloop()
def Filtro5():
    ventanaX=tk.Toplevel()
    ancho_pantalla= 400
    alto_pantalla= 200
    #Porción de código para centrar la ventana a la pantalla 
    x_ventana=ventanaX.winfo_screenwidth() // 2 - ancho_pantalla // 2
    y_ventana=ventanaX.winfo_screenheight() // 2 - alto_pantalla // 2
    posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
    ventanaX.geometry(posicion)
    ventanaX.resizable(0,1)
    def buscarInfoViaje():
        dato=str(DiaSalida.get())+"/"+str(MesSalida.get())+"/"+str(AñoSalida.get())
        f=open("Viajes.txt", "r")
        info=f.readlines()
        f.close()
        if info==[]:
            mensaje=mb.showinfo(title="Atención", message="No hay viajes registrados")
            return user()
        else:
            resultadosViajes=tk.Toplevel()
            resultadosViajes.title("Ver viajes")
            ancho_pantalla= 700
            alto_pantalla= 270
            #Porción de código para centrar la ventana a la pantalla 
            x_ventana=resultadosViajes.winfo_screenwidth() // 2 - ancho_pantalla // 2
            y_ventana=resultadosViajes.winfo_screenheight() // 2 - alto_pantalla // 2
            posicion=str(ancho_pantalla)+"x"+str(alto_pantalla)+"+"+str(x_ventana)+"+"+str(y_ventana)
            resultadosViajes.geometry(posicion)
            resultadosViajes.resizable(0,1)
            ListaViajes=tk.Listbox(resultadosViajes, width=150)
            ListaViajes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(resultadosViajes, command=ListaViajes.yview)
            barraY.place(x=683, y=0, relheight=0.55)
            ListaViajes.config(yscrollcommand=barraY)
            barraX=tk.Scrollbar(resultadosViajes, command=ListaViajes.xview, orient=tk.HORIZONTAL)
            barraX.place(x=0, y=217, relwidth=0.6)
            ListaViajes.config(xscrollcommand=barraX)
            ListaViajes.insert(0, " Nº Viaje  |  Lugar Salida  | Fecha-Hora Salida | Lugar Llegada  | Fecha-Hora Llegada | Empresa  | Transporte |Montos VIP - Normales - Económicos   |")
            def SeEncuentra(linea, palabra):
                largoPalabra=contarString(palabra)
                return buscarAux(palabra, linea, largoPalabra, contarString(linea))
            def contarString(texto):
                res=0
                while texto!="":
                    res+=1
                    texto=texto[1:]
                return res
            def buscarAux(palabra, linea, largoPalabra, i):
                if i<largoPalabra:
                    return False
                else:
                    while palabra!=linea[:largoPalabra]:
                        return buscarAux(palabra, linea[1:], largoPalabra, i-1)
                    return True
            n=1
            i=1
            while info!=[]:
                if SeEncuentra(info[0], dato):
                    ListaViajes.insert(n, str(i)+") "+info[0]+"____")
                    info=info[1:]
                    i+=1
                    n+=1
                else:
                    info=info[1:]
            ListaViajes.insert(n, "Total de coincidencias:"+str(i-1))
            ListaViajes.pack()
            resultadosViajes.mainloop()
    FiltroElegido=tk.Label(ventanaX, text="Fecha de llegada", font=("Helvetica", 12), width=20, height=2).place(x=0, y=50)
    DiaSalida=tk.Spinbox(ventanaX, from_=1, to=31, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
    DiaSalida.place(x=170, y=64)
    DiaSalida["state"] = "readonly"
    MesSalida=tk.Spinbox(ventanaX, from_=1, to=12, relief="raise", font=("Sans Serif", 12), width=2, wrap=True)
    MesSalida.place(x=210, y=64)
    MesSalida["state"] = "readonly"
    AñoSalida=tk.Spinbox(ventanaX, from_=2021, to=2030, relief="raise", font=("Sans Serif", 12), width=5, wrap=True)
    AñoSalida.place(x=250, y=64)
    AñoSalida["state"] = "readonly"
    boton2=tk.Button(ventanaX, text="Buscar", width=8, height=1,font=("Helvetica", 12), command=buscarInfoViaje).place(x=155, y=100)
    ventanaX.mainloop()
def consultaViajes():
    filtrosParaViajes= tk.Toplevel()
    #Porción de código para centrar la ventana a la pantalla 
    width= filtrosParaViajes.winfo_screenwidth()  
    height= filtrosParaViajes.winfo_screenheight() 
    filtrosParaViajes.geometry("%dx%d" % (width, height))
    filtrosParaViajes.resizable(0,1)
    filtrosParaViajes.title("BestTraveller: Gestión de viajes")
    filtrosParaViajes.iconbitmap("img.ico")
    imagen=tk.PhotoImage(file="f.png")
    fondo=tk.Label(filtrosParaViajes, image=imagen).place(x=0, y=0)

    label = tk.Label(filtrosParaViajes, text="Menú de filtros", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    empresa=tk.Button(filtrosParaViajes, text="Empresa", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Filtro1).place(x=170, y=200)
    lugarSalida=tk.Button(filtrosParaViajes, text="Lugar de salida", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Filtro2).place(x=555, y=200)
    lugarLlegada=tk.Button(filtrosParaViajes, text="Lugar de llegada", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Filtro3).place(x=935, y=200)
    volver=tk.Button(filtrosParaViajes, text="Volver", command=filtrosParaViajes.destroy, font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2").place(x=555, y=250)
    fechaSalida=tk.Button(filtrosParaViajes, text="Fecha de salida", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Filtro4).place(x=170, y=250)
    fechaLlegadaSalir=tk.Button(filtrosParaViajes, text="Fecha de llegada", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=Filtro5).place(x=935, y=250)
    
    filtrosParaViajes.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
ReservarViaje
Esta función permite al usuario hacer una reservación en un viaje
Entradas:
    El usuario dará los siguientes datos:
        Seleccionar un viaje de la lista
        El nombre del usuario
        La cantidad de asientos VIP, normales y/o económicos a reservar
Salida:
    Se le entragará al usuario un comprobante al usuario con los siguientes datos:
        Id de reserva (autogenerado)
        Nombre de quien reserva
        Fecha y hora de reserva (capturadas del sistema)
        Empresa
        Transporte
        Lugar, fecha y hora de salida
        Lugar, fecha y hora de llegada
        Cantidad de asientos reservados en clase VIP, normal y económica
        Monto total de reservación
    La reserva será registrada en el archivo 'Reservas.txt'
Restricciones:
    Deben haber asientos disponibles en el viaje para proceder
    Debe reservar al menos un asiento
"""
def ReservarViaje():
    f=open("Viajes.txt", "r")
    info=f.readlines()
    f.close()
    if info==[]:
        mensaje=mb.showinfo(title="Atención", message="No hay viajes registrados")
        return Viajes()
    else:
        Reservas= tk.Toplevel()
        #Porción de código para centrar la ventana a la pantalla 
        width= Reservas.winfo_screenwidth()  
        height= Reservas.winfo_screenheight() 
        Reservas.geometry("%dx%d" % (width, height))
        Reservas.resizable(0,1)
        Reservas.title("BestTraveller: Gestión de viajes")
        Reservas.iconbitmap("img.ico")
        imagenUser=tk.PhotoImage(file="f.png")
        fondoUser=tk.Label(Reservas, image=imagenUser).place(x=0, y=0)
        label = tk.Label(Reservas, text="Bienvenido al sistema de reservas de BestTraveller", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
        label2 = tk.Label(Reservas, text="A continuación se le mostrará la lista de viajes registrados en el sistema.", font=("Helvetica", 16, "bold"), bg="#6fafd8" ,relief="sunken").pack(pady=10)
        ListaViajes=tk.Listbox(Reservas, width=150)
        ListaViajes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
        barraY=tk.Scrollbar(Reservas, command=ListaViajes.yview)
        barraY.place(x=1210, y=88, relheight=0.312)
        ListaViajes.config(yscrollcommand=barraY)
        barraX=tk.Scrollbar(Reservas, command=ListaViajes.xview, orient=tk.HORIZONTAL)
        barraX.place(x=155, y=305, relwidth=0.6)
        ListaViajes.config(xscrollcommand=barraX)
        ListaViajes.insert(0, " Nº Viaje  |  Lugar Salida  | Fecha-Hora Salida | Lugar Llegada  | Fecha-Hora Llegada | Empresa  | Transporte |Montos VIP - Normales - Económicos   |")
        n=1
        i=1
        while info!=[]:
            ListaViajes.insert(n, str(i)+") "+info[0]+"____")
            info=info[1:]
            i+=1
            n+=1
        ListaViajes.pack()
        Viaje=tk.Label(Reservas, text="Viaje #", font=("Sans Serif", 12), width=15, height=2).pack(pady=2)
        dato=tk.IntVar()
        SelecViaje=tk.Entry(Reservas, font="Helvetica 12", textvariable=dato)
        SelecViaje.pack(pady=2)
        seleccionar=tk.Button(Reservas, text="Seleccionar", font=("Helvetica",14), bg="#6ee2ff", width="16", relief="groove", command=None, cursor="hand2").pack(pady=2)
            
    Reservas.mainloop()
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
    user.resizable(0,1)
    user.title("BestTraveller: Gestión de viajes")
    user.iconbitmap("img.ico")
    imagenUser=tk.PhotoImage(file="f.png")
    fondoUser=tk.Label(user, image=imagenUser).place(x=0, y=0)

    label = tk.Label(user, text="Bienvenido a BestTraveller", font=("Helvetica", 20, "italic", "bold"), bg="#6fafd8" ,relief="sunken").pack()
    label = tk.Label(user, text="Una aplicación hecha para su comfort", font=("Helvetica", 16, "bold"), bg="#6fafd8" ,relief="sunken").pack()
    consulta=tk.Button(user, text="Consulta de viajes", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=consultaViajes).place(x=170, y=200)
    Reserva=tk.Button(user, text="Reservar Viaje", font=("Helvetica",14), bg="#6ee2ff", width="23",height="1",relief="groove", cursor="hand2", command=ReservarViaje).place(x=555, y=200)
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
ventanaPrincipal.resizable(0,1)
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
