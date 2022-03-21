palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
s = palabra[::-1]
class palindromo:
    def __init__(self,palabra,s):
      self.palabra = palabra
<<<<<<< HEAD
      self.s = s
    def correcto(self):
      if self.s ==self.palabra:
        print("True")
      else: 
        print("False")
=======

    def comprobar(self):
      if len(self.palabra) < 1:
        print ( self.palabra ," es un palindromo!")
      else:
        if palabra[0] == palabra[-1]:
           palindromo(palabra[1:-1])
        else:
           print(self.palabra, "no es un palindromo")



palindromo1 = palindromo()
palindromo1.iniciar(palabra)
palindromo1.comprobar()


>>>>>>> 3733cd6fe21b342806cb8eb3ece2ad0427fcd15a



palindromo1 = palindromo(palabra,s)
print(palindromo1.correcto())
