# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

#                   [5,2] 0
#                     V
# [[], [4], [3], [], [5,2], []]


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Process from shortest to highest, pre-acllocate slots.
        # scan from left to right, use definition to find loction to place people.

        # queue = [[] for _ in range(len(people))]
        # people.sort() # O(NlogN)
        # # O(N^2)
        # for h, k in people:
        #     num_ge = 0
        #     for i, loc in enumerate(queue):
        #         if num_ge == k and not loc: 
        #             queue[i] = [h, k]
        #             break
        #         if not loc or loc[0] == h: num_ge += 1
        # return queue
        
        # or process people from highest to shortest.
        # At any given time, we only have ppl with ge height inserted.
        # so the k is now just the insertion point. 
        queue = list()
        for p in sorted(people, key=lambda x: [-x[0], x[1]]):
            queue.insert(p[1], p)
        return queue