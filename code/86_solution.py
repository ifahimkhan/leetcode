# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# init 143252   x = 3    

#             l    r         n
#        1--->4--->3--->2--->5--->2      
#      prev           trav
# 1. one swap 124352  
# rewire
#         l   r
#         |---------|
#         V         |     n
#    1    4--->3--- 2 --->5--->2      
#    |              ^
#    ---------------|
#  prev           trav

# advance
#         l   r
#         |---------|
#         V         |     n
#    1    4--->3--- 2 --->5--->2      
#    |              ^
#    ---------------|
#                 prev   trav

# 2. one swap 122435
#              l          r
#    1--->2--->4--->3---->5--->2      
#       prev                 trav
  
    
#       t  
# n 1 4 3 2 5 2     x = 3
#   p l/r


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        prev = dummy = ListNode()
        dummy.next = trav = left = right = head
        while trav:
            while trav and trav.val >= x:
                right = trav
                trav = trav.next
            if not trav: continue
            if trav != right:
                next_ = trav.next
                prev.next = trav
                trav.next = left
                right.next = next_

                prev = trav
                trav = next_
            else:
                prev = trav
                trav = left = right = prev.next
        return dummy.next
