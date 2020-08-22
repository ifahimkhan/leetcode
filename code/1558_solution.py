class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return set(range(n)).difference(map(lambda x: x[1], edges))

# code is easy. should prove it.