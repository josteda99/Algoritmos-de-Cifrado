
import base64
import numpy as np
from io import BytesIO
from PIL import Image
import PIL
import requests
from pyDes import *


# abrir imagen
with open("Criptografia/Algoritmos-de-Cifrado/DES/img.png", "rb") as image2string:
    # base64
    converted_string = base64.b64encode(image2string.read())
    if len(converted_string) % 8 != 0:
        for i in range(len(converted_string) % 8):
            converted_string += converted_string[0:1]


def desEncryptAndDesEncrypt():

    # llave
    k = des("ABEJONES", CBC, "\0\0\0\0\0\0\0\0")
    data = converted_string
    print("Key      : %r" % k.getKey())
    print("Data     : %r" % data)

    # encriptar
    d = k.encrypt(data)
    print("Encrypted: %r" % d)

    # desencriptar
    d = k.decrypt(d)
    print("Decrypted: %r" % d)

    # decodificar mensaje
    f = open('Criptografia/Algoritmos-de-Cifrado/DES/desencrypt.txt', 'w')
    # decodificar base64
    f.write('orginal: ' + d.decode("utf-8"))
    f.close()

    # imagen nueva
    decodeit = open(
        'Criptografia/Algoritmos-de-Cifrado/DES/imagenDeco.png', 'wb')
    decodeit.write(base64.b64decode((d)))
    decodeit.close()


if __name__ == '__main__':
    desEncryptAndDesEncrypt()
