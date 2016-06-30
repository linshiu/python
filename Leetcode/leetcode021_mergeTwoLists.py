# -*- coding: utf-8 -*-
"""

Leetcode 021 - Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.

The new list should be made by splicing together the nodes of the first two lists.


Solution:
1) First find the smallest by comparing the first nodes of each linked list (FIRST)
2) Set CURRENT = FIRST
3) Then iterate (go to next) until run out of elements in a linked list. In
each iteration, compare the two nodes, assign the next element of CURRENT to the 
smallest node, advance CURRENT and smallest node.
4) Assign next of CURRENT to remaining nodes of linked list 1 or 2

Time: O(n)
Space: O(1)

"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        
        if not l2:
            return l1
            
        # initialize
        if l1.val <= l2.val: 
            first = l1
            l1 = l1.next   
        else:    
            first = l2
            l2 = l2.next
            
        current = first
        
        # iterate list nodes 1 and 2 advancing to next for smallest node
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1         
                l1 = l1.next                
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
            
        
        # remaining nodes of l1 or l2
        current.next = l1 or l2
        
        return first
                
    def printList(self,ls_node):
        
        s = str(ls_node.val)
        ls_node = ls_node.next
        while ls_node:
            s = s + " -> " + str(ls_node.val)
            ls_node = ls_node.next
        print(s)
            
                
                
        
        
        
#%% Test #####################################################################
        
if __name__ == '__main__':
    
    test = Solution()
    vals1 = [3, 10, 20]
    vals2 = [1, 2, 3, 15, 30, 35]
    
    l1_0 = ListNode(3)
    l1_1 = ListNode(10)
    l1_2 = ListNode(20)
    
    l1_0.next = l1_1
    l1_1.next = l1_2
    
    l2_0 = ListNode(1)
    l2_1 = ListNode(2)
    l2_2 = ListNode(3)
    l2_3 = ListNode(15)
    l2_4 = ListNode(30)
    l2_5 = ListNode(35)
    
    l2_0.next = l2_1
    l2_1.next = l2_2
    l2_2.next = l2_3
    l2_3.next = l2_4
    l2_4.next = l2_5
    
    test.printList(l1_0)
    test.printList(l2_0)
    
    l12 = test.mergeTwoLists(l1_0, l2_0)
    test.printList(l12)


    
    
    """
    nodes1 = [ListNode(v) for v in vals1]
    nodes2 = [ListNode(v) for v in vals2]
    
    for i in range(len(nodes1)-1):
        nodes1[i].next = nodes1[i+1]
        
    for i in range(len(nodes2)-1):
        nodes2[i].next = nodes2[i+1]
        
    """
    
