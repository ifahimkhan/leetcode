class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def length(p, q):
            return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** .5
        
        lengths = set()
        pairs = ((p1, p2), (p1, p3), (p1, p4), (p2, p3), (p2, p4), (p3, p4))
        for p, q in pairs:
            lengths.add(length(p, q))
        return len(lengths) == 2 and 0 not in lengths
