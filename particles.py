#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 00:56:18 2021

@author: pablo
"""

from parameters import elementalCharge, electronMass, protonMass, neutronMass,\
    muonMass, neutralPionMass, chargedPionMass
from parameters import lightVelocity as c
from parameters import pi
from parameters import muonDecayTime, pionDecayTime

class Particle:
    def __init__(self, typeParticle, chargeParticle=elementalCharge):
        self.typeParticle = typeParticle
        self.chargeParticle = elementalCharge
        if typeParticle == 'electron':
            self.massParticle = electronMass
        elif typeParticle == 'proton':
            self.massParticle = protonMass        
        elif typeParticle == 'neutral pion':
            self.massParticle = neutralPionMass
        elif typeParticle == 'charged pion':
            self.massParticle = chargedPionMass
        elif typeParticle == 'muon':
            self.massParticle = muonMass
        elif typeParticle == 'neutron':
            self.massParticle = neutronMass
            self.chargeParticle = 0.
        else:
            raise AttributeError('Unknown particle')
            
def mass(particle):
    return Particle(particle).massParticle

def charge(particle):
    return Particle(particle).chargeParticle

def classicalRadius(particle):
    q = Particle(particle).chargeParticle
    m = Particle(particle).massParticle    
    return  q*q/m/c/c

def thomsonCrossSection(particle):    
    return 8.*pi*(classicalRadius(particle)**2)/3

def restEnergy(particle):
    return mass(particle)*c*c

def decayTime(typeParticle,lorentzFactor):
    if typeParticle == 'charged pion':
        return pionDecayTime*lorentzFactor
    if typeParticle == 'muon':
        return muonDecayTime*lorentzFactor