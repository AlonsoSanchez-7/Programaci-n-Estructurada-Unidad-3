"""
Crear un proyecto que permita gestionar (administrar) peliculas.
Coloca un menu de opciones:Agregar,Borrar,Modificar,mostrar,buscar ,limpiar una lista de peliculas.

Notas:
1- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2-Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas.
3-Utilizar o implemetar BD relacional con MySQL para guardar infromacion 

"""

import funciones
from peliculas import peliculas

opc="1"
caracteristicas={}
while opc!="7":
    funciones.borrarPantalla()
    opc=peliculas.menuPrincipal()
    match opc:
        case "1":
               funciones.borrarPantalla()
               peliculas.agregarPeliculas(caracteristicas)
        case "2":
               funciones.borrarPantalla()
               peliculas.borrarPeliculas(caracteristicas)
        case "3":
               funciones.borrarPantalla()
               peliculas.modificarPeliculas(caracteristicas)
        case "4":
               funciones.borrarPantalla()
               peliculas.mostrarPeliculas(caracteristicas)
        case "5":
               funciones.borrarPantalla()
               peliculas.buscarPeliculas(caracteristicas)
        case "6":
               funciones.borrarPantalla()
               peliculas.limpiarPeliculas(caracteristicas)
        case "7":
               funciones.borrarPantalla()
               funciones.terminarSistema()
        case _:
               funciones.opcionInvalida()