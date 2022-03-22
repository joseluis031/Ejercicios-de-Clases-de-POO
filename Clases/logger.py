import itertools
class Test():
  def llamada(self,p):
    self.palabra = p
    for i in itertools.repeat (1,n):
      if i == 1:
        print(Test.llamada(self.palabra , "1"))
      else:
        print(Test.llamada("{}ª" , self.palabra,format(p) ))





palabra=str(input("Introduce la palabra: "))
n=int(input("¿Cuántas veces desea repetir la palabra: "))

Test1 = Test()
print(Test1.llamada())

#test = Test() 
#for i in range(1, 6): 
 #  if i == 1: 
  #     test.llamada("Primera llamada") 
   #else: 
    #   test.llamada("{}ª llamada".format(string)) 
#$> cat log.txt 
#--Start log-- 
#Primera llamada 
#2a llamada 
#3a llamada 
#4a llamada 
#5a llamada 
#--End log: 5 log(s)-- 