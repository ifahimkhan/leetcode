# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random

class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        # self.head = head
        # node = head
        # self.count = 0
        # while node:
        #     self.count += 1
        #     node = node.next
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # node = self.head
        # i = random.randint(0, self.count - 1)
        # for j in range(i):
        #     node = node.next
        # return node.val
        
        cnt = 0
        curr = self.head
        
        while curr:
            if random.randint(0, cnt) == cnt:
                val = curr.val
            curr = curr.next
            cnt += 1
        return val
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
