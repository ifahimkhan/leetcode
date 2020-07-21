# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#    ------|
#    |     V
# 1->2  6->3->4->5->6
#          ^  ^
      #  prev next_

#     ----------|
#     |         V
#  sentinel  6->5 -> ... -> nullptr
#     ^         ^
#   prev        next_
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(None, head)
        prev = sentinel
        next_ = head
        while next_:
            # 1. find the next keep node
            while next_ and next_.val == val: next_ = next_.next
            # 2. rewire
            prev.next = next_
            # 3. advance
            prev = next_
            if next_: next_ = next_.next
        return sentinel.next