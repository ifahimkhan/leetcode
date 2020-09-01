class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        i = j = 0
        last_star = tmp = -1

        while i < len_s:
            if j < len_p and p[j] in ['?', s[i]]:
                i += 1
                j += 1
            elif j < len_p and p[j] == '*': 
                last_star = j
                tmp = i
                j += 1
            elif last_star == -1: 
                return False
            else:
                j = last_star + 1
                i = tmp + 1
                tmp = i
        return all(x == '*' for x in p[j:])
