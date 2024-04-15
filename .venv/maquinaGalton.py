#maquina de Galton simula una campana de Gauss

#Se añaden las librerias necesarias
from collections import Counter
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import random
#Cantidad de eventos a suce
# der
canicas = 3000
peldaños = []
resultados = []
while canicas > 0:
    x = 0

    #Aqui se genera un numero aleatorio generando una lista con ellos
    if peldaños == []:
        #randint es para generar numeros enteros dentro de un interbalo
        #random es para generar floats entre 0 y 1
        peldaños = [random.randint(0,1) for _ in range(12)]
        
        for i in peldaños:
            if i == 1:
                x = x + 1
            else:
                x = x-1
                
        resultados.append(x)
        canicas = canicas - 1
    else:
        peldaños = []

mapaResultados = {}

#Se cuenta el numero de de frecuencia de cada valor 
mapaResultados = Counter(resultados)
#ordenar el resultado de menor a mayor
for valor in sorted(mapaResultados):
    print(f'{valor}: {mapaResultados[valor]}')  
#----------------------------------------------------------------
#Graficar con la libreria matplotlib

#Se calcula los extremos de los intervalos
casillas = range(min(resultados), max(resultados), + 2)

#creamos el gráfico en Seaborn
#sb.displot(resultados, color='#006400', bins=casillas, kde=True)
#Se configuran los componentes visuales
plt.hist(x= resultados, bins= casillas, color='#006400', rwidth= 0.85)
plt.title('Grafica de maquina de Galton')
plt.xlabel('Casillas')
plt.ylabel('Frecuencia')
plt.xticks(casillas)

plt.show()
