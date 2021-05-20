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
            modifEmpresa.geometry("400x400")
            modifEmpresa.title("Ver Empresas")
            modifEmpresa.iconbitmap("img.ico")
            modifEmpresa.config(bg="grey")
            modifEmpresa.resizable(0,1)
            def modifCamposEmpresa():
                num=int(emp.get())
                Datos=ListaEmpresas.get(num)
                Cedulaempresa=Datos[3:13]
                RestoDeDatos=recopilarDatos(Datos[14:-4])
                print(RestoDeDatos)
                NombreAntiguo=RestoDeDatos[0]
                UbicAntigua=RestoDeDatos[1]
                modifEmpresa.destroy()
                return modifCamposEmpresaAux(Cedulaempresa, NombreAntiguo, UbicAntigua)
            def modifCamposEmpresaAux(Cedulaempresa, NombreAntiguo, UbicAntigua):
                modifEmpresa2=tk.Toplevel()
                #Porción de código para centrar la ventana a la pantalla 
                modifEmpresa2.geometry("450x600")
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
            barraY.place(x=383, y=0, relheight=0.55)
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
            verEmpresas.geometry("410x400")
            verEmpresas.title("Ver Empresas")
            verEmpresas.iconbitmap("img.ico")
            verEmpresas.config(bg="grey")
            verEmpresas.resizable(0,1)
            ListaEmpresas=tk.Listbox(verEmpresas, width=150)
            ListaEmpresas.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(verEmpresas, command=ListaEmpresas.yview)
            barraY.place(x=393, y=0, relheight=0.55)
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
        nuevoTransporte.geometry("450x600")
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
            print(lineaAborrar)
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
            modifTransporte.geometry("400x400")
            modifTransporte.title("Ver Transportes")
            modifTransporte.iconbitmap("img.ico")
            modifTransporte.config(bg="grey")
            modifTransporte.resizable(0,1)
            def modifCamposTransporte():
                num=int(trp.get())
                Datos=ListaTransportes.get(num)
                print(Datos)
                PlacaVHC=Datos[3:9]
                print(PlacaVHC)
                RestoDeDatos=recopilarDatos(Datos[10:-4])
                print(RestoDeDatos)
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
                modifTransporte2.geometry("450x600")
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
                            f.write(Placa+"|"+tipo+"|"+Nuevamarca+"|"+Nuevomodelo+"|"+nuevoAño+"|"+NuevaEmp+"|"+NuevoVIP+"-"+NuevoNormal+"-"+NuevoEconom+"|"+filas+"\n")
                            g.write(Placa+"|"+NuevoVIP+"|"+NuevoNormal+"|"+NuevoEconom+"|"+filas+"\n")
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
            barraY.place(x=383, y=0, relheight=0.55)
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
            verTransportes.geometry("400x400")
            verTransportes.title("Ver Empresas")
            verTransportes.iconbitmap("img.ico")
            verTransportes.config(bg="grey")
            verTransportes.resizable(0,1)
            ListaTransportes=tk.Listbox(verTransportes, width=150)
            ListaTransportes.config(selectforeground="white",selectbackground="blue", selectborderwidth=3, font=("Sans Serif", 10))
            barraY=tk.Scrollbar(verTransportes, command=ListaTransportes.yview)
            barraY.place(x=383, y=0, relheight=0.55)
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
##    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
##    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
"Pantalla del administrador"
def administrador():
    admin= tk.Toplevel()
    #Porción de código para centrar la ventana a la pantalla 
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
