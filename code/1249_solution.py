class Solution:    
    def solution_stack_and_set(self, s):
        stack = [] # keep track of unclosed open parentheses
        to_delete = set() # keep track of indices to delete
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  
            if char == ')':
                if not stack:
                    to_delete.add(i)
                else:
                    stack.pop()
        to_delete.update(stack)
        return ''.join([char for i, char in enumerate(s) if i not in to_delete])
    
    def solution_set_only(self, s):
        unclosed = 0
        num_closed = 0
        to_delete = set()
        for i, char in enumerate(s):
            if char == '(': 
                unclosed += 1
                
            if char == ')':
                if unclosed:
                    unclosed -= 1
                    num_closed += 1
                else:
                    to_delete.add(i)
        
        for i, char in enumerate(s):
            if char == '(':
                if num_closed:
                    num_closed -= 1
                else:
                    to_delete.add(i)
        
        return ''.join(char for i, char in enumerate(s) if i not in to_delete)
    
    minRemoveToMakeValid = solution_set_only # solution_stack_and_set
