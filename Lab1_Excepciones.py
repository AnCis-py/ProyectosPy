# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:36:50 2020

@author: CEC
"""

def leerEntrada(dato, min,max):
   # while min>=-10 and max<=10:
        try:        
            dato=int(input(" Por favoringrese un numero"))
        except ValueError:
            print("Por favor ingresar un valor valido....")
        else:
            print("El valor es:" ,dato)
        
        finally:
            print("Todo salio bien")