# -*- coding: utf-8 -*-
"""
Assignment 4
Steven Lin
5/19/15

Python: 3.4
Editor: Spyder
"""

import numpy as np
from copy import deepcopy
import itertools
import os

#import Hw5_v3.py

###
bn2 = Network()
bn2.addNode('A',['a1','a2']          ,np.array([ 0.9,  0.1]))
bn2.addNode('C',['c1','c2','c3','c4'],np.array([ 0.1,  0.2,  0.3,  0.4]))

bCPT = np.array(
      [[[0.2, 0.1, 0.01, 0.2], [0.33, 0.3, 0.2, 0.9 ]],
       [[0.4, 0.5, 0.01, 0.1], [0.33, 0.1, 0.7, 0.05]],
       [[0.4, 0.4, 0.98, 0.7], [0.34, 0.6, 0.1, 0.05]]])    
                
bn2.addNode('B',['b1','b2','b3'],bCPT, ['A','C']) 

# define a couple of useful functions
def marginal2(name):
    print('{} marginal distribution is {}'.format(name, bn2.computeMarginal(name)))
def allMarginals2():
    for name in bn2.nodes:
        marginal2(name)
        
# define a couple of useful functions
        
print ("Marginal distributions without evidence")
allMarginals2()

print ("\n\nMarginal distributions given B=b3")
bn2.nodes["B"].setEvidence('b3')
allMarginals2()

print ("\n\nMarginal distributions given B=b3 and C=c4")
bn2.nodes["C"].setEvidence('c4')
allMarginals2()

print ("\n\nMarginal distributions given C=c4")
bn2.nodes["B"].removeEvidence()
allMarginals2()