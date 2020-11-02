# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sentinal = ListNode()
        curr = head
        while curr:
            prev = sentinal
            next_ = prev.next
            while next_ and curr.val >= next_.val:
                prev = next_
                next_ = prev.next
            
            tmp = curr.next
            curr.next = next_
            prev.next = curr
            curr = tmp
        return sentinal.next
