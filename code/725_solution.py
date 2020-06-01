# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root: return [None] * k
        
        def count_nodes(head):
            n = 0
            while head:
                n += 1
                head = head.next
            return n

        def split(head, size):
            prev, trav = None, head
            while size:
                prev = trav
                trav = trav.next
                size -= 1
            if prev: prev.next = None 
            return head, trav            
        
        n = count_nodes(root)
        base_size, extra = divmod(n, k)
        
        heads = []
        for i in range(k):
            size = base_size + 1 if i < extra else base_size
            old_head, root = split(root, size)
            heads.append(old_head)
        return heads
