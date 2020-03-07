# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:51:18 2020

@author: CEC
"""
devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print (devices)