# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:15:15 2021

@author: Marcel
"""


def saludos():
        """ESTA FUNCION NOS DA LAS BUENAS NOCHES BASADO EN NUESTROS NOMBRES"""
        nombre=input("Digite su primer nombre: ")
        salida="¡Buenas noches, "+nombre+"!"
        return salida
 
print(saludos())
