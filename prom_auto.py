# -*- coding: utf-8 -*-
#  
#   Telegram: @fedex6
#
#-------------------------------------------------------#3

## Imports
import os
import sys
import time
import glob

## Titulo
print('Promedio (automatico) de TC en GeCom v1.5\n******************************************************\n')

def leer_archivo():
    for nombre_archivo in glob.glob("listas/*.csv"):

        ## Lectura y comprension del Archivo
        archivo = open(nombre_archivo, "r")
        tipo_cambio = 0
        dias_habiles = 0

        for linea in archivo.readlines():
            valores = linea.split(";")

            if valores[1] != '' and valores[1] != 'Cotización':
                tipo_cambio += float(valores[1].replace(",","."))
                dias_habiles += 1

            if valores[3] != '' and valores[3] != 'Cotización':
                tipo_cambio += float(valores[3].replace(",","."))
                dias_habiles += 1

            if valores[5] != '' and valores[5] != 'Cotización':
                tipo_cambio += float(valores[5].replace(",","."))
                dias_habiles += 1

        promedio = float(tipo_cambio) / int(dias_habiles)

        print(' >> Leyendo: '+str(nombre_archivo)+'\n')

        ##Grabar los Datos en el archivo registro
        tc_file = open('resultados/tc_promedios.txt','a')
        tc_file.write('\n'+str(nombre_archivo.replace('listas\\','').replace('.csv',''))+';'+str(round(promedio, 2))+';')
        tc_file.close()

        ## Cerrar Archivo
        archivo.close()

    print('\n******************************************************\nSalir ?: [ s / n ]', end="\n")
    respuesta = input()

    if respuesta == 'y' or respuesta == 's':
      exit()
    else :
      print('Nada mas que hacer, es automatico este...')
      ct = 5
      while ct > 0 :
        print(str(ct)+'...')
        ct -= 1
        time.sleep(1)
      exit()

leer_archivo()