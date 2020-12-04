class Solution:
    def brute_force(self, n, k):
        for i in range(1, n+1):
            if not n % i: 
                k -= 1
                if not k: return i 
        return -1
    
    def math(self, n, k):
        divisors = []
        for i in range(1, int(n ** .5) + 1):
            if not n % i:
                k -= 1
                divisors.append(i)
                if not k: return i
        if divisors[-1] ** 2 == n: k += 1
        if k <= len(divisors): return n // divisors[-k]
        return -1
        
    kthFactor = math # rute_force
