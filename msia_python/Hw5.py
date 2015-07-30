# -*- coding: utf-8 -*-
"""
Assignment 4
Steven Lin
5/19/15

Python: 3.4
Editor: Spyder

Code adapted from Jorge's graph and assignment codes
"""

import numpy as np
from copy import deepcopy
import itertools


#%% Classes  ##############################################################

class Node:
    """
    Attributes: name, values, cpt, parents list of objects
    Method: set and get names, values, cpt, parents
    
    """
    def __init__(self, name):
        self.name = name
        self.values = []
        self.evidence = None
        self.parents = []
        self.cpt = None
        self.cptOriginal = None
        self.einsumID = None
        self.einsumIDcpt = None
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setValues(self, valuesList):
        self.values = valuesList
    
    def getValues(self):
        return self.values
    
    def setCPT(self,cptArray):
        self.cpt = cptArray
        self.cptOriginal = cptArray
    
    def getCPT(self):
        return self.cpt
    
    def setParents(self, parentsList):
        self.parents = parentsList
    
    def getParents(self):
        return self.parents
        
    def setEvidence(self,value):
        self.evidence = np.zeros(len(self.values))
        i = self.values.index(value)
        self.evidence[i] = 1 
        #self.cpt = self.cptOriginal[i]
        
    def removeEvidence(self):
        self.evidence = None
        #self.cpt = self.cptOriginal
        
    def nodeInfo(self):
        print("Name: {0}\nValues: {1}\nCPT: {2}\nParents:{3}".format(
        self.name, self.getValues(), self.getCPT(),self.getParents()))
         
    '''   
        Nodes are compared according to their names
    '''
    def __hash__(self):
        return hash(self.name)
        
    def __eq__(self,other):
        return self.name == other.name        
        
    def __lt__(self,other):
        return self.name < other.name
    
    def __repr__(self):
        return str(self.name)
    

class Network:
    def __init__(self, name = "MyNetwork"):
        self.name = name
        self.nodes = {}

    def addNode(self, name, values, cpt, parents=[]):
        self.nodes[name]= Node(name)
        self.nodes[name].setValues(values)
        self.nodes[name].setCPT(cpt)
        self.nodes[name].setParents(parents)
        
        # assign unique character for einsum function
        self.nodes[name].einsumID = chr(96+len(self.nodes)) # 97 --> "A"
        
        # get the unique character combinations representing cpt for einsum
        # einsumID + einsumID of parents
        self.nodes[name].einsumIDcpt= self.nodes[name].einsumID + ''.join(
        [self.nodes[parent].einsumID for parent in self.nodes[name].parents])

        return self.nodes[name]
        
    def computeMarginal(self,name):
        
        n = self.nodes[name]
        
        # get subscripts
        einsumSub = [n.einsumIDcpt for n in self.nodes.values()]
        einsumSubEvid = [n.einsumID for n in self.nodes.values() if n.evidence!=None]
         
        # get operands 
        einsumArrays = [n.cpt for n in self.nodes.values()]
        einsumArraysEvid = [n.evidence for n in self.nodes.values() if n.evidence!=None ]

        subscripts = ','.join(einsumSub+einsumSubEvid)+'->'+n.einsumID
        marginal = np.einsum(subscripts,*(einsumArrays+einsumArraysEvid))

        return marginal/np.sum(marginal) # normalize 
        
    def networkInfo(self):
        print("Name: {0}\nNodes: {1}\n".format(self.name, self.nodes.values()))
    
    def __hash__(self):
        return hash(self.name)
        
    def __eq__(self,other):
        return self.name == other.name        
        
    def __lt__(self,other):
        return self.name < other.name
    
    def __repr__(self):
        return str(self.name)
        
#%% Test
import numpy as np 

ageP = np.array([0.3,0.7])
genderP= np.array([0.4,0.6])
cancerP = np.array([[[0.1, 0.2], [0.3, 0.4]],
                    [[0.2, 0.3], [0.4, 0.5]],
                    [[0.7, 0.5], [0.3, 0.1]]])

# Have to add nodes to the network sequentially
# (to add a child, parents must exist before)
 
# sample bayesian network: age -> cancer, gender -> cancer
bn = Network()

age = bn.addNode("Age", ["Young", "Old"], ageP)
gender = bn.addNode("Gender",["Male", "Female"], genderP)
cancer = bn.addNode("Cancer", ["None", "Benign", "Malign"], cancerP, ["Age","Gender"])           
               
age.nodeInfo()
gender.nodeInfo()
cancer.nodeInfo()
bn.networkInfo()

for name in bn.nodes:
    print("einsumid: {0}, ensumIDcpt: {1}".format(
    bn.nodes[name].einsumID,
    bn.nodes[name].einsumIDcpt)) 

print(bn.nodes["Cancer"].evidence)
print(bn.computeMarginal("Age"))
print(bn.computeMarginal("Gender"))
print(bn.computeMarginal("Cancer"))

print(bn.nodes["Cancer"].setEvidence("None"))
print(bn.computeMarginal("Age"))
print(bn.computeMarginal("Gender"))
print(bn.computeMarginal("Cancer"))

print(bn.nodes["Cancer"].removeEvidence())
print(bn.computeMarginal("Age"))
print(bn.computeMarginal("Gender"))
print(bn.computeMarginal("Cancer"))




    



#%% Classes  ##############################################################
