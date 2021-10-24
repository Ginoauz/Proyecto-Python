# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:05:07 2021

@author: Marcel
"""

def funcion1(param1,param2=100):
    if type(param1)==int and type(param2)==int:
        if param1>0 and param2>0:
            suma=param1+param2
            return suma
        else:
            print("Los numeros no son positivos")
        
    else:
        print("Los numeros no son tipo INT")
        
num1=int(input("Numero 1: "))
num2=int(input("Numero 2: "))

funcion1(num1,num2)

            
            
                 