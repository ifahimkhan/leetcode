class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = dict()
        self.l = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. 
        Returns true if the set did not already contain the specified element.
        """
        if val in self.m: return False
        self.m[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. 
        Returns true if the set contained the specified element.
        """
        if val not in self.m: return False
        l, m = self.l, self.m
        l[m[val]] = l[-1]
        m[l[-1]] = m[val]
        l.pop()
        m.pop(val)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()