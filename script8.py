# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:06:09 2021

@author: Marcel
"""

ing_edad=int(input("Ingrese su edad en numeros: "))

if ing_edad<17:
    print("Su edad corresponde a un menor")
    calc=ing_edad*10
    
elif ing_edad>=18 and ing_edad<=40:
   print("Su edad corresponde a un adulto joven")
   calc=ing_edad*20
 elif ing_edad>40 and ing_edad<=60:
     print("Su edad corresponde a un adulto")
     calc=ing_edad*30

     
else:
    print("Su edad corresponde a un adulto mayor")
    calc=ing_edad*30
    
print(f"La edad ingresada fue: {ing_edad}\nEl valor del calculo es {calc}")




