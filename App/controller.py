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
def initialize():
    return model.newCatalog()
    
# Funciones para la carga de datos
def Load_data(catalog,file):
    file = cf.data_dir + file
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for evento in input_file:
        model.AddEvento(evento,catalog)
    return catalog

def Traducir_caracteristica(num):
    return model.Traducir_caracteristica(num)

def Characterize_reps(char1,min_1,max_1,char2,min_2,max_2,catalog):
    return model.Characterize_reps(char1,min_1,max_1,char2,min_2,max_2,catalog)

def Encontrar_musica_festejar(minl,mins,maxl,maxs,catalog):
    return model.Encontrar_musica_festejar(minl,mins,maxl,maxs,catalog)

def Encontrar_musica_ruptura(minv,mint,maxv,maxt,catalog):
    return model.Encontrar_musica_ruptura(minv,mint,maxv,maxt,catalog)

def Traducir_generos(lista):
    return model.Traducir_generos(lista)

def rep_artistas_por_genero(nombre, min, max, catalog):
    return model.rep_artistas_por_genero(nombre, min, max, catalog)
    

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
