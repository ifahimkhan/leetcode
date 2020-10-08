class TwoSum(dict):
    def __init__(self):
        super().__init__()        

    def add(self, number: int) -> None:
        self.__setitem__(number, self.get(number, 0) + 1)
        
    def find(self, value: int) -> bool:
        for num in self.keys():
            complement = value - num
            if complement == num and self.__getitem__(num) > 1: return True
            if complement != num and self.__contains__(value - num): return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
