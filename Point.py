# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:34:28 2019

@author: josep
"""

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def getData(self):
        print("({0},{1})".format(self.x,self.y))
    