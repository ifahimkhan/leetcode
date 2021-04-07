# from 
# 2 [2,3, 5]
# 1 [1, 4] 
# [x, 1, 2, 2, 1, 2]

# remove(1)

# to

# 2 [2,3, 4]
# 1 [1] 
# [x, 1, 2, 2, 2]


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = defaultdict(set)  
        self.numbers = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.lookup[val].add(len(self.numbers))
        self.numbers.append(val)
        return len(self.lookup[val]) == 1
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.lookup[val]) == 0: return False
        pos = self.lookup[val].pop()
        tail_val = self.numbers[-1]
        self.numbers[pos] = tail_val
        self.numbers.pop()
        self.lookup[tail_val].add(pos)
        self.lookup[tail_val].discard(len(self.numbers))
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        i = random.randint(0, len(self.numbers)-1)
        return self.numbers[i]
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
