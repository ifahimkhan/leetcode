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
        self.head = head

    def count(self):
        node = self.head
        num_nodes = 0
        while node:
            num_nodes += 1
            node = node.next
        return num_nodes
        
    def count_then_get(self):
        num_nodes = self.count()
        i = random.randint(1, num_nodes)
        node = self.head
        for _ in range(i):
            node = node.next
        return node.val        
    
    def reservoir_sampling(self):
        cnt = 0
        curr = self.head
        
        while curr:
            if random.randint(0, cnt) == cnt:
                val = curr.val
            curr = curr.next
            cnt += 1
        return val
    
    getRandom = reservoir_sampling # count_then_get
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
