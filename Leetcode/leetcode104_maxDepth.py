# -*- coding: utf-8 -*-
"""
Leetcode 104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest
 path from the root node down to the farthest leaf node.


"""

#%% Solution 1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    """
    Do BFS, keeping track of number of nodes in current and next level to update depth
    
    :type root: TreeNode
    :rtype: int
    """
    depth = 0
    nodes_current = 0 # number of nodes current level
    nodes_next = 0 # number of nodes next level
    
    if not root:
        return depth
    
    # BFS
    queue = [root]
    
    while queue:
        
        node = queue.pop(0)    
        
        if node.left:
            queue.append(node.left)
            nodes_next+=1
    
        if node.right:
            queue.append(node.right)
            nodes_next+=1
            
        # everytime pop one node, reduce number of nodes in current level that need to be checked
        nodes_current-=1
        
        # no more nodes at current level, then reset count for nodes next level
        if nodes_current <= 0: # less than zero for root case
            nodes_current = nodes_next
            nodes_next = 0
            depth += 1 # completed current level so add to depth number
    
    return depth
    
#%% Recursive Solution


def maxDepth(root):
    
    # base case
    if root is None:
        return 0
    else:    
        return max(maxDepth(root.left), maxDepth(root.right)) + 1    


#%% Test
n0 = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n0.left = n1
n0.right = n2
n1.left = n3
n2.left = n4
n2.right = n5
n4.right = n6

maxDepth(n0)