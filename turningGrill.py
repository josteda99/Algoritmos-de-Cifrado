import string
import numpy as np

# methods from user9402118


def ruota_orario(matrix):
    ruota = list(zip(*reversed(matrix)))
    return[list(elemento) for elemento in ruota]


def ruota_antiorario(matrix):
    ruota = list(zip(*reversed(matrix)))
    return[list(elemento)[::-1] for elemento in ruota][::-1]


def crearMatriz(n):
    matriz = []
    for i in range(0, n):
        a = ['o']*n
        matriz.append(a)
    return matriz


def crearAgujeros(grilla, grillaAgujeros, n):
    aux = 0
    k = 0
    for i in range(n):
        for j in range(n):
            if aux == grilla[k]:
                if k < len(grilla)-1:
                    k += 1
                grillaAgujeros[i][j] = 'X'
            aux += 1
    return grillaAgujeros


def cifrar(men, grilla, n, optRot):
    matriz = crearMatriz(n)
    aux = 0
    for k in range(4):
        for i in range(n):
            for j in range(n):
                if grilla[i][j] == 'X':
                    matriz[i][j] = men[aux]
                    if aux < len(men)-1:
                        aux += 1
        if optRot == 1:
            grilla = ruota_orario(grilla)
        if optRot == 2:
            grilla = ruota_antiorario(grilla)
    mensaje = ''
    for i in range(n):
        for j in range(n):
            mensaje += matriz[i][j]
        mensaje += ' '
    print(mensaje)


def descifrar(men, grilla, n, optRot):
    temp = crearMatriz(n)
    k = 0
    for i in range(n):
        for j in range(n):
            temp[i][j] = men[k]
            k += 1
    mensaje = []
    aux = 0
    for k in range(4):
        for i in range(n):
            for j in range(n):
                if grilla[i][j] == 'X':
                    mensaje.append(temp[i][j])
        if optRot == 1:
            grilla = ruota_orario(grilla)
        if optRot == 2:
            grilla = ruota_antiorario(grilla)
    menBloque = ''
    cont = 0
    for i in range(len(mensaje)):
        if cont < nAgujeros-1:
            menBloque += mensaje[i]
            cont += 1
        else:
            menBloque += mensaje[i]
            menBloque += ' '
            cont = 0
    print(menBloque)


if __name__ == '__main__':
    n = int(input("introduzca tamaño se la reticula: "))
    optRot = int(
        input("1: rotacion hacia derecha - 2: rotacion hacia izquierda: "))
    nAgujeros = int(input("introduzca el numero de agujeros: "))
    grilla = []
    print("introduza posicion (empieza desde 0)")
    for i in range(nAgujeros):
        grilla.append(int(input("posicion: ")))
    grilla.sort()
    grillaAgujeros = crearMatriz(n)
    grillaAgujeros = crearAgujeros(grilla, grillaAgujeros, n)
    mensaje = input(
        'introduzca el mensaje sin espacios: ')
    print('Escoja una opcion:')
    print('1: cifrar')
    print('2: descifrar')
    print('cualquier otra para salir')
    opt = int(input())
    if opt == 1:
        cifrar(mensaje, grillaAgujeros, n, optRot)
    else:
        descifrar(mensaje, grillaAgujeros, n, optRot)
