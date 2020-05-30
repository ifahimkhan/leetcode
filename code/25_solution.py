# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# init 12345
#         oldhead       oldtail
#     1---->2---->3---->4----->5
#    prev  trav              beyound


# final 14325
#         newtail       newhead
#     1     2<----3<----4      5
#    prev  trav              beyound

# reverse_k(trav, k) -> beyound, newhead, newtail 

# rewire
# prev->newhead
# newtail->beyound

# advance
# prev = trav
# trav = beyound

#       k==3
# nptr<-1<-2<-3 4
#             p t n

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        
        def has_k_nodes(trav, k):
            while trav and k:
                trav = trav.next
                k -= 1
            return k == 0
        
        def reverse_k_nodes(trav, k):
            newtail = trav
            prev = None
            for i in range(k):
                next_ = trav.next
                trav.next = prev
                prev = trav
                trav = next_
            return trav, prev, newtail
        
        dummy = prev = ListNode(None)
        trav = dummy.next = head
        while has_k_nodes(trav, k):
            beyound, newhead, newtail = reverse_k_nodes(trav, k)
            
            prev.next = newhead
            newtail.next = beyound
            
            prev = trav
            trav = beyound
        
        prev.next = trav
        return dummy.next
