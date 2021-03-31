# reverse the process
# slide stamp over the sequence, mask chars when we can stamp
# if one pass, nothing changed, terminate
# check if sequence is all masked. 


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target_length, stamp_length = len(target), len(stamp)
        sequence = list(target)
        stamped = '*'
        mask = [stamped] * stamp_length
        order = deque()
        
        def should_stamp(subseq, ignore=stamped):
            for c1, c2 in zip(subseq, stamp):
                if c1 == ignore: continue
                if c1 != c2: return False
            return True
        
        def try_stamp():
            prev_stamps = len(order)
            for i in range(target_length - stamp_length + 1):  # slide stamp over
                if sequence[i:i+stamp_length] == mask: continue
                if should_stamp(sequence[i:i+stamp_length]):
                    sequence[i:i+stamp_length] = mask # apply_stamp
                    order.appendleft(i)
            return len(order) > prev_stamps
            
        should_continue = True
        while should_continue:
            should_continue = try_stamp()
        
        if sequence != [stamped] * target_length: order = []
        return order
        
        
            
        
        
        
        
        
        
