# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:59:53 2020

@author: CEC
"""

file=open("devices.txt","a")

while True:
    
    newItem = input("Ingrese un nuevo dispositivo: ")
    
    if newItem == "exit":
        print("All done!")
        break
    else:
        file.write(newItem+"\n")
file.close()