palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
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
