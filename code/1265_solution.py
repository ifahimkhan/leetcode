# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def solution_stack(self, head):
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.getNext()
        
        while stack:
            node = stack.pop()
            node.printValue()
        
    def solution_constant_space(self, head, n=None):
        if n is None:
            n = 0
            node = head
            while node:
                node = node.getNext()
                n += 1
        
        while n:
            node = head
            for _ in range(n-1):
                node = node.getNext()
            node.printValue()
            n -= 1
            
    def solution_final(self, head):
        n = 0
        node = head
        while node:
            node = node.getNext()
            n += 1

        section_size = int(n ** .5) + 1
        section_heads = []
        section_lengths = [] 
        node, i = head, 0
        while node:
            if i % section_size == 0:
                section_heads.append(node)
                section_lengths.append(section_size)
            node = node.getNext()
            i += 1
        section_lengths[-1] = n - sum(section_lengths[:-1])
        
        for section_head, section_length in zip(reversed(section_heads), reversed(section_lengths)):
            self.solution_constant_space(section_head, section_length)
        
    
    printLinkedListInReverse = solution_final # solution_constant_space # solution_stack
