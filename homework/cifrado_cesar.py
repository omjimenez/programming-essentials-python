# Programm in python - Algorithm Caesar Cipher

class Cifrado:

    def __init__(self, posiciones):
        self.posiciones = posiciones

    def codificar(self,mensaje):
        _cadena_codificada = []
        _numero_letra = 0

        for letra in mensaje:
            _numero_letra = ord(letra) + self.posiciones
            _cadena_codificada.append(chr(_numero_letra))

        return ''.join(_cadena_codificada)

    def decodificar(self, mensaje):
        _cadena_decodificada = [] 
        _numero_letra = 0

        for letra in mensaje:
            _numero_letra = ord(letra) - self.posiciones
            _cadena_decodificada.append(chr(_numero_letra))

        return ''.join(_cadena_decodificada)


# Implementacion
if __name__ == '__main__':
    print('Introduzca un mensaje ')
    mensaje = input('---> ')
    rotaciones = 3

    proceso_codificar = Cifrado(rotaciones)

    msj_codificar = proceso_codificar.codificar(mensaje)
    msj_decodificado = proceso_codificar.decodificar(msj_codificar)

    print('\n Mensaje Cifrado: ', msj_codificar)

    print('\n Mensaje Descifrado: ', msj_decodificado)
