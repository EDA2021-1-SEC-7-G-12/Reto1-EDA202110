﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def initCatalog(tipo):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.NuevoCatalogo(tipo)
    return catalog


def loadData(catalogo):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalogo)
    loadCategorias(catalogo)


def loadVideos(catalogo):
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalogo, video)


def loadCategorias(catalogo):
    categoriasfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoriasfile, encoding='utf-8'))
    for categoria in input_file:
        model.addCategoria(catalogo, categoria)
# Funciones para la carga de datos

# Funciones de ordenamiento
def sortVideos(catalog, size, country, category_name, tiposort):
    return model.sortVideos(catalog, size, country, category_name, tiposort)

def sortVideosTest(catalog, size, tiposort):
    return model.sortVideosTest(catalog, size, tiposort)
# Funciones de consulta sobre el catálogo
