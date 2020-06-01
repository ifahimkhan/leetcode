# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: return head
        def get_middle(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(head):
            prev, trav = None, head
            while trav:
                next_ = trav.next
                trav.next = prev
                prev = trav
                trav = next_
            return prev
        
        def merge_2_list(l1, l2):
            trav = ListNode(None)
            while l1 and l2:
                trav.next = l1
                l1 = l1.next
                trav = trav.next
                
                trav.next = l2
                l2 = l2.next
                trav = trav.next
            if l1: trav.next = l1
            
        l1_tail = get_middle(head)
        l2_head = l1_tail.next            
        l1_tail.next = None
        l2_head = reverse(l2_head)
        merge_2_list(head, l2_head)
