class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        balance = [0] * 10
        for s, g in zip(secret, guess): 
            if s == g: 
                bull += 1
            else:
                freq_s[int(s)] += 1
                freq_g[int(g)] -= 1
                cow += int(freq[int(s)] < 0)
                cow += int(freq[int(g)] > 0)
        return '{}A{}B'.format(bull, cow)


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        balance = [0] * 10
        for s, g in zip(secret, guess): 
            if s == g: 
                bull += 1
            else:
                balance[int(s)] += 1
                balance[int(g)] -= 1
                cow += int(balance[int(s)] <= 0)
                cow += int(balance[int(g)] >= 0)
        return '{}A{}B'.format(bull, cow)
