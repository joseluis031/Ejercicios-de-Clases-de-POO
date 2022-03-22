#Define la clase padre
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
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z')))