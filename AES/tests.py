import os
import pyaes
import base64

# abrir imagen
with open("AES/img.png", "rb") as image2string:
    # base64
    converted_string = base64.b64encode(image2string.read())
    if len(converted_string) % 8 != 0:
        for i in range(len(converted_string) % 8):
            converted_string += converted_string[0:1]


def desEncryptAndDesEncrypt(key):
    # encripta
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted = aes.encrypt(converted_string)
    # desencripta
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted = aes.decrypt(encrypted)

    f = open('AES/desencrypt.txt', 'w')
    # decodificar base64
    f.write('orginal: ' + decrypted.decode("utf-8"))
    f.close()

    # imagen nueva
    decodeit = open(
        'AES/imagenDeco.png', 'wb')
    decodeit.write(base64.b64decode((decrypted)))
    decodeit.close()

    print(encrypted)


if __name__ == '__main__':
    # key = 'X_esto_es_una_prueba_para_cifrar'
    tam = int(
        input("introduzca nivel de seguridad (128 bits, 192 bits o 256 bits): "))
    if tam == 128:
        key = input('introduzca la clave de tamaño 16 caracteres: ')
    elif tam == 192:
        key = input('introduzca la clave de tamaño 24 caracteres: ')
    elif tam == 256:
        key = input('introduzca la clave de tamaño 32 caracteres: ')

    desEncryptAndDesEncrypt(key.encode("utf-8"))
