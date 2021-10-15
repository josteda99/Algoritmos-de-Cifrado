import string
# playfair Cypher


def crearMatriz(cla):
    matriz = []
    for i in range(0, 5):
        a = ['0']*5
        matriz.append(a)

    clave = []
    for i in cla:
        if i not in clave:
            clave.append(i)

    alfabeto = list(string.ascii_lowercase)
    for i in clave:
        alfabeto.remove(i)
    alfabeto.remove('j')

    cont = 0
    i = 0
    for x in range(0, 5):
        for y in range(0, 5):
            if cont < len(clave):
                matriz[x][y] = clave[cont]
                cont += 1
            else:
                matriz[x][y] = alfabeto[i]
                i += 1
    return matriz


def cifrar(men, cla):
    men = men.replace(" ", "")
    cla = cla.replace("j", "i")
    if len(men) % 2 != 0:
        men = men + 'x'

    menEnc = []
    matriz = crearMatriz(cla)

    # primera regla horizontal

    i = 0
    while(i < len(men)):
        indx = indy = indx2 = indy2 = indxe = indye = 0

        for x in range(0, 5):
            for y in range(0, 5):
                if matriz[x][y] == 'x':
                    indxe = x
                    indye = y

        for x in range(0, 5):
            for y in range(0, 5):
                if men[i] == matriz[x][y]:
                    indx = x
                    indy = y

        i += 1
        for x in range(0, 5):
            for y in range(0, 5):
                if men[i] == matriz[x][y]:
                    indx2 = x
                    indy2 = y
                    break

        i += 1
        if indx == indx2 and indy == indy2:
            indx2 = indxe
            indy2 = indye

        if indx == indx2:
            menEnc.append(matriz[indx][(indy+1) % 5])
            menEnc.append(matriz[indx2][(indy2+1) % 5])
        if indy == indy2:
            menEnc.append(matriz[(indx+1) % 5][indy])
            menEnc.append(matriz[(indx2+1) % 5][indy2])
        if indy < indy2 and indx < indx2:
            menEnc.append(matriz[indx][indy2])
            menEnc.append(matriz[indx2][indy])
        if indy > indy2 and indx < indx2:
            menEnc.append(matriz[indx][indy2])
            menEnc.append(matriz[indx2][indy])
        if indy < indy2 and indx > indx2:
            menEnc.append(matriz[indx][indy2])
            menEnc.append(matriz[indx2][indy])
        if indy > indy2 and indx > indx2:
            menEnc.append(matriz[indx][indy2])
            menEnc.append(matriz[indx2][indy])
    menEncr = "".join(menEnc)
    print('Mensaje: ', menEncr)


def descifrar(men, cla):
    men = men.replace(" ", "")
    cla = cla.replace("j", "i")
    if len(men) % 2 != 0:
        men = men + 'x'

    menEnc = []
    matriz = crearMatriz(cla)

    # primera regla horizontal

    i = 0
    while(i < len(men)):
        indx = indy = indx2 = indy2 = indxe = indye = 0

        for x in range(0, 5):
            for y in range(0, 5):
                if matriz[x][y] == 'x':
                    indxe = x
                    indye = y

        for x in range(0, 5):
            for y in range(0, 5):
                if men[i] == matriz[x][y]:
                    indx = x
                    indy = y

        i += 1
        for x in range(0, 5):
            for y in range(0, 5):
                if men[i] == matriz[x][y]:
                    indx2 = x
                    indy2 = y
                    break

        i += 1
        if indx == indx2 and indy == indy2:
            indx2 = indxe
            indy2 = indye

        if indx == indx2:
            menEnc.append(matriz[indx][(indy-1) % 5])
            menEnc.append(matriz[indx2][(indy2-1) % 5])
        if indy == indy2:
            menEnc.append(matriz[(indx-1) % 5][indy])
            menEnc.append(matriz[(indx2-1) % 5][indy2])
        if indy < indy2 and indx < indx2:
            menEnc.append(matriz[indx][indy2])
            menEnc.append(matriz[indx2][indy])
        if indy > indy2 and indx < indx2:
            menEnc.append(matriz[indx][indy2])
            menEnc.append(matriz[indx2][indy])
        if indy < indy2 and indx > indx2:
            menEnc.append(matriz[indx][indy2])
            menEnc.append(matriz[indx2][indy])
        if indy > indy2 and indx > indx2:
            menEnc.append(matriz[indx][indy2])
            menEnc.append(matriz[indx2][indy])
    menEncr = "".join(menEnc)
    print('Mensaje: ', menEncr)


if __name__ == '__main__':
    print('Escoja una opcion:')
    print('1: cifrar')
    print('2: descifrar')
    print('cualquier otra para salir')
    opt = int(input())
    # opt = 2

    if opt == 1:
        print('Introduzca el mensaje a cifrar (minusculas)')
        mensaje = input()
        print('Introduzca la clave (sin espacios)')
        clave = input()
        cifrar(mensaje, clave)
    elif opt == 2:
        print('Introduzca el mensaje a descifrar (minusculas)')
        mensaje2 = input()
        print('Introduzca la clave (sin espacios)')
        clave2 = input()
        descifrar(mensaje2, clave2)
        # descifrar('qtekhb', 'saludos')
    else:
        print('la opcion no existe')
