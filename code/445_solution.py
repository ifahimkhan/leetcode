# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            if not head or not head.next: return head
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        def add(l1, l2):
            carry = 0
            ret = curr = ListNode(None)
            while l1 or l2 or carry:
                if l1:
                    carry += l1.val
                    l1 = l1.next
                if l2:
                    carry += l2.val
                    l2 = l2.next
                carry, val = divmod(carry, 10)
                curr.next = ListNode(val)
                curr = curr.next
            return ret.next        
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        l3 = add(l1, l2)
        l3 = reverse(l3)
        return l3
