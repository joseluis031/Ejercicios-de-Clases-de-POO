# Ejercicios-de-Clases-de-POO

La dirección de GitHub de este repositorio es:[GitHub](https://github.com/joseluis031/Ejercicios-de-Clases-de-POO.git)

Trabaj realizado por :
[José Luis](https://github.com/joseluis031) y
[Claudia](https://github.com/claudiaalozano)

## Ejercicio 1: Palindromo
```palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
class palindromo:
    def __init__(self,palabra):
      self.palabra = palabra
    def correcto(self):
      self.s = palabra[::-1]
      if self.s ==self.palabra:
        print("True")
      else: 
        print("False")
```
## Su UML
![uml palindromo 1](https://user-images.githubusercontent.com/91721888/159445832-0808970e-4ffe-45be-ab91-02d378f5eaf1.png)


## Ejercicio 2: Palindromo
```palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
class palindromo2:
    def __init__(self,palabra):
      self.palabra = palabra
    def correcto2(self):
      self.s = palabra[::-1]
      if self.s ==self.palabra:
        print(palabra.upper(),"True")
      else: 
        print(palabra.upper(),"False")

palindromo1 = palindromo2(palabra)
print(palindromo1.correcto2())
```
## Su UML
![uml palindromo2](https://user-images.githubusercontent.com/91721888/159445872-ac0fa203-e213-4da9-b3e9-99a70a5b1901.png)


## Ejercicio 3: Puzzle
## Su UML


## Ejercicio 4: Logger
## Su UML

