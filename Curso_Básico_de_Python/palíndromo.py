def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra= palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
       return True
    else:
        return False


def run():
    palabra =input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Tu palabra es un palíndromo")
    else:
        print("Tu palabra no es un palíndromo")



if __name__ == "__main__":
    run() 