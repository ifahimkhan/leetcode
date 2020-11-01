# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListIterator:
    def __init__(self, head):
        self.head = head
    
    def __iter__(self):
        self.node = self.head
        return self
    
    def __next__(self):
        if self.node: 
            val = self.node.val
            self.node = self.node.next
            return val
        raise StopIteration

        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        for val in ListIterator(head): 
            num = val + (num << 1)
        return num
