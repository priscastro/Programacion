from array import array
import numpy as np
from numpy import random

vocales = 0
consonantes = 0

matriz = np.array([["t","m","i","o"],['p','r','f','e'],['k','a','i','x'],['s','j','o','n']])

print(matriz)


for x in range(4):
    for y in range(4):
        if (matriz[x][y] == "a" or matriz[x][y] == "e" or matriz[x][y] =="i" or matriz[x][y] =="o" or matriz[x][y] =="u"):
            vocales = vocales + 1


        
print(f"La cantidad de vocales es: {vocales}")
