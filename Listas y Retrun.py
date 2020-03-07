# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 08:24:14 2020

@author: CEC
"""

def isYearLeap(year):
#
# Su codigo AQUI
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
    	if result == testResults[i]:
    		print("OK")
    	      else:
    		      print("Failed")
