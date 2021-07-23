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
    print("5- Encontrar número de canciones y artistas por género")

def printCaracteristicas():
    print("\nCaracteristicas")
    print("1- Instrumentalness")
    print("2- Liveness")
    print("3- Speechiness")
    print("4- Danceability")
    print("5- Valence")
    print("6- Loudness")
    print("7- Tempo")
    print("8- Acousticness")
    print("9- Energy")

def printGeneros():
    print("\nGeneros")
    print("1- Reggae ")
    print("2- Down-Tempo")
    print("3- Chill-out")
    print("4- Hip-hop")
    print("5- Jazz and Funk")
    print("6- Pop")
    print("7- R&B")
    print("8- Rock")
    print("9- Metal")
    print("10- Agregar género")


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
        print("Numero de artistas únicos: "+str(mp.size(catalog["Artistas"])))
        print("Numero de pistas únicas: "+str(mp.size(catalog["Pistas"])))
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
        printCaracteristicas()
        char1=input("Seleccione el número de la característica 1: ")
        min1=(input("Minimo: "))
        max1=(input("Maximo: "))
        char2=input("Seleccione el número de la caracteristica 2: ")
        min2=(input("Minimo: "))
        max2=(input("Maximo: "))
        res=ctrl.Characterize_reps(ctrl.Traducir_caracteristica(int(char1)),float(min1),float(max1),ctrl.Traducir_caracteristica(int(char2)),float(min2), float(max2),catalog)
        print("Total de eventos de escucha: "+str(res[1]))
        print("Total autores únicos: "+str(res[0]))

    elif int(inputs[0]) == 3:
        minl=input("Vivacidad minima: ")
        maxl=input("Vivacidad maxima: ")
        mins=input("Habla minima: ")
        maxs=input("Habla maxima: ")
        res=ctrl.Encontrar_musica_festejar(float(minl),float(mins),float(maxl),float(maxs),catalog)
        print("Numero de pistas: "+str(res[0]))
        lst=res[1]
        for i in range(1, lt.size(lst)+1):
            E=lt.getElement(lst,i)
            print("Track {}: ".format(i)+E['track_id'],"with liveness of: "+E["liveness"],"and speechiness of: "+E["speechiness"])

    elif int(inputs[0]) == 4:
        minv=input("Valencia minima: ")
        maxv=input("Valencia maxima: ")
        mint=input("Tempo minimo: ")
        maxt=input("Tempo maximo: ")
        res=ctrl.Encontrar_musica_ruptura(float(minv),float(mint),float(maxv),float(maxt),catalog)
        print("Numero de pistas: "+str(res[0]))
        lst=res[1]
        for i in range(1, lt.size(lst)+1):
            E=lt.getElement(lst,i)
            print("Track {}: ".format(i)+E['track_id'],"with valence of: "+E["valence"],"and tempo of: "+E["tempo"])

    elif int(inputs[0]) == 5:
        printGeneros()
        lst=[]
        n = int(input("Cuántos géneros desea consultar: "))
        for i in range(0, n):
            ele = int(input("Inserte el número de género que desea: "))
            lst.append(ele)
        generos=ctrl.Traducir_generos(lst)
        print("\nTotal of reproductions: {}".format(lt.size(catalog["Eventos"])))
        for genero in generos:
            res=ctrl.rep_artistas_por_genero(genero[0], genero[1], genero[2], catalog)
            print("\nFor {} the tempo is between {} and {} BPM".format(res[0], res[1], res[2]))
            print("{} reproductions: {} with {} different artist".format(res[0], res[4], res[3]))
            print("-----Some artists for {} -----".format(res[0]))
            lst=res[5]
            for i in range(1,lt.size(lst)+1):
                E=lt.getElement(lst,i)
                print("Artist {}: ".format(i)+E['artist_id'])
              
    else:
        sys.exit(0)
sys.exit(0)