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
print(aa is a()) #devuelve un False, porque no es cierto
z = aa.y 
print(z(())) #devuelve un 0, porque no tiene ningún elemento
print(a().y((a,))) #devuelve un 1, ya que tiene el lemento "a"
print(A.y(aa, (a,z))) #devuelve un 2, ya que tiene el elemto "a" y "z"
print(aa.y((z,1,'z'))) #devuelve un 3, ya que tiene tres elementos "z","1" y "`z´"