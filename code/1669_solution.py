class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        sentinel = ListNode(next=list1)
        
        def traverse(node, k):
            while node and k:
                node = node.next
                k -= 1
            return node
        
        def tail(node):
            while node.next:
                node = node.next
            return node
        
        prev = traverse(sentinel, a)
        post = traverse(prev, b - a + 2)
        prev.next = list2
        tail(list2).next = post
        return sentinel.next
