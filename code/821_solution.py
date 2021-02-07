class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        
        shortest_distances = [n] * n

        c_pos = -2 ** 32
        for i in range(n):
            if s[i] == c: c_pos = i
            shortest_distances[i] = min(shortest_distances[i], i - c_pos)
        
        print(shortest_distances)
        c_pos = 2**32
        for i in range(n-1, -1, -1):
            if s[i] == c: c_pos = i
            shortest_distances[i] = min(shortest_distances[i], c_pos - i)

        return shortest_distances
