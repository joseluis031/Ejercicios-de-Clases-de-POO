palabra = input("Introduce la palabra que quieras comprobar si es un palindromo")
class Palindromo:
    def palindromo(palabra):
        if len(palabra) < 1:
            print(palabra, "palindromo!!")
        else:
            if palabra[0] == palabra[-1]:
                Palindromo(palabra[1:-1])
            else:
                print(palabra, "no es un palindromo")
    palindromo(palabra)