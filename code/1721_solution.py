# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fast = head
        
        for _ in range(k-1):
            fast = fast.next
        p1 = fast
            
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        p2 = slow

        p1.val, p2.val = p2.val, p1.val
        return head
