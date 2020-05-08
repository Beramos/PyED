# -*- coding: utf-8 -*-
"""
Created on Fri May 08 10:50:00 2020
@author: Bram De Jaegher
""" 

class Electrolyte:
    def __init__(self, lambdaEq=10.53e-3):
        self.lambdaEq = lambdaEq


class Reservoir:
    def __init__(self, volume, concentration, electrolyte=Electrolyte()):
        self.volume = volume
        self.electrolyte = electrolyte
        self.concentration = concentration
    
    def timeLoop(self, flux, time):
        return self.concentration - time*flux/self.volume

    def conductivity(self, concentration):
        return concentration*self.electrolyte.lambdaEq


class Channel:
    def __init__(self, length, width, thickness, electrolyte=Electrolyte()):
        self.length = length
        self.width = width
        self.thickness = thickness
        self.surfaceMem = length*width
        self.volume = length*width*thickness
        self.electrolyte = electrolyte

    def conductivity(self, concentration):
        return concentration*self.electrolyte.lambdaEq
        
    def resistance(self, concentration):
        kappa = self.conductivity(concentration)
        resistanceSolution = self.thickness/kappa/self.surfaceMem
        return resistanceSolution