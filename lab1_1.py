# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:54:14 2020

@author: CEC
"""

def readint(prompt, min,max):
   while min>=-10 and max<=10:
        try:       
            
            
            v = readint("Enter a number from -10 to 10: : ", min, max)
        except ValueError:
            print("Por favor ingresar un valor valido....")
        else:
            print("El valor es:" ,v)
        
       # finally:
           # print("Todo salio bien")