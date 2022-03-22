# Ejercicios-de-Clases-de-POO

La dirección de GitHub de este repositorio es:[GitHub](https://github.com/joseluis031/Ejercicios-de-Clases-de-POO.git)

Trabajo realizado por :
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
```#Define la clase padre
class A:
  #A continuación define los métodos de la clase 
    def z(self): 
        return self #Aquí devuelve una referencia al objeto de instancia que fue llamado.
 
    def y(self, t): 
        return len(t) 
 
a = A  #define la variable "a" y la iguala a la clase A
y = a.z 
print(y(a)) #imprime por pantalla la variable "y" y "a"
aa = a() 
print(aa is a()) #devuelve un False, porque no es cierto
z = aa.y 
print(z(())) #devuelve un 0, porque no tiene ningún elemento
print(a().y((a,))) #devuelve un 1, ya que tiene el lemento "a"
print(A.y(aa, (a,z))) #devuelve un 2, ya que tiene el elemto "a" y "z"
print(aa.y((z,1,'z'))) #devuelve un 3, ya que tiene tres elementos "z","1" y "`z´"
```
## Su UML
![UML puzzle parejas](https://user-images.githubusercontent.com/91722847/159485428-6b01524f-9bef-464e-aa7d-9a27b4ee7248.png)

## Ejercicio 4: Logger
```import itertools
import string
import os
import time

class Test():
  def llamada(self,n,pal):
    self.palabra = pal
    for i in itertools.repeat (1,n):
      if i == 1:
        Test.llamada("Primera llamada")
      else:
        Test.llamada("{}ª llamada" , format(string) )

fichero = open("logger.txt","a") #Abre el fichero en el que se creará el número de llamadas
fichero.write("llamada")
time.sleep(15) #durará sólo 15s
os.remove("logger.txt") #Tras transcurrir el tiempo, se destrirá
```
## Su UML
![UML logger](https://user-images.githubusercontent.com/91722847/159484222-08525ec2-8a5c-4f54-87a9-1505fbe844d9.png)

