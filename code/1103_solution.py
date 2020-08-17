class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        # figure out how many complete rounds we can do
        total, k = 0, 0
        next_round = n * (n + 1) / 2 + k * n ** 2
        while total + next_round < candies:
            total += next_round
            k += 1
            next_round = n * (n + 1) / 2 + k * n ** 2
        
        # do complete rounds just figured out
        dist = [(i + 1) * k + k * (k - 1) * n / 2 for i in range(n)]
        candies -= total
        
        # finish the last round
        i = 0
        while candies > 0:
            distribution = i + 1 + k * n
            dist[i] += min(candies, distribution)
            candies -= distribution
            i += 1
        return list(map(int, dist))

    
