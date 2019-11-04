# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:24:07 2019

@author: josep
"""

import random
class Chromosome :
    def __init__(self,degree,points,lowBoundry=float(-10),upperBoundry=float(10)):
         self.lowBoundry=lowBoundry
         self.upperBoundry=upperBoundry
         self.size=degree+1
         self.degree=degree
         self.floatsList=self.generateGene()
         self.points=points
         self.fitness=self.getFitness()         
    def generateGene(self):
        floats=[]
        for x in range (self.size):
            floats.append(random.uniform(self.lowBoundry,self.upperBoundry))
        return floats
 
    def getEquationValueAtPoint(self,point):
        yCalc=0
        for i in range(self.size):
            yCalc+=self.floatsList[i]*(point.x**i)
        return yCalc
   
    def getFitness(self):
        totalSquaredError=0
        for i in (self.points):
            totalSquaredError+=(self.getEquationValueAtPoint(i)-i.y)**2
        return totalSquaredError/len(self.points)

    def mutate(self,currentGeneration,totalGeneration):
        index=random.randint(0,self.size-1)
        selectedItem=self.floatsList[index]
        r1=random.uniform(0,1)
        deltaL=selectedItem-self.lowBoundry
        deltaU=self.upperBoundry-selectedItem
        Y=deltaL if r1<=0.5 else deltaU
        depFactor=5
        valueOfMutation=Y*(1-r1**(1-currentGeneration/totalGeneration)**depFactor)
        self.floatsList[index]=valueOfMutation
        
        
         
        