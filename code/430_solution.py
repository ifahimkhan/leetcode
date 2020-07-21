"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        
        prev = dummy = Node(None, None, head, None)
        stack = [head]
        while stack:
            trav = stack.pop()
            
            prev.next = trav
            trav.prev = prev
            
            if trav.next: stack.append(trav.next)
            if trav.child: 
                stack.append(trav.child)
                trav.child = None
                
            prev = trav
            
        dummy.next.prev = None
        return dummy.next
