if __name__ == "__main__":
    main = int(input("Que ejercicio deseas realizar(1,2,3 o 4):"))
    if main == 1:
        print("Ejercicio palindromo: ")
        from Clases.palindromo import *
        palindromo1 = palindromo(palabra)
        print(palindromo1.correcto())  
    elif main == 2:
        print("2º ejercicio palindromo: ")
        from Clases.palinstancia import *
        palindromo1 = palindromo2(palabra)
        print(palindromo1.correcto2())
    elif main == 3:
        print("Ejercicio puzzle: ")
        from Clases.puzzle import *
        A.y()
    elif main == 4:
        print("Ejercicio logger: ")
        from Clases.logger import *
        Test1 = Test()
        print(Test1.llamada())
    else:
        print("Ese número no es valido")
    