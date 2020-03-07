# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:15:18 2020

@author: CEC
"""

aclNum=int(input("What is the IPv4 ACL number?"))
if aclNum >=1 and aclNum <=99:
    print("This is a standart IPv4 ACL.")
    
elif aclNum>=100 and aclNum<=199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not a standart or extended IPv4 ACL.")
    

devices=["R1","R2","S1","R3"]

switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
        
        
        
        x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<x:
    print(y)
    y=y+1
    
    
    
        x1=input("Enter a number to count to: ")
x=int(x1)
y=1
while True:
    print(y)
    y=y+1
    if y>x1:
        break
    
    
    while True:
    x=input("Enter a number o count to: ")
    if x=='q' or x=='quit':
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
        
            break
        
        --ejemplo
for i in range(5):
    print(i+1)
    
    --Rangos
    
    result =0
n=5

for i in range (1,n+1):
    result +=i
        print (result)
        
    for i in range(10,0,-2):
        print(i)
        
        
        
    