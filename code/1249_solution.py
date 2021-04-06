class Solution:
    def solution_stack_and_set(self, s):
        stack = [] # keep track of unclosed open parentheses
        to_delete = set() # keep track of indices to delete
        for i, char in enumerate(s):  # first pass
            if char == '(':
                stack.append(i)  
            if char == ')':
                if not stack:
                    to_delete.add(i)
                else:
                    stack.pop()
        to_delete.update(stack)
        return ''.join([char for i, char in enumerate(s) if i not in to_delete]) # second pass
    
    
    def solution_stack_only(self, s: str) -> str:
        result = []
        capacity = s.count(')')  # first pass
        opened = 0
        for char in s:  # second pass
            if char == '(':
                if opened == capacity: continue              
                opened += 1
            elif char == ')':
                capacity -= 1
                if not opened: continue
                opened -= 1
            result.append(char)
        return ''.join(result) # third pass
       
    minRemoveToMakeValid = solution_stack_and_set # solution_stack_only
