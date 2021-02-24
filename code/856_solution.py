class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        mapping = {
            '((': '2*(',
            '()': '1',
            ')(': '+',
            '))': ')'
        }
        return eval(''.join([mapping[pair] for pair in map(lambda x:''.join(x), zip(S, S[1:]))]))
            
