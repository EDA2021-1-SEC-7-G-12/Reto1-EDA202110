"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def NuevoCatalogo(tipo):
    catalogo = {
        "videos": None,
        "categorias": None,
    }
    catalogo["videos"] = lt.newList(tipo)
    catalogo["categorias"] = lt.newList(tipo)
    return catalogo

# Funciones para agregar informacion al catalogo


def addVideo(catalogo, video):
    lt.addLast(catalogo["videos"], video)


def addCategoria(catalogo, categoria):
    cat = newCategoria(categoria['video_id'], categoria['title'])
    lt.addLast(catalogo['categorias'], cat)


# Funciones para creacion de datos

def newCategoria(id, name):
    categoria = {'id': '', 'name': ''}
    categoria['id'] = id
    categoria['name'] = name
    return categoria

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    return (int(video1["views"]) < int(video2["views"]))
# Funciones de ordenamiento

def sortVideos(catalog, size, country, category_name):
    catalog2 = lt.newList(catalog["videos"]["type"],catalog["videos"]["cmpfunction"])
    print(catalog["videos"].keys())
    for x in catalog["videos"]["elements"]:
        if (x["category_name"] == category_name) and (x["country"] == country):
            lt.addFirst(catalog2,x)
    sub_list = lt.subList(catalog2, 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sa.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list