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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'Eventos': None,
                'Artistas': None,
                'Pistas': None,
                'instrumentalness':None,
                'liveness':None,
                'speechiness':None,
                'acousticness':None,
                'energy':None,
                'valence':None,
                'danceability':None,
                'tempo':None,
                'loudness':None
                }

    catalog['Eventos'] = lt.newList('ARRAY_LIST')
    catalog['Artistas'] = mp.newMap(numelements=200,
           prime=109345121,
           maptype='PROBING',
           loadfactor=0.5,
           comparefunction=None)
    catalog['Pistas'] = mp.newMap(numelements=1000,
           prime=109345121,
           maptype='PROBING',
           loadfactor=0.5,
           comparefunction=None)
    catalog['instrumentalness']=om.newMap("RBT")
    catalog['liveness']=om.newMap("RBT")
    catalog['speechiness']=om.newMap("RBT")
    catalog['acousticness']=om.newMap("RBT")
    catalog['energy']=om.newMap("RBT")
    catalog['danceability']=om.newMap("RBT")
    catalog['valence']=om.newMap("RBT")
    catalog['tempo']=om.newMap("RBT")
    catalog['loudness']=om.newMap("RBT")
    return catalog
    
# Funciones para agregar informacion al catalogo
def AddEvento(evento,catalog):
    lt.addLast(catalog['Eventos'],evento)
    mapping_artista(evento,catalog)
    mapping_pista(evento, catalog)
    Order_instrumentalness(evento,catalog)
    Order_liveness(evento,catalog)
    Order_acousticness(evento,catalog)
    Order_danceability(evento,catalog)
    Order_energy(evento,catalog)
    Order_speechiness(evento,catalog)
    Order_valence(evento,catalog)
    Order_loudness(evento,catalog)
    Order_tempo(evento, catalog)
    return catalog

def mapping_artista(evento,catalog):
    if mp.contains(catalog['Artistas'],evento["artist_id"]):
        lista=me.getValue(mp.get(catalog['Artistas'],evento["artist_id"]))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        mp.put(catalog['Artistas'],evento["artist_id"],lista)


def mapping_pista(evento,catalog):
    if mp.contains(catalog['Pistas'],evento["track_id"]):
        lista=me.getValue(mp.get(catalog['Pistas'],evento["track_id"]))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        mp.put(catalog['Pistas'],evento["track_id"],lista)

def Order_instrumentalness(evento,catalog):
    instrumentalidad=float(evento["instrumentalness"])
    if om.contains(catalog['instrumentalness'],instrumentalidad):
        lista=me.getValue(om.get(catalog['instrumentalness'],instrumentalidad))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['instrumentalness'],instrumentalidad,lista)

def Order_speechiness(evento,catalog):
    speechiness=float(evento["speechiness"])
    if om.contains(catalog['speechiness'],speechiness):
        lista=me.getValue(om.get(catalog['speechiness'],speechiness))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['speechiness'],speechiness,lista)

def Order_liveness(evento,catalog):
    liveness=float(evento["liveness"])
    if om.contains(catalog['liveness'],liveness):
        lista=me.getValue(om.get(catalog['liveness'],liveness))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['liveness'],liveness,lista)

def Order_acousticness(evento,catalog):
    acustica=float(evento["acousticness"])
    if om.contains(catalog['acousticness'],acustica):
        lista=me.getValue(om.get(catalog['acousticness'],acustica))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['acousticness'],acustica,lista)

def Order_energy(evento,catalog):
    energia=float(evento["energy"])
    if om.contains(catalog['energy'], energia):
        lista=me.getValue(om.get(catalog['energy'], energia))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['energy'], energia,lista)

def Order_valence(evento,catalog):
    valencia=float(evento["valence"])
    if om.contains(catalog['valence'], valencia):
        lista=me.getValue(om.get(catalog['valence'], valencia))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['valence'], valencia,lista)

def Order_danceability(evento,catalog):
    danceability=float(evento["danceability"])
    if om.contains(catalog['danceability'], danceability):
        lista=me.getValue(om.get(catalog['danceability'], danceability))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['danceability'], danceability,lista)

def Order_tempo(evento,catalog):
    tempo=float(evento["tempo"])
    if om.contains(catalog['tempo'], tempo):
        lista=me.getValue(om.get(catalog['tempo'], tempo))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['tempo'], tempo, lista)

def Order_loudness(evento,catalog):
    loudness=float(evento["loudness"])
    if om.contains(catalog['loudness'], loudness):
        lista=me.getValue(om.get(catalog['loudness'], loudness))
        lt.addLast(lista,evento)
    else:
        lista=lt.newList("ARRAY_LIST")
        lt.addLast(lista,evento)
        om.put(catalog['loudness'], loudness,lista)


#Falta hacer los otros mapas que ordenan por propiedad

# Funciones para creacion de datos

# Funciones de consulta
def Characterize_reps(char1:str,min_1:float,max_1:float,char2:str,min_2:float,max_2:float,catalog)->tuple:
    listas_1=om.values(catalog[char1],min_1,max_1)
    eventos_n=0
    artistas=lt.newList("ARRAY_LIST")
    for i in lt.iterator(listas_1):
        for j in lt.iterator(i):
            if float(j[char2])<=max_2 and float(j[char2])>=min_2:
                eventos_n+=1
                if not(lt.isPresent(artistas,j["artist_id"])):
                    lt.addLast(artistas,j["artist_id"])
    return lt.size(artistas),eventos_n

def Encontrar_musica_festejar(minl,mins,maxl,maxs,catalog):
    mapa=mp.newMap(numelements=100000,maptype="PROBING")
    listas_1=om.values(catalog['liveness'],minl,maxl)
    for i in lt.iterator(listas_1):
        for j in lt.iterator(i):
            if float(j["speechiness"])<=maxs and float(j["speechiness"])>=mins and not(mp.contains(mapa,j['track_id'])):
                mp.put(mapa,j['track_id'],j)
    if mp.size(mapa)>8:
       return mp.size(mapa),lt.subList(mp.valueSet(mapa),1,8)
    else: 
        return mp.size(mapa), mp.valueSet(mapa)

def Encontrar_musica_ruptura(minv:str,mint:str,maxv:str,maxt:str,catalog):
    mapa=mp.newMap(numelements=100000,maptype="PROBING")
    lista_v=om.values(catalog['valence'],minv,maxv)
    for i in lt.iterator(lista_v):
        for j in lt.iterator(i):
            if float(j["tempo"])<=maxt and float(j["tempo"])>=mint and not(mp.contains(mapa,j['track_id'])):
                mp.put(mapa,j['track_id'],j)
    if mp.size(mapa)>8:
       return mp.size(mapa),lt.subList(mp.valueSet(mapa),1,8)
    else: 
        return mp.size(mapa), mp.valueSet(mapa)

def Traducir_caracteristica(num:int):
    caracteristica=None
    if num==1:
        caracteristica="instrumentalness"
    elif num==2:
        caracteristica="liveness"
    elif num==3:
        caracteristica="speechiness"
    elif num==4:
        caracteristica="danceability"
    elif num==5:
        caracteristica="valence"
    elif num==6:
        caracteristica="loudness"
    elif num==7:
        caracteristica="tempo"
    elif num==8:
        caracteristica="energy"
    return caracteristica

def Traducir_generos(lista:list):
    generos=lt.newList("ARRAY_LIST")
    for numero in lista:
        if numero==1:
            name="Reggae"
            min=60
            max=90
        elif numero==2:
            name="Down-Tempo"
            min=70
            max=100
        elif numero==3:
            name="Chill-Out"
            min=90
            max=120
        elif numero==4:
            name="Hip-Hop"
            min=85
            max=115
        elif numero==5:
            name="Jazz and Funk"
            min=120
            max=125
        elif numero==6:
            name="Pop"
            min=100
            max=130
        elif numero==7:
            name="R&B"
            min=60
            max=80
        elif numero==8:
            name="Rock"
            min=110
            max=140
        elif numero==9:
            name="Metal"
            min=100
            max=160
        elif numero==10:
            name=input("Escriba el nombre del nuevo género: ")
            min=int(input("Escriba el tempo mínimo: "))
            max=int(input("Escriba el tempo máximo: "))
        lt.addLast(generos,(name, min, max))
    return lt.iterator(generos)

def rep_artistas_por_genero(nombre, min, max, catalog):
    listas_t=om.values(catalog['tempo'],min,max)
    artistas=mp.newMap(numelements=100000,maptype="PROBING")
    eventos=mp.newMap(numelements=100000,maptype="PROBING")
    for i in lt.iterator(listas_t):
        for j in lt.iterator(i):
            if not(mp.contains(artistas,j['artist_id'])):
                    mp.put(artistas,j['artist_id'],j)
            if not(mp.contains(eventos, j['track_id'])):
                    mp.put(eventos, j['track_id'], j)
    if mp.size(artistas)>=10:
        map_artistas=lt.subList(mp.valueSet(artistas),1,10)
    else:
        map_artistas=mp.valueSet(artistas)
    return nombre, min, max, mp.size(artistas), mp.size(eventos), map_artistas



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento