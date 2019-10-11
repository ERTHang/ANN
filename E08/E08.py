from collections import namedtuple
import numpy as np
coordenada = namedtuple('coordenada', ['x', 'y'])
coordenadas = list()
def criar_coordenada(x):
    return coordenada(*list(map(float, x.split())))

with open("numeros.txt") as numfile:
    coordenadas.extend(map(criar_coordenada, numfile.readlines()))

matriz = np.zeros((21, 22), np.float64)
for i in range(21):
    for j in range(21):
        matriz[i][j] = 1
        for k in range(j):
            matriz[i][j] *= (coordenadas[i].x - coordenadas[k].x)
    matriz[i][21] = coordenadas[i].y


for i in range(21):
    for j in range(i):
            const = matriz[i][j] / matriz[j][j]
            for k in range(22):
                matriz[i][k] -= const * matriz[j][k]


for i in range(20, -1, -1):
    matriz[i][21] /= matriz[i][i]
    for j in range(i):
        matriz[j][i] *= matriz[i][21]
        matriz[j][21] -= matriz[j][i]
        
for i in range(21):
    print(f"a{i:2.0f} = {matriz[i][21]:20.15f}")

np.savetxt("matriz.txt", matriz, '%30.15f')