# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:14:22 2020

@author: CEC
"""

#class TheSimplestClass:
 #   pass
#myFirstObject = TheSimplestClass()
 
class Empleado:
     'Common bases class for all employees'
     empCount=0
     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
         Empleado.empCount +=1
         
     def displayCount(self):
             print ("Total Empleados %d" % Empleado.empCount)
     def displayEmployee(self):
             print ("Name: ",self.name,"Salary",self.salary)
             
             
emp1=Empleado("Zara",2000)
emp2=Empleado("Manni",5000)
emp3=Empleado("Melissa",1500)
emp4=Empleado("Eduardo",1600)
emp5=Empleado("Carlos",800)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()
emp4.displayCount()
#print ("Total Empleados %d" % Empleado.empCount)