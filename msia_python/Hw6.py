"""
*************************************************************************

The goal of this assignment is to build a function that will process an 
image to produce another image such that regions of similar color in the 
input image are converted to regions of exactly the same color in the
output image.

Step 1:
build a graph from the image with one vertex per pixel and edges 
connecting neighboring pixels if they have similar color and 
should be in the same region;

Step 2:
apply your connected component algorithm from assignment #3 
to find the pixels in each region

Step 3:
Experiment to find good functions to determine if two neighboring
pixels have a similar color in order to produce a segmentation that 
looks good. Make sure you can handle both black and white and color images


@author: Steven

*************************************************************************
"""

import os
#os.chdir('C:\\Users\\Steven\\Documents\\Academics\\3_Graduate School\\2014-2015 ~ NU\\Python\\Hw6')

import graph
import graphalgorithms
import numpy as  np

from PIL import Image


def segmentImage(inFileName, outFileName, distanceFunction, threshold):
    
    """
    @ param: inFileName
    @ param: outFileName
    @ param: distanceFunction
    @ param: threshold: if within this distance, add an edge between pixels
             the smaller the threshold, the fewer edges (more connected components)
             meaning more segmentation
    
    """
    im = Image.open(inFileName)
    pixels = np.asarray(im)
    # print(pixels.shape)
        
    g = graph.UndirectedGraph()
    height= pixels.shape[0]
    width = pixels.shape[1]
    
    computeDistance = distanceFunction
    
    # (j,i) j = column, i = row
    for i in range(height):
        for j in range(width):
            node = g.addVertex((i,j))
            # node.rgb = pixels[i,j]
            
            # check neighborhs
            
            if( j > 0 and computeDistance(pixels[i,j], pixels[i,j-1]) < threshold ):
                g.addEdge((i,j),(i,j-1))
                
            if( j > 0 and i > 0 and computeDistance(pixels[i,j], pixels[i-1,j-1]) < threshold ):
                g.addEdge((i,j),(i-1,j-1))
            
            if( i > 0 and computeDistance(pixels[i,j], pixels[i-1,j]) < threshold ):
                g.addEdge((i,j),(i-1,j))
            
            if( i > 0 and j < width-1 and computeDistance(pixels[i,j], pixels[i-1,j+1]) < threshold ):
                g.addEdge((i,j),(i-1,j+1))
                
            # More efficient way to do is using combination of tuples"
                # dimRanges = [range(dimDic[k]) for k in labels]
                # comb = itertools.product(*dimRanges) # np.indices((3,3))
            
    def forEachNodeCC(node, cc):
            node.cc = cc
    
    # dictionary with key = cc , value = set of vertixes objects
    ccDict = graphalgorithms.connectedComponents(g, forEachNodeCC)
    print("Number of segments: {0}".format(len(ccDict))) # number of components
    
    # computer average color for each connected component, key=cc, value=color
    ccRGB = {}
    for k,v in ccDict.items():
        
        # get RGB from vertex object, store in np array and compute averages
        # ccRGB[k] = np.average(np.array([n.rgb for n in v]),axis=0)
        ccRGB[k] = np.average(np.array([pixels[n.name] for n in v]),axis=0)
    
    # create new image
    new = np.zeros(shape=pixels.shape, dtype=np.uint8)
    
    # fill the new image with colors with each pixel having the cc color
    for i in range(height):
        for j in range(width):   
            new[i,j] = ccRGB[g._vertexes[(i,j)].cc]
    
    img = Image.fromarray(new, 'RGB')
    img.save(outFileName)
    img.show()

#%%  ########## Define distance functions  ###################################

# Euclidean Distance
def find2Norm(x,y):
    # compute the max distance between rgb pixels to normalize
    black = np.array([0,0,0])
    white = np.array([255,255,255])
    maxdist = np.linalg.norm(black-white)

    #return np.linalg.norm(x-y)/maxdist
    return np.linalg.norm(x-y)

# Correlation Coefficient   
def findInvCorr(x,y):
    return 1/np.corrcoef([x,y])[0,1]
    
#%% ########## Test  ################################## 

inFileName = "sailboat.jpg"
outFileName = "output.jpg"
distanceFunction = findInvCorr
threshold  = 1.0005 #1/.995 
#distanceFunction = find2Norm
#threshold = 6 

segmentImage(inFileName, outFileName, distanceFunction, threshold)

#%% ########## Test2  ################################## 

inFileName = "lebron.jpg"
outFileName = "output2.jpg"
distanceFunction = findInvCorr
threshold  = 1.0005 #1/.995 
#distanceFunction = find2Norm
#threshold = 6 

segmentImage(inFileName, outFileName, distanceFunction, threshold)