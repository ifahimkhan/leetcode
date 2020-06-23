class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        freq_s, freq_g = [0] * 10, [0] * 10
        for s, g in zip(secret, guess): 
            if s == g: 
                bull += 1
            else:
                freq_s[int(s)] += 1
                freq_g[int(g)] += 1
        for s, g in zip(freq_s, freq_g): 
            cow += min(s, g)
        return '{}A{}B'.format(bull, cow)
