# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:54:01 2020

@author: CEC
"""

def validarNumero(prompt, min,max):
   while (True):
        try:       
            x=int(input(prompt))
            assert x>=min and x<=max
            return x
            break

        except ValueError:
            print("Por favor ingresar un valor valido....")
        except:
            print("El valor debe estar ingresado dentro del rango....> (-10....10)  <---")
            
v = validarNumero("Ingrese un valor desde -10 a 10:", -10,10)
print("El valor es:" ,v)
        