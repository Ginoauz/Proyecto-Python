# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 19:53:04 2021

@author: Marcel
"""

n=int(input("Ingrese el numero de palanquetas que no son del día como un numero: "))
descuentopalanqueta= round(2.5*0.5,2)
precio=round(2.5-descuentopalanqueta,2)
print(f'precio de una palanqueta:\t2.50\
      \nDescuento por palanqueta que no es del día:\t{descuentopalanqueta}\
          \nTotal compra:\t{n*precio}')
          
          