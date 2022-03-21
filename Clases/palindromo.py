palabra = input("Introduce la palabra que quieras comprobar si es un palindromo: ")
class palindromo:
    def iniciar (self,palabra):
      self.palabra = palabra

    def correcto(self):
      if len(self.palabra) < 1:
        print ( self.palabra ," es un palindromo!")
      else:
        if palabra[0] == palabra[-1]:
           palindromo(palabra[1:-1])
        else:
           print(self.palabra, "no es un palindromo")



palindromo1 = palindromo()
palindromo1.iniciar(palabra)
palindromo1.correcto()





  
    #def palindromo(palabra):
     #   if len(palabra) < 1:
      #      print(palabra, "palindromo!!")
       # else:
        #    if palabra[0] == palabra[-1]:
         #       palindromo(palabra[1:-1])
          #  else:
           #     print(palabra, "no es un palindromo")
  #  palindromo(palabra)