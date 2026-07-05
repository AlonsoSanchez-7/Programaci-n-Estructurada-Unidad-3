import funciones
    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(caracteristicas):
    print("\t\t....:::: AGREGAR CARACTERISTICA A UNA PELICULA ::::...\n")
    caracteristica=input("Ingresa la caracteristicas: ").upper().strip()
    caracteristicas[caracteristica] = True
    funciones.accionExitosa()
    
def mostrarPeliculas(caracteristicas):
    print("\t\t....:::: MOSTRAR  CARACTERISTICA DE LA PELICULA ::::...\n")
    if len (caracteristicas)>0:
        print("\tCaracteristica\t\tvalor")
        for i in caracteristicas:
            print(f"\t{i}\t\t{caracteristicas[i]}")
    funciones.espereTecla()
   
def limpiarPeliculas(caracteristicas):
     print("\t\t....:::: BORRRAS TODAS  CARATERISTICAS DE LA PELICULAS ::::...\n") 
     if len(caracteristicas)>0:
         opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
         while opc!="si" and opc!="no":
             opc=input("¿Deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
         if opc=="si":
             caracteristicas.clear()
             funciones.accionExitosa()
     else:
         input("\n\t...¡No existen peliculas que borrar, verifique! ....")
    
def buscarPeliculas(caracteristicas):
    print("\t\t....:::: BUSCAR CARACTERISCA DE LA PELICULA ::::...\n")   
    caracterisca=input("Escribe la caracterisca de la pelicula: ").upper().strip()
    print("\tcaracteristica\t\tvalor")
    noencroto=False
    for i in caracteristicas:
      if caracterisca==i:
        print(f"\t{i}\t\t{caracteristicas[i]}")
        noencroto=True
    funciones.espereTecla()
    if not(noencroto):
       input("\n\t...¡NO existe esta carateristica no exitec")


def borrarPeliculas(caracteristicas):
    posiciones=[]
    print("\t\t....:::: BORRAR  CARACTERISTICA PELICULAS ::::...\n")   
    caracteristica_input=input("Escribe el nombre de la Caracteristicas: ").upper().strip()
    noencontro=False
    for i in list(caracteristicas.keys()):
     if caracteristica_input==i:
      opc=""
      while opc!="si" and opc!="no":
        opc=input("¿Deseas borrar la caracteristicas (Si/No)? ").lower().strip()
      if opc=="si":
        caracteristicas.pop(i)
        funciones.accionExitosa()
        noencontro=False
    if noencontro:
      input("\n\t...¡No existe la pelicula que andas buscando!...")

def modificarPeliculas(caracteristicas):
    print("\t\t....:::: MODIFICAR LAS CARACTERISTICAS PELICULAS ::::...\n")   
    caracteristica=input("Escribe el nombre de la  Caracteristicas: ").upper().strip()
    noencontro=True
    if caracteristica in caracteristicas:
              opc=""
              while opc!="si" and opc!="no":
                opc=input("¿Deseas mofificar la caracteriscas (Si/No)? ").lower().strip()
              if opc=="si":
                caracteristicas[caracteristica]=input("Escribe el nuevo nombre: ").upper().strip()
                funciones.accionExitosa()
                noencontro=False
    if noencontro:
        input("\n\t...¡No existe la caracteriscas andas buscando!...")
 

def buscarpeliculas2(caracteristicas):
    print("\t\t....::::buscar caracteristicas de la peliculas ::::....\n")
    caracteriscas=input("Escribe el nombre de la caracteristica: "). upper().strip()
    
    noencontro=True
    for i in caracteristicas:
     if caracteriscas==i:
      print("\tcaracteristica\t\tvalor")
      print(f"\t{i}\t\{caracteristicas[i]}")
      noencontro=False
     funciones.espereTecla()
    if noencontro:
       input("\n\t...¡NO existe esta caracterisca que andas buscando!...")