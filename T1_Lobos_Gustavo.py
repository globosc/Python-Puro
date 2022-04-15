# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:26:12 2020

@author: GLobos
"""
#Mi primer Proyecto en Python
from io import open
with open("p4ds_esi_messy_data.txt", 'r') as fichero:
	p4ds = fichero.read().splitlines()
lineas = [i.replace('**', ' ')for i in(p4ds)]
lectura = []
for i in lineas:
    espacios = i.strip().split()
    lectura.append(espacios)
    #print(espacios)
#### Almacencar el nombre de los cuerpos celestes en listas###
CC0 = ((lectura[3][0])) #Earth
CC1 = ((lectura[4][0])) #Marte
CC2 = ((lectura[5][0])) #Mercury
CC3 = ((lectura[6][0])) #Moon
CC4 = ((lectura[7][0])) #Venus
CC5 = ((lectura[8][0])) #Io
CC6 = ((lectura[9][0])) #Jupiter
CC7 = ((lectura[10][0])) #Titan
CC8 =  "GJ 581 g" #((lectura[11][0:3]))
CC9 = "GJ 581 b" #((lectura[12][0]))
CC10 = "HD 96167 b" #((lectura[13][0]))
CC11 = "WASP-26 b"
#print(CC8)


###Lista de Listas para los Cuerpos Celestes###
CCELESTES = [CC0, CC1, CC2, CC3, CC4, CC5, CC6, CC7, CC8, CC9, CC10, CC11]
DATOS = (lectura[3:15])
###Lineas para facilitar el indexing###
linea0 = (DATOS[0])
linea1 = (DATOS[1])
linea2 = (DATOS[2])
linea3 = (DATOS[3])
linea4 = (DATOS[4])
linea5 = (DATOS[5])
linea6 = (DATOS[6])
linea7 = (DATOS[7])
linea8 = (DATOS[8])
linea9 = (DATOS[9])
linea10 = (DATOS[10])
linea11 = (DATOS[11])

###Lista de listas con las lineas del archivo###
LINEAS1 = [linea0, linea1, linea2, linea3, linea4, linea5, linea6, linea7]
LINEAS2 = [linea8, linea9, linea10]
LINEAS3 = [linea11]


###Identificación de los datos necesarios para hacer los cálculos###
RADIOS = []
for i in LINEAS1:
    radio = (i[2])
    RADIOS.append(radio)
    continue
for i in LINEAS2:
    radio = (i[4])
    RADIOS.append(radio)
    continue
for i in LINEAS3:
    radio = (i[3])
    RADIOS.append(radio)
    continue


DENSIDADES = []
for i in LINEAS1:
    densi = (i[3])
    DENSIDADES.append(densi)
    continue
for i in LINEAS2:
    densi = (i[5])
    DENSIDADES.append(densi)
    continue
for i in LINEAS3:
    densi = (i[4])
    DENSIDADES.append(densi)
    continue


VELOCIDAD = []
for i in LINEAS1:
    velociraptor = (i[5])
    VELOCIDAD.append(velociraptor)
    continue
for i in LINEAS2:
    velociraptor = (i[7])
    VELOCIDAD.append(velociraptor)
    continue
for i in LINEAS3:
    velociraptor = (i[6])
    VELOCIDAD.append(velociraptor)
    continue


TEMPERATURA = []
for i in LINEAS1:
    temp = (i[7])
    TEMPERATURA.append(temp)
    continue
for i in LINEAS2:
    temp = (i[-2])
    TEMPERATURA.append(temp)
    continue
for i in LINEAS3:
    temp = (i[-2])
    TEMPERATURA.append(temp)
    continue

###Convertir las listas anteriores a números float para hacer cálculos###
RADI_CC = [float(i) for i in RADIOS]
DENS_CC = [float(i) for i in DENSIDADES]
VELO_CC = [float(i) for i in VELOCIDAD]
TEMP_CC = [float(i) for i in TEMPERATURA]


#comienzo de calculos matemáticos
### ESI INTERNO ###
radiox = []
def ESI_INTERNO_RADIO (radiox):
    '''Cálculos para el ESI Interno | Parte I (RADIO)\n
    =============================================================\n
    A través de un ciclo for se aplica la fórmula Earth Similarity Index
    interna para sacar los valores de la primera parte de la ecuación (Radio).
    Posterior a esto se guardan los resultados en la lista "radiox".
    Todos los datos ahí almacenados mantienen el orden con el que ingresan
    al ciclo For.
    =============================================================\n'''
    for i in RADI_CC:
        resultado1 = (1-abs((i-1.0)/(i+1.0)))**(0.57 / 2)
        radiox.append(resultado1)
        #print(resultado1)
        continue
    return resultado1
ESI_INTERNO_RADIO(radiox)
#print(radiox)

densidax = []
def ESI_INTERNO_DENSIDAD (densidax):
    '''Cálculos para el ESI Interno | Parte I (DENSIDAD)\n
    =============================================================\n
    A través de un ciclo For se aplica la fórmula Earth Similarity Index
    interna para sacar los valores de la primera parte de la ecuación 
    (Densidad).
    Posterior a esto se guardan los resultados en la lista "densidax".
    Todos los datos ahí almacenados mantienen el orden con el que ingresan
    al ciclo For.
    =============================================================\n'''
    for j in DENS_CC:
        resultado2 = (1-abs((j - 1.0)/(j + 1.0)))**(1.07 / 2)
        densidax.append(resultado2)
        continue
    return resultado2
ESI_INTERNO_DENSIDAD(densidax)
#print(densidax)
ESI_INTERNO_FINAL = [i*j for i, j in zip(radiox, densidax)]


#### ESI SUPERFICIAL ####
velocidax = []
def ESI_SUP_VELOCIDAD (velocidax):
    '''Cálculos para el ESI Superficial | Parte II (VELOCIDAD)\n
    =============================================================\n
    A través de un ciclo for se aplica la fórmula Earth Similarity Index
    interna para sacar los valores de la primera parte de la ecuación 
    (Velocidad).
    Posterior a esto se guardan los resultados en la lista "velocidax".
    Todos los datos ahí almacenados mantienen el orden con el que ingresan
    al ciclo For.
    =============================================================\n'''
    for i in VELO_CC:
        resultado1 = (1-abs((i - 1.0)/(i + 1.0)))**(0.70 / 2)
        velocidax.append(resultado1)
        #print(resultado1)
        continue
    return resultado1
ESI_SUP_VELOCIDAD(velocidax)
#print(radiox)

temperaturax = []
def ESI_SUP_TEMP (temperaturax):
    '''Cálculos para el ESI Superficial | Parte II (TEMPERATURA)\n
    =============================================================\n
    A través de un ciclo for se aplica la fórmula Earth Similarity Index
    interna para sacar los valores de la primera parte de la ecuación 
    (Temperatura).
    Posterior a esto se guardan los resultados en la lista "temperaturax".
    Todos los datos ahí almacenados mantienen el orden con el que ingresan
    al ciclo For.
    =============================================================\n'''
    for j in TEMP_CC:
        resultado2 = (1-abs((j-288.0)/(j+288.0)))**(5.58 / 2)
        temperaturax.append(resultado2)
        continue
    return resultado2
ESI_SUP_TEMP(temperaturax)
#print(densidax)
ESI_SUP_FINAL = [i*j for i, j in zip(temperaturax, velocidax)]
#print(ESI_SUP_FINAL)
ESI_GLOBAL = [(abs(r*d)*abs(v*t)/4) for r, d, v, t in zip(radiox, densidax, 
                                                   velocidax, temperaturax)]



print(ESI_GLOBAL)
print()
#print(ESI_GL2)

########################Intento de calcular de otra manera el ESI_GLB#########
#print(ESI_INTERNO_FINAL)
#print(ESI_SUP_FINAL)
raiz_interna = []
raiz_superior = []
from math import sqrt
for i in ESI_INTERNO_FINAL:
    raiz1 = sqrt(i)
    #print(raiz1)
    raiz_interna.append(raiz1)
    continue
for j in ESI_SUP_FINAL:
    raiz2 = sqrt(j)
    #print(raiz2)
    raiz_superior.append(raiz2)
    continue
ESI_GL2 = [(i*j) for i, j in zip(raiz_interna, raiz_superior)]
#print(ESI_GL_RELOAD)
########################Intento de calcular de otra manera el ESI_GLB#########

#print(CCELESTES)
#print(ESI_INTERNO_FINAL)
#print(ESI_SUP_FINAL)
#print(ESI_GLOBAL) ## Este era el que usabas antes
SIMIL = []
SIMILAR = "SI"
NO_SIMILAR = "NO"
for x in ESI_GL2:
    valor = (float(0.8))
    if x >= valor:
        SIMIL.append(SIMILAR)
    else:
        SIMIL.append(NO_SIMILAR)
    #SIMIL.append(x)
    continue



#INDICES DEL ARCHIVO
t0 = "---"
t1 = "Nombre"
t2 = "ESI_int"
t3 = "ESI_sup"
t4 = "ESI_glb"
t5 = "¿SIMILAR?"
#print(os.__doc__)

def escribir_en_mi_archivo():
    '''Función generada para realizar y ejecutar las siguientes operaciones:\n
    1) Importar el módulo os y el paquete date de módulo datetime.\n
    2) Definir la ruta la de una carpeta exclusiva.\n
    3) Si la carpeta existe, se utilizará esa carpeta, sino una nueva carpeta
    será generada.\n
    ========= =============================================================\n
    ITEM      Descripción\n
    --------- -------------------------------------------------------------\n
    'today'     Guarda las propiedades del tiempo\n
    'carpeta'   Establece el nombre de la carpeta contenedora del archivo
                entregable.
    'archivo'   Define la ruta en donde se generará el archivo entregable\n
    ========= =============================================================\n
    
    El modo por defecto de esta función contempla el uso de format para 
    complementar la salida de cada linea de texto con el propósito de 
    la salida en un formato estructurado en donde la primera fila está
    definida por los títulos de los índices de similaridad.\n
    \n
    \n
    Esta función contempla 2 formas de generar el archivo .txt\n
    
    ###OPCIÓN 1###
    La primera es que al momento de generar el archivo este utiliza todos los
    complementos del método .format expresando la fecha exacta de ejecución.
    
    ###OPCIÓN 2###
    La segunda, es que sólo se utilizan los métodos de 'today.month' y 
    'today.day' para generar el archivo de salida. Esta opción es conveniente
    cuando este script es ejecutado durante el año 2020, si es ejecutado fuera
    de ese año, se recomienda usar la opción 1.
    #############La opción por defecto es la 2################
    '''
    import os
    from datetime import date
    today = date.today()
    carpeta = 'TAREA1_2020'
    #archivo = 'TAREA1_2020\P4DS_T1_{}0{}{}_Lobos_Gustavo.txt'.format(today.year
    #                                                , today.month, today.day)
    
    archivo = 'TAREA1_2020\P4DS_T1_200{}{}_Lobos_Gustavo.txt'.format(
        today.month, today.day)
    
    if not os.path.exists(carpeta): os.makedirs(carpeta)
    archivo=open(archivo, "w")
    #archivo=open('TAREA1_2020\P4DS_T1_YYMMDD_Lobos_Curamil.txt', 'a')
    archivo.write('{:<10} {:^17} {:^17} {:^17} {:^17} \n'.format(t1, t2, 
                                                                 t3, t4, t5))
    archivo.write('{} \n'.format(t0*27))
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC0, ESI_INTERNO_FINAL[0], ESI_SUP_FINAL[0], ESI_GL2[0], SIMIL[0]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC1, ESI_INTERNO_FINAL[1], ESI_SUP_FINAL[1], ESI_GL2[1], SIMIL[1]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC2, ESI_INTERNO_FINAL[2], ESI_SUP_FINAL[2], ESI_GL2[2], SIMIL[2]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC3, ESI_INTERNO_FINAL[3], ESI_SUP_FINAL[3], ESI_GL2[3], SIMIL[3]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC4, ESI_INTERNO_FINAL[4], ESI_SUP_FINAL[4], ESI_GL2[4], SIMIL[4]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC5, ESI_INTERNO_FINAL[5], ESI_SUP_FINAL[5], ESI_GL2[5], SIMIL[5]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC6, ESI_INTERNO_FINAL[6], ESI_SUP_FINAL[6], ESI_GL2[6], SIMIL[6]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC7, ESI_INTERNO_FINAL[7], ESI_SUP_FINAL[7], ESI_GL2[7], SIMIL[7]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC8, ESI_INTERNO_FINAL[8], ESI_SUP_FINAL[8], ESI_GL2[8], SIMIL[8]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
        CC9, ESI_INTERNO_FINAL[9], ESI_SUP_FINAL[9], ESI_GL2[9], SIMIL[9]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
    CC10, ESI_INTERNO_FINAL[10], ESI_SUP_FINAL[10], ESI_GL2[10], SIMIL[10]))
    
    archivo.write("{:<10} {:^17,.3f} {:^17,.3f} {:^17,.3f} {:^17} \n".format(
    CC11, ESI_INTERNO_FINAL[11], ESI_SUP_FINAL[11], ESI_GL2[11], SIMIL[11]))
    
    archivo.close()
escribir_en_mi_archivo()
###Fin del programa##





    





