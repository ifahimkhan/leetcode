class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = ''
        while numbers:
            if num < numbers[0]:
                numbers.pop(0)
                symbols.pop(0)
            else:
                while num >= numbers[0]:
                    result += symbols[0]
                    num -= numbers[0]
        return result
