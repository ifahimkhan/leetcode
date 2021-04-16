class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_length = 0        
        stack = []
        
        for section in input.split('\n'):
            level, is_file = section.count('\t'), '.' in section
            while len(stack) > level:  stack.pop()
            stack.append(len(section) - int(level != 0) * (level - 1))
            if is_file: max_length = max(max_length, sum(stack))
            
        return max_length            
