class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        def traverse(node, k):
            while node and k:
                node = node.next 
                k -= 1
            return node
        
        node = sentinel = ListNode(next=head)
        while node:
            node = traverse(node, m)
            if node: node.next = traverse(node, n + 1)
        return sentinel.next
