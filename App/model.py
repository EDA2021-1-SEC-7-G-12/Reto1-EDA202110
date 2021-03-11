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


import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def NuevoCatalogo():
    catalogo = {
        "videos": None,
        "categorias": None,
    }
    catalogo["videos"] = lt.newList("ARRAY_LIST")
    catalogo["categorias"] = lt.newList("ARRAY_LIST")
    return catalogo

# Funciones para agregar informacion al catalogo


def addVideo(catalogo, video):
    lt.addLast(catalogo["videos"], video)


def addCategoria(catalogo, categoria):
    cat = newCategoria(categoria['id'], categoria['name'])
    lt.addLast(catalogo['categorias'], cat)


# Funciones para creacion de datos

def newCategoria(id, name):
    categoria = {'id': '', 'name': ''}
    categoria['id'] = id
    categoria['name'] = name
    return categoria

# Funciones de consulta


def sacaridcategoria(catalogo, nombre_categoria):
    lista = catalogo["categorias"]
    categoria = -1
    for x in range(lista["size"]):
        elemento = lt.getElement(lista, x)
        if elemento["name"] == nombre_categoria:
            categoria = elemento["id"]
    return categoria

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    return (int(video1["views"]) > int(video2["views"]))


def cmpVideosByLikes(video1, video2):
    return (int(video1["likes"]) > int(video2["likes"]))

def cmpVideosByAppearances(video1, video2):
    return (int(video1["apariciones"]) > int(video2["apariciones"]))
# Funciones de ordenamiento


def sortVideos(catalog, size, country, category_name):
    catalog2 = lt.newList(catalog["videos"]["type"], catalog["videos"]["cmpfunction"])
    idcategoria = sacaridcategoria(catalog, category_name)
    if catalog["videos"]["type"] == "ARRAY_LIST":
        for x in catalog["videos"]["elements"]:
            if (x["category_id"] == idcategoria) and (x["country"] == country):
                lt.addFirst(catalog2, x)
    if catalog2["size"] < size:
        print("Excede el tamaño de la lista, ingrese un valor válido")
    else:
        sub_list = catalog2.copy()
        start_time = time.process_time()
        sorted_list = ms.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list


def sortVideosLikes(catalog, size, tag, pais):
    catalog2 = lt.newList(catalog["videos"]["type"], catalog["videos"]["cmpfunction"])
    if catalog["videos"]["type"] == "ARRAY_LIST":
        for x in catalog["videos"]["elements"]:
            if (tag in x["tags"]) and (x["country"] == pais):
                lt.addFirst(catalog2, x)
    if catalog2["size"] < size:
        print("Excede el tamaño de la lista, ingrese un valor válido")
    else:
        sub_list = catalog2.copy()
        start_time = time.process_time()
        sorted_list = ms.sort(sub_list, cmpVideosByLikes)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list

def videos_a_dias_trending(videos):
    nodiccionario = lt.newList("ARRAY_LIST")
    listaids = []
    for x in videos["elements"]:
        if not x["video_id"] == "#NAME?":
            if not x["video_id"] in listaids:
                listaids.append(x["video_id"])
                lt.addFirst(nodiccionario, {"id" : x["video_id"], "apariciones": 1})
            else:
                for y in nodiccionario["elements"]:
                    if y["id"] == x["video_id"]:
                        y["apariciones"] += 1
    diccionariosorteado = ms.sort(nodiccionario, cmpVideosByAppearances)
    return diccionariosorteado


def topdiastrendingporpais(catalog, pais):
    catalog2 = lt.newList(catalog["videos"]["type"], catalog["videos"]["cmpfunction"])
    if catalog["videos"]["type"] == "ARRAY_LIST":
        for x in catalog["videos"]["elements"]:
            if (pais == x["country"]):
                lt.addFirst(catalog2, x)
    sub_list = catalog2.copy()
    respuesta = None
    sorteado = videos_a_dias_trending(sub_list)
    for x in sub_list["elements"]:
        if x["video_id"] == sorteado["elements"][0]["id"]:
            respuesta = x
    return respuesta , sorteado["elements"][0]["apariciones"]


def topdiastrendingporcateg(catalog, categ):
    catalog2 = lt.newList(catalog["videos"]["type"], catalog["videos"]["cmpfunction"])
    idcategoria = sacaridcategoria(catalog, categ)
    if catalog["videos"]["type"] == "ARRAY_LIST":
        for x in catalog["videos"]["elements"]:
            if (x["category_id"] == idcategoria):
                lt.addFirst(catalog2, x)
    sub_list = catalog2.copy()
    respuesta = None
    sorteado = videos_a_dias_trending(sub_list)
    for x in sub_list["elements"]:
        if x["video_id"] == sorteado["elements"][0]["id"]:
            respuesta = x
    return respuesta , sorteado["elements"][0]["apariciones"]