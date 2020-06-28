class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # graph processing from edge list to adj_list
        flights = defaultdict(deque)
        for f, t in sorted(tickets):
            flights[f].append(t)    
            
        itn, stack = deque([]), ['JFK']
        while stack:
            while flights[stack[-1]]:
                stack.append(flights[stack[-1]].popleft())
            itn.appendleft(stack.pop())
        return itn
