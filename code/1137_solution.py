# class Solution:
#     def tribonacci(self, n: int) -> int:
#         numbers = [0, 1, 1]
#         if n <= 2: return numbers[n]
#         for i in range(2, n):
#             new_number = sum(numbers)
#             numbers[0] = numbers[1]
#             numbers[1] = numbers[2]
#             numbers[2] = new_number
#         return new_number


class Solution:
    def __init__(self):
        numbers = [0, 1, 1]
        for i in range(2, 38):
            numbers.append(sum(numbers[-3:]))
        self.numbers = numbers
        
    def tribonacci(self, n):
        return self.numbers[n]
        
    
