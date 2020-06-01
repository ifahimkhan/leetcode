# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack, result = [], []
        n = 0
        while head:
            while stack and stack[-1][0] < head.val:
                result[stack.pop()[1]] = head.val
            result.append(0)
            stack.append((head.val, n))
            n += 1
            head = head.next
        return result
