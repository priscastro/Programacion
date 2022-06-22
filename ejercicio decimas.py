import numpy as np 
from numpy import random

A = np.arange(10) 

for x in range(10):
    aleatorio = random.randint(0,301)
    A[x] = aleatorio
print(A)

B = np.arange(10) 

for x in range(10):
    aleatorio = random.randint(0,301)
    B[x] = aleatorio
print(B)

print(f"La suma total del arreglo A es: {A.sum()}")

print(f"La suma total del arreglo B es: {B.sum()}")

print(f"La suma total de los arreglos es: {A.sum()+B.sum()}")


#print(f"Tabla de multiplicar de los números impares del arreglo B: ")
#busque e intente pero no pude hacer lo de la tabla de multiplicar :(
