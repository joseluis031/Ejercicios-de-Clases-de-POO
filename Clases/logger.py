import itertools
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