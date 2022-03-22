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
        a = A  
        y = a.z 
        print(y(a)) 
        aa = a() 
        print(aa is a()) 
        z = aa.y 
        print(z(())) 
        print(a().y((a,))) 
        print(A.y(aa, (a,z))) 
        print(aa.y((z,1,'z'))) 
    elif main == 4:
        print("Ejercicio logger: ")
        from Clases.logger import *
        n=int(input("¿Cuántas veces desea repetir la palabra: "))
        Test1 = Test()
        print(Test1.llamada(n))
    else:
        print("Ese número no es valido")
    