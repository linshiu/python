# -*- coding: utf-8 -*-
"""
Find the top K in a list of tuples
"""

#%% function
def getFrequency(list_tuples, pos):
    """Gets the frequency of each value of a certain index position in tuple
    
    Args:
        list_tuples (list): list of tuples
        pos (int): index position of items to find frequency 
    
    Returns:
        dict: dictionary key: item from index pos, value: frequency (count)
    
    """
    freq = {}
    
    for t in list_tuples:
        if t[pos] not in freq:
            freq[t[pos]] = 1
        else:
            freq[t[pos]] += 1

    return freq
    
def findTop(freq, k):
    """ Find top k keys from freq dictionary 
    
    Args:
        freq (dict): frequency dictionary key: item, value: frequency
        k (int): top k
        
    Returns
        list: top k items
    
    """
    
    freq_list = list(freq.items())
    max_list = []
    
    i = 0
    
    # iterate until k number of max values are removed
    while i < k:
           
        max_value = freq_list[0][1]
        max_index = 0
        
        for j in range(1,len(freq_list)):
            
            # update max
            if freq_list[j][1] > max_value:
                max_index = j
                max_value = freq_list[j][1]
        
        # remove max tuple and add to max        
        max_list.append(freq_list.pop(max_index))
        
        i+=1
    
    # sort by count
    max_list.sort(key = lambda x : -x[1])
    
    # return only keys
    return list(zip(*max_list))[0]
    
    
#%% test
import random
test = [(chr(random.randrange(65,91)),random.random()) for i in range(200)]

freq = getFrequency(test,0)
top = findTop(freq,5)
print(top)

