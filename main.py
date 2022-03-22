if __name__ == "__main__":
    main = int(input("Que ejercicio deseas realizar(1,2,3 o 4):"))
    if main == 1:
        from Clases.palindromo import *
        print("Ejercicio palindromo: ")
        palindromo.correcto()
    elif main == 2:
        from Clases.palinstancia import *
        print("2º ejercicio palindromo: ")
        palindromo2.correcto2()
    elif main == 3:
        from Clases.puzzle import *
        print("Ejercicio puzzle: ")
        A.y()
    elif main == 4:
        from Clases.logger import *
        print("Ejercicio logger: ")
        Test.llamada()
    else:
        print("Ese número no es valido")
    