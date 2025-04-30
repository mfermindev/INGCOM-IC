def sumar_ascii(cadena):
    """
    Recibe una cadena de caracteres y devuelve la suma de cada carácter con su valor ASCII.
    
    Ejemplo:
    "hola mundo" -> h(104) + o(111) + l(108) + a(97) + (32) + m(109) + u(117) + n(110) + d(100) + o(111) = 999
    """
    #  implementar esta función
    suma = 0
    for caracter in cadena:
        suma += ord(caracter) + ord(caracter)
    return suma
