palabra = input("Introduce la palabra que quieras comprobar si es un palindromo")
class palindromo:
    def iniciar (self,p):
      self.cadena = p

    def correcto(self):
      if len(palabra) < 1:
        print ( self.cadena ," es un palindromo!")
      else:
         if palabra[0] == palabra[-1]:
           palindromo(palabra[1:-1])
           else:
                print(self.cadena, "no es un palindromo")



palindromo1 = palindromo()
palindromo1.iniciar(palabra)





  
    #def palindromo(palabra):
     #   if len(palabra) < 1:
      #      print(palabra, "palindromo!!")
       # else:
        #    if palabra[0] == palabra[-1]:
         #       palindromo(palabra[1:-1])
          #  else:
           #     print(palabra, "no es un palindromo")
  #  palindromo(palabra)