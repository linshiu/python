# -*- coding: utf-8 -*-
"""
Leetcode 083. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

#%% Solution 1
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        current = head
        
        while current.next:
            
            # move on to next
            previous, current = current, current.next
            
            # duplicate
            if previous.val == current.val:
                
                # delete the current node by changing the links
                previous.next = current.next
                current = previous
                
        return head
        
    
    def printList(self, head):
        
        s = ""
        if not head:
            return s

        current = head
        s += str(current.val)
        
        while current.next:
            current = current.next
            s += "->" + str(current.val)
            
        return s

#%% Solution 2
class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current = head
        
        while current:
            
            next_node = current.next
            
            # got to next until next node in None or the values of the current and next are different
            # so find the next node that is different than current one
            while next_node and current.val == next_node.val:
                next_node = next_node.next
                           
            # set the next link for first entry in repetition to first different one in sequence
            current.next = next_node
            current = next_node             
                
        return head
        
    
    def printList(self, head):
        
        s = ""
        if not head:
            return s

        current = head
        s += str(current.val)
        
        while current.next:
            current = current.next
            s += "->" + str(current.val)
            
        return s                
        
#%% Test
        
if __name__ == "__main__":
    
    test = Solution2()
    
    nums = [1,1,2,3,3]
    nodes = [ListNode(i) for i in nums]
    
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    
    head = nodes[0]
    
    test.printList(head)
    test.deleteDuplicates(head)
    test.printList(head)
    
    
    
    