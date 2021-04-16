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
        
        def has_k_nodes(curr, k):
            while curr and k:
                curr = curr.next
                k -= 1
            return k == 0
        
        def reverse_k_nodes(curr, k):
            tail = curr
            prev = None
            for i in range(k): curr.next, prev, curr = prev, curr, curr.next
            return curr, prev, tail
        
        sentinel = prev = ListNode(None)
        sentinel.next = curr = head
        while has_k_nodes(curr, k):
            next_curr, new_head, new_tail = reverse_k_nodes(curr, k)
            
            prev.next = new_head
            new_tail.next = next_curr
            
            prev = curr
            curr = next_curr
        
        prev.next = curr
        return sentinel.next
