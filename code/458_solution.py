class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        '''
        arrange buckets as a k-dimentional cube.
        have pigs to test one row per dim. 
        whole process should be finished within given time requirement. 
        And we can test one less. 
            ie cube is 1x1, we don't need to test
               cube is 2x2, we only need to test first row and column
               etc. 
        so k = minutesToTest // minutesToDie + 1  (1)
        and num_pig ^ k > num_buckets             (2)
        solve for num_pig
        '''
        dim = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets, dim))
