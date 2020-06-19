class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def match(query):
            i = 0
            
            # match the pattern
            for c in pattern:
                while i < len(query) and query[i].islower() and query[i] != c: i += 1
                if i == len(query): return False
                if c.isupper() and query[i] != c: return False
                i += 1                
                
            # check for additional Uppercase letter after match
            return all(char.islower() for char in query[i:])
        
        return list(map(match, queries))