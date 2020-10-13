# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None: return None
        
        def count_nodes(node):
            total = 0
            while node:
                total +=1
                node = node.next
            return total
        
        def split(node, step):
            i = 1
            while i < step and node:
                node = node.next
                i += 1
                
            if node is None: return None
            temp, node.next = node.next, None
            return temp
        
        def merge(l, r, node):
            while l and r:
                if l.val < r.val: node.next, l = l, l.next
                else: node.next, r = r, r.next
                node = node.next
            
            node.next = l if l is not None else r
            while node.next: node = node.next
            return node

        size = count_nodes(head)
        current_size = 1
        
        sentinel = ListNode(None)
        sentinel.next = head
        
        while current_size < size:
            node = sentinel.next
            tail = sentinel
            while node:
                l = node
                r = split(l, current_size)
                node = split(r, current_size)
                tail = merge(l, r, tail)
            current_size *= 2
        return sentinel.next
