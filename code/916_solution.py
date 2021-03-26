class Solution:
    def solution(self, A: List[str], B: List[str]) -> List[str]:
        required = Counter()
        for b in B:
            for char, freq in Counter(b).items():
                required[char] = max(required[char], freq)
        
        filtered = []
        for a in A:
            supply = Counter(a)
            for char, freq in required.items():
                if supply[char] < freq: 
                    break
            else:
                filtered.append(a)
                
        return filtered
    
    
    def solution_simplified(self, A, B):
        required = Counter()
        for b in B: required |= Counter(b)
        return [a for a in A if Counter(a) & required == required]    
        
    
    wordSubsets = solution_simplified
