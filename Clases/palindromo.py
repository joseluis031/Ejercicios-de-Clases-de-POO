palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
s = palabra[::-1]
class palindromo:
    def __init__(self,palabra,s):
      self.palabra = palabra
      self.s = s
    def correcto(self):
      if self.s ==self.palabra:
        print("True")
      else: 
        print("False")

palindromo1 = palindromo(palabra,s)
print(palindromo1.correcto())
