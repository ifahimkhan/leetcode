# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#         V
# init ..1234..
#  ---->1----->2----->3----->4--->
#      prev   trav   next_  beyound
    
        
# final ..1324..
#       --------------|
#       |             V
#  ---->1      2<-----3      4--->
#              |             ^
#              --------------|
#      prev   trav   next_  beyound

# link swaps
# trav.next = beyound
# next_.next = trav
# prev.next = next_

# advance
# prev = trav
# trav = beyound
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(None)
        trav = dummy.next = head
        while trav and trav.next:
            next_ = trav.next
            beyound = next_.next
            
            trav.next = beyound
            next_.next = trav
            prev.next = next_
            
            prev = trav
            trav = beyound            
        return dummy.next
