# -*- coding: utf-8 -*-
# 
#   Telegram: @fedex6
#
#-------------------------------------------------------#3

## Imports
import os
import sys

print('Promedio de TC en GeCom v0.8\n******************************************************\n')

def leer_archivo():
    ## Que archivo hay que leer ?
    print('Como se llama el archivo ? (con la extencion)', end="\n")
    nombre_archivo = input()

    ## Lectura y comprension del Archivo
    archivo = open(nombre_archivo, "r")
    tipo_cambio = 0
    dias_habiles = 0

    for linea in archivo.readlines():
      #for linea > 2:
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

    print('***************************\n >> Leyendo: '+str(nombre_archivo)+'\n')
    print('  Dias Habiles del mes: ' + str(dias_habiles) + '\n' + '  Tipo de Cambio Promedio: $' + str(round(promedio, 2)) )

    tc_file = open('tc_promedios.txt','a')
    tc_file.write('\n'+str(nombre_archivo.replace('.csv',''))+';'+str(round(promedio, 2))+';')
    tc_file.close()

    ## Cerrar Archivo
    archivo.close()

    print('\n***************************\nSalir ?: [ s / n ]', end="\n")
    respuesta = input()

    if respuesta == 'y' or respuesta == 's':
      exit()
    else :
      leer_archivo()

leer_archivo()