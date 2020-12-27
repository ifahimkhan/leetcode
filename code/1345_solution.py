class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        num_idx = defaultdict(list)
        for idx, num in enumerate(arr):
            num_idx[num].append(idx)              
        
        pos_visited, num_visited = set(), set()
        queue = deque([(0, 0)])
        while queue:
            idx, step = queue.popleft()
            pos_visited.add(idx)
            num, neighbors = arr[idx], []
            
            if idx == n - 1: return step
            if idx - 1 >= 0: neighbors.append(idx - 1)
            if idx + 1 <= n - 1: neighbors.append(idx + 1)
            if num not in num_visited: neighbors.extend(num_idx[num])
                
            for neighbor in neighbors:
                if neighbor not in pos_visited:
                    queue.append((neighbor, step + 1))
            
            num_visited.add(num)
