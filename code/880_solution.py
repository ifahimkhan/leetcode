class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        n = i = 0
        
        # find the sub pattern long enough for K
        while n < K:
            if S[i].isalpha(): 
                n += 1
            else: 
                n *= int(S[i])
            i += 1
        
        # locate the Kth char in the sub pattern        
        for j in range(i - 1, -1, -1):
            if S[j].isdigit():
                n /= int(S[j])
                K %= n
            else:
                if not (K % n): return S[j]
                n -= 1
