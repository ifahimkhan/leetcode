INT_MAX = 2 ** 32

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        dp = [INT_MAX] * (1 << n) # dp[i]: has ith char in target been satisfied or not. 
        dp[0] = 0
    
        def get_next_state(state, sticker):
            n = len(target)
            for char in sticker:
                for i in range(n):
                    if ((state >> i) & 1) == 0 and target[i] == char:
                        state += 1 << i
                        break
            return state
           
        # that latter state can only be reached from previous state, thus this for loop guarantee all situations be considered. 
        for state in range(1 << n):  
            if dp[state] == INT_MAX: continue
            for sticker in stickers:
                new_state = get_next_state(state, sticker)
                dp[new_state] = min(dp[new_state], dp[state] + 1)

        return -1 if dp[-1] == INT_MAX else dp[-1]
