# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:02:28 2021

@author: Marcel
"""

Datos_2021=[1,2,3,4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
Datos_2021_pares=[]
Datos_2021_impares=[]

# aqui el for lee o se barre todos los elementos de la lista
for i in Datos_2021:
    # esta linea verifica si el elemento es par o impar 
    if i % 2 == 0:
        # esta linea agrega el item en la lista de pares
       Datos_2021_pares.append(i)
       # esta linea agrega el item en la lista de impares
    else:
       Datos_2021_impares.append(i)

# esta linea ordena los datos pares
Datos_2021_pares.sort()   
Datos_2021_impares.sort()  
 
# estas lineas imprimen los datos pares
print("Lista de números pares: ")    
print(Datos_2021_pares)

# estas lineas imprimen los datos impares 
print("Lista de numeros impares: ")
print(Datos_2021_impares)




        

        


    