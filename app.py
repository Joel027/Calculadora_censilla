# import re 


# def validar_email(email):
    
#     cacteres_validar = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    

#     if re.match(cacteres_validar , email):
#         return True
#     else:
#         return False



# Email = input("introduce tu correo electronico: ")

# if validar_email(Email):
#     print("El email es valido")
# else:
#     print("EL email es invalido")

import math

#herencia ejemplo practico

class calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    
    def ingresardato(self):
        self.datos = [int(input('Ingresar tu datos: '+str(i+1)+ '= '))for i in range(self.n)]

class op_basica(calculadora):
    def __init__(self):
        calculadora.__init__(self, 2)
        

    
    def suma(self):
        a,b, = self.datos
        s = a + b
        print('El resultado es: ',s)        
    
    def resta(self):
        a,b, = self.datos
        r = a - b
        print('El resultado es: ',r)
        
    def multiplicacion(self):
        a,b, = self.datos
        m = a * b
        print('El resultado es: ',m)
        
    def divicion(self):
        a,b, = self.datos
        d = a / b
        print('El resultado es: ',d)
        

class Raiz(calculadora):
    def __init__(self):
        #funcion padre
        calculadora.__init__(self, 1)
    
    def cuandra(self):
        a,= self.datos
        print('el resultado es: ',math.sqrt(a))
        

resultado = Raiz()

print(resultado.ingresardato())
print(resultado.cuandra())