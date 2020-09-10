class Solution:
    def two_pass(self, secret, guess):
        bull, cow = 0, 0
        freq_s, freq_g = [0] * 10, [0] * 10
        for s, g in zip(secret, guess): 
            if s == g: 
                bull += 1
            else:
                freq_s[int(s)] += 1
                freq_g[int(g)] += 1
        for s, g in zip(freq_s, freq_g): cow += min(s, g)
        return '{}A{}B'.format(bull, cow)        
    
    def one_pass(self, secret, guess):
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
    
    getHint = one_pass # two_pass
