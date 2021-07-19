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
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Eventos de escucha que se encuentran en la interseccion de 2 rangos determinados")
    print("3- Encontrar musica para festejar")
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
        #print(lt.subList(catalog["Eventos"],1,5))
        #print(lt.subList(catalog["Eventos"],lt.size(catalog["Eventos"])-5,5))
        #print(me.getValue(om.get(catalog["liveness"],"0.034")))
        print(mp.size(catalog["Artistas"]))
        #print(me.getValue(mp.get(catalog["Artistas"],"481d88c05dfb1c8709238453bbe14fee")))
        print("Numero de eventos: "+str(lt.size(catalog["Eventos"])))
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
        for i in range(1,9):
            E=lt.getElement(lst,i)
            print("track_id: "+E['track_id'],"liveness: "+E["liveness"],"speechiness: "+E["speechiness"])
    else:
        sys.exit(0)
sys.exit(0)
