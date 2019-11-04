# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:54:07 2019

@author: josep
"""
from Chromosome import Chromosome as chromosome
import random
from operator import attrgetter

class FloatAlgorithm:
    def __init__(self,degree,points):
        self.degree=degree
        self.size=degree+1
        self.points=points
        self.populationSize=32
        self.population=self.initialPopulation()
    
    def initialPopulation(self):
        populationList=[]
        for i in range (self.populationSize):
            newChromosome=chromosome(self.degree,self.points)
            populationList.append(newChromosome)
        return populationList

    def totalFitness(self):
        total=0
        for i in self.population:
            total+=i.fitness
        return total
    
    def rouletteWheelSelection(self):
        maxSum=self.totalFitness()
        randomNumber=random.uniform(0,maxSum)
        currentSum=0
        for chromosomeObject in self.population:
            currentSum+=chromosomeObject.fitness
            if currentSum > randomNumber:
                return chromosomeObject

    def singlePointCrossover(self,parent1,parent2):
         point=self.singlePointPlace() 
         child1=chromosome(self.degree,self.points)
         child2=chromosome(self.degree,self.points)
        
         child1.floatsList=parent1.floatsList[0:point]+parent2.floatsList[-(self.size-point):]
         child2.floatsList=parent2.floatsList[0:point]+parent1.floatsList[-(self.size-point):]
        
         return child1,child2    

    def singlePointPlace(self):
        return random.randint(0,self.size-1)

    def removeWorst(self):
         worstIndex=0
         for i in range(len(self.population)):
             if self.population[i].fitness > self.population[worstIndex].fitness:
                 worstIndex=i
         self.population.pop(worstIndex)
    
    def run(self):
        generationCount=400
        for i in range (generationCount):
            parent1=self.rouletteWheelSelection()
            parent2=self.rouletteWheelSelection()
            #Crossover
            child1,child2=self.singlePointCrossover(parent1,parent2)
            
            #Mutation
            child1.mutate(i,generationCount)
            child2.mutate(i,generationCount)
            
            self.population.extend([child1,child2])
            
            #remove worst 2 genes in population
            self.removeWorst()
            self.removeWorst()
        
        return min(self.population, key=attrgetter('fitness'))