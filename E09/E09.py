from collections import namedtuple
import numpy as np
coordenada = namedtuple('coordenada', ['x', 'y'])
coordenadas = list()
def criar_coordenada(x):
    return coordenada(*list(map(float, x.split())))

with open("numeros.txt") as numfile:
    coordenadas.extend(map(criar_coordenada, numfile.readlines()))

matriz = np.zeros((15, 16), np.float64)
for i in range(15):
    for j in range(15):
        matriz[i][j] = 1
        for k in range(15):
            if k != j:
                matriz[i][j] *= (coordenadas[i].x - coordenadas[k].x)
    matriz[i][15] = coordenadas[i].y


for i in range(15):
    for j in range(i):
            const = matriz[i][j] / matriz[j][j]
            for k in range(16):
                matriz[i][k] -= const * matriz[j][k]


for i in range(14, -1, -1):
    matriz[i][15] /= matriz[i][i]
    for j in range(i):
        matriz[j][i] *= matriz[i][15]
        matriz[j][15] -= matriz[j][i]
        
for i in range(15):
    print(f"a{i:2.0f} = {matriz[i][15]:20.15f}")

np.savetxt("matriz.txt", matriz, '%30.15f')