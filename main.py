# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:56:38 2019

@author: josep
"""

from FloatAlgorithm import FloatAlgorithm 
from Point import Point 

filePath = "input-2.txt"
f = open("result.txt", "a")

with open(filePath, "r") as file:
    text = file.read()

testCases = text.split("\n")

start=1
testCaseIndex=1
while testCaseIndex <= int(testCases[0]):
    caseSize,degree = testCases[start].split(" ")

    items = []
    for item in testCases[start+1:start+1+int(caseSize)]:
         x, y = item.split(" ")
         items.append(Point(float(x), float(y)))
    floatObj=FloatAlgorithm(int(degree),items)
    result=floatObj.run()
    f.write("Case {0}:\n".format(testCaseIndex))
    f.write(" ".join(map(str,result.floatsList)))
    f.write("\nError:{0} \n".format(str(result.fitness)))
    f.write("------------------------------------------------\n")
    print("Case {0}: {1}".format(testCaseIndex,result.floatsList))
    start+=int(caseSize)+1
    testCaseIndex+=1
f.write("------------------------------------------------- New Iteration ----------------------------------------------------\n")
f.close()