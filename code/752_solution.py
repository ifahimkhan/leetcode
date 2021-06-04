class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        def turn(wheel):
            return str((int(wheel) - 1) % 10), str((int(wheel) + 1) % 10)
                    
        def get_next_states(state):
            states = []
            for i in range(len(state)):
                states.extend([state[:i] + wheel + state[i+1:] 
                               for wheel in turn(state[i])])
            return states
            
        seen = set()
        queue = deque([('0000', 0)])
        while queue:
            state, turns = queue.popleft()
            if state in seen or state in deadends:  continue
            if state == target: return turns
            seen.add(state)
            queue.extend([(new_state, turns + 1) for new_state in get_next_states(state)])
        return -1
