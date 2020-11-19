class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        rep_stack = []
        curr_str = ''
        curr_rep = 0
        
        for char in s:
            if char.isdigit():
                curr_rep = 10 * curr_rep + int(char)
            elif char == '[':
                str_stack.append(curr_str)
                rep_stack.append(curr_rep)
                curr_str, curr_rep = '', 0
            elif char == ']':
                prev_rep = rep_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + curr_str * prev_rep
            else:
                curr_str += char
                
        return curr_str
