palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
class palindromo:
    def __init__(self,palabra):
      self.palabra = palabra
    def correcto(self):
      self.s = palabra[::-1]
      if self.s ==self.palabra:
        print("True")
      else: 
        print("False")

