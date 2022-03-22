import itertools
import string
class Test():
  def llamada(self,n,p):
    self.palabra = p
    for i in itertools.repeat (1,n):
      if i == 1:
        Test.llamada("Primera llamada")
      else:
        Test.llamada("{}ª llamada" , format(string) )






#Test1 = Test()
#print(Test1.llamada())

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