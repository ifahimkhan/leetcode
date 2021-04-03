class Solution:
    def bfs(self, n: int) -> int:
        # brute force, but totally doable in interview
        if n == 1: return 0
        queue = deque([('C', 1, 1)])
        i = 1
        while queue:
            for _ in range(len(queue)):
                prev_op, prev_total, copied = queue.popleft()
                if prev_total == n: return i
                if prev_total > n: continue
                if prev_op == 'C': 
                    # can only paste now
                    queue.append(['P', prev_total + copied, copied])
                else:
                    # paste
                    queue.append(['P', prev_total + copied, copied])
                    # copy
                    queue.append(['C', prev_total, prev_total])
            i += 1            
    
    def prime_factor(self, n):
        # top-down reduce n to 1
        # the sequence of operations has a pattern is [Init]->[CP]Xa->[CPP]Xb->[CPPPP]Xc 
        
        # [Init]->[CPPP]x1 = 'A' * 4 takes 4 operations
        # can be factored down to 
        # [Init]->[CP]x2 = 'A' * 4 takes 4 operations also 

        # [Init]->[CPPPPPPPPP]x1 = 'A' * 10 takes 10 operations
        # can be factored down to
        # [Init]->[CP][CPPPP] = 'A' * 10 takes 6 operations also 
        
        # that is the optimal sequence of operations consists fo sections which have prime number length
        # otherwise that section can be broken into smaller sequences without increasing total length 
        
        # need to prove this observation 
        
        total = 0
        r = 2
        while n != 1:
            while not n % r:
                total += r
                n /= r
            r += 1
        return total     
    
    minSteps = prime_factor #, bfs
