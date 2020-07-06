#   0010   x << 1
# ^ 0100   x >> 1
# ^ 1111   mask 1
# ----------------------
#   1001
# & 0110   mask 2
# ----------------------
#   0000  


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        bits = len(cells)
        mask_1 = (1 << bits) - 1
        mask_2 = (mask_1 >> 1) - 1
        
        def get_next(state): # O(1) # O(K)
            # return tuple([0] + [i^j^1 for i, j in zip(state, state[2:])] + [0])
            state = (state << 1) ^ (state >> 1) ^ mask_1
            return state & mask_2
        
        def to_cells(state):
            cells = [0] * bits
            for i in range(bits):
                cells[~i] = state & 1
                state >>= 1
            return cells
        
        def to_state(cells):
            state = 0
            for i in range(bits):
                state += cells[i] << (bits - 1 - i)
            return state
        
        state = to_state(cells) # tuple(cells)
        memo = dict()
        # O(min(N, 2^(K-2)) * 1)
        while N: 
            if state in memo: break
            memo[state] = N
            N -= 1
            state = get_next(state)
        else: return to_cells(state) # state
        
        # O(2^(K-2) * 1)
        for _ in range(N % (memo[state] - N)): state = get_next(state)
        return to_cells(state) # state
            