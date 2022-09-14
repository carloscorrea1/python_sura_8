from distutils.text_file import TextFile
from traceback import print_tb
import pandas as pd

##cargar los datos
## crear variable

dataFrame=pd.read_csv('./empleados (1).csv')
#print(dataFrame)

## cargar todos los datos

#print(dataFrame.to_string())

## cargar los primeros n registro de un bando de datos

#print(dataFrame.head(20))

##cargar los ultimos n registros
#print(dataFrame.tail())
## Cargar informaciomn
##print(dataFrame.info())
## estadistica descriptiva
#print(dataFrame.describe())
##combianciom
##print(dataFrame["nombres"].head())
##print(dataFrame["salario"].tail())
## registros por subindice
##print(dataFrame.iloc[20:30])
##print(dataFrame.loc[[20,20,30,40]])
#tabla=(dataFrame.loc[[1,5,10],["nombres"]])
'''
abla.to_html()
text_file=open("index.html","w")
text_file.write(html)
text_file.close()
'''
##filtros con condicones logicas
##print(dataFrame[dataFrame["salario"]>5500000].head(10))

print(dataFrame[(dataFrame["salario"]>5500000) & (dataFrame["cargo"]=="analista2")])





