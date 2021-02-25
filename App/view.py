"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
# Hola

def printResults(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son:")
        i=1
        while i <= sample:
            video = lt.getElement(ord_videos,i)
            print('Trending date: ' + video['trending_date'] + ' Title: ' +
                video['title'] + ' Channel title: ' + video['channel_title']
                + ' Publish time: ' + video['publish_time'] + ' Views: ' + video['views'] 
                + ' Likes: ' + video['likes'] + ' Dislikes: ' + video['dislikes'])
            i+=1

def printMenu():
    print("Bienvenido")
    print("1- Cargar datos de videos")
    print("2- Consultar los videos con más visitas en una categoría y país específicos")
    print("3- Consultar el video que ha sido trending más días en un país específico")
    print("4- Consultar el video que ha sido trending más días en una categoría específica")
    print("5- Consultar los videos con más likes en un país y tag específicos")
    print("0- Salir de la aplicacion")


def loadData(catalog):
    controller.loadData(catalog)


def initCatalog(tipo):
    return controller.initCatalog(tipo)


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo = input("Escoja el tipo de representación de la lista (ARRAY_LIST o LINKED_LIST): ")
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))

    elif int(inputs[0]) == 2:
        # Por completar
        categ = input("Escriba una categoría: ")
        pais = input("Escriba un país: ")
        size = input("Indique tamaño de la muestra: ")
        print("Sorteando videos ....")
        result = controller.sortVideos(catalog, int(size), pais, categ)
        if not (result==None):
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0]))
            printResults(result[1])

    elif int(inputs[0]) == 3:
        # Por completar
        pais = input("Escriba un país: ")
        print("Cargando información del video ....")

    elif int(inputs[0]) == 4:
        # Por completar
        categ = input("Escriba una categoría: ")
        print("Cargando información del video ....")

    elif int(inputs[0]) == 5:
        # Por completar
        tag = input("Escriba un tag: ")
        pais = input("Escriba un país: ")
        print("Cargando información de los videos ....")

    else:
        sys.exit(0)
sys.exit(0)
