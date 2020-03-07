# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:42:59 2020

@author: CEC
"""

import math
try:
   x=int(input("Ingrese un numero: "))
   y=1/x
   print(y)
except ZeroDivisionError:
    print("No puede dividir para cero, lo siento.")
except ValueError:
    print("Debe ingresar un valor entero")
except:
    print("Oh, algo estuvo mal")
print("FIN")
     