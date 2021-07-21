﻿"""
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
import controller as ctrl
from DISClib.ADT import list as lt
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as mp
assert cf



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Eventos de escucha que se encuentran en la interseccion de 2 rangos determinados")
    print("3- Encontrar musica para festejar")
    print("4- Encontrar musica para una ruptura amorosa")
    print("5- Encontrar canciones y artistas por género")

catalog = None
file="context_content_features-small.csv"

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=ctrl.initialize()
        ctrl.Load_data(catalog,file)
        print("\nNumero de eventos: "+str(lt.size(catalog["Eventos"])))
        print("Numero de artistas: "+str(mp.size(catalog["Artistas"])))
        print("Numero de pistas: "+str(mp.size(catalog["Pistas"])))
        print("\nPrimeros 5 eventos de escucha")
        i=1
        while i<=5:
            evento=lt.getElement(catalog["Eventos"], i)
            print("\nInstrumentalidad: {}, Liveness: {}, Speechiness: {}, Capacidad de Baile: {}, Valencia: {}, Sonoridad: {}, Tempo: {}, Acústica: {}, Energía: {}, Modo: {}, Clave: {}, Idioma del Tweet: {}, Fecha de creación: {}, Idioma del usuario: {}, Zona horaria: {}".format(evento['instrumentalness'], evento['liveness'], evento['speechiness'], evento['danceability'], evento['valence'], evento['loudness'], evento['tempo'],evento['acousticness'], evento['energy'], evento['mode'], evento['key'], evento['tweet_lang'], evento['created_at'], evento['lang'], evento['time_zone']))
            i+=1
        print("\nÚltimos 5 eventos de escucha")
        i=1
        while i<=5:
            evento=lt.getElement(catalog["Eventos"], -i)
            print("\nInstrumentalidad: {}, Liveness: {}, Speechiness: {}, Capacidad de Baile: {}, Valencia: {}, Sonoridad: {}, Tempo: {}, Acústica: {}, Energía: {}, Modo: {}, Clave: {}, Idioma del Tweet: {}, Fecha de creación: {}, Idioma del usuario: {}, Zona horaria: {}".format(evento['instrumentalness'], evento['liveness'], evento['speechiness'], evento['danceability'], evento['valence'], evento['loudness'], evento['tempo'],evento['acousticness'], evento['energy'], evento['mode'], evento['key'], evento['tweet_lang'], evento['created_at'], evento['lang'], evento['time_zone']))
            i+=1

    elif int(inputs[0]) == 2:
        char1=input("Caracteristica 1: ")
        min1=(input("Minimo: "))
        max1=(input("Maximo: "))
        char2=input("Caracteristica 2: ")
        min2=(input("Minimo: "))
        max2=(input("Maximo: "))
        res=ctrl.Characterize_reps(char1,min1,max1,char2,min2,max2,catalog)
        print("Total de eventos de escucha: "+str(res[1]))
        print("Total autores: "+str(res[0]))

    elif int(inputs[0]) == 3:
        minl=input("Vivacidad minima: ")
        maxl=input("Vivacidad maxima: ")
        mins=input("Habla minima: ")
        maxs=input("Habla maxima: ")
        res=ctrl.Encontrar_musica_festejar(minl,mins,maxl,maxs,catalog)
        print("Numero de pistas: "+str(res[0]))
        lst=res[1]
        for i in range(lt.size(lst)):
            E=lt.getElement(lst,i)
            print("Track {}: ".format(i)+E['track_id'],"with liveness of: "+E["liveness"],"and speechiness of: "+E["speechiness"])

    elif int(inputs[0]) == 4:
        minv=input("Valencia minima: ")
        maxv=input("Valencia maxima: ")
        mint=input("Tempo minimo: ")
        maxt=input("Tempo maximo: ")
        res=ctrl.Encontrar_musica_ruptura(minv,mint,maxv,maxt,catalog)
        print("Numero de pistas: "+str(res[0]))
        lst=res[1]
        for i in range(lt.size(lst)):
            E=lt.getElement(lst,i)
            print("Track {}: ".format(i)+E['track_id'],"with valence of: "+E["valence"],"and tempo of: "+E["tempo"])
    
    else:
        sys.exit(0)
sys.exit(0)
