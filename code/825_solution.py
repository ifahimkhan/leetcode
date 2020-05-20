class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # def friendRequest(a, b):
        #     if b <= .5 * a + 7: return False
        #     if b > a: return False
        #     return True
        
        # age_groups = collections.Counter(ages)
        # total_requsts = 0
        # for a, num_a in age_groups.items():
        #     for b, num_b in age_groups.items():
        #         if friendRequest(a, b):
        #             total_requsts += num_a * num_b
        #             if a == b: total_requsts -= num_a
        # return total_requsts
        age_groups = [0] * 121
        for age in ages: age_groups[age] += 1
        total = 0
        for a, num_a in enumerate(age_groups):
            l = a // 2 + 8
            h = a + 1
            total += sum(age_groups[l:h]) * num_a
            if l <= a < h: total -= num_a
        return total