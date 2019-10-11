from collections import namedtuple
import numpy as np
coordenada = namedtuple('coordenada', ['x', 'y'])
coordenadas = list()
def criar_coordenada(x):
    return coordenada(*list(map(float, x.split())))

with open("numeros.txt") as numfile:
    coordenadas.extend(map(criar_coordenada, numfile.readlines()))

matriz = np.zeros((15, 16), np.float64)
print(matriz)
for i in range(15):
    for j in range(15):

        matriz[i][j] = coordenadas[i].x ** j
    matriz[i][15] = coordenadas[i].y


for i in range(15):
    for j in range(i):
            const = matriz[i][j] / matriz[j][j]
            print(const)
            for k in range(16):
                matriz[i][k] -= const * matriz[j][k]


print(matriz)
np.savetxt("matriz.txt", matriz, '%15.4f')