class Solution:
    def on_str_to_int(self, low, high):
        def num_digits(x):
            c = 0
            while x:
                x //= 10
                c += 1
            return c
        
        def make_number(s, num_digits):
            if s + num_digits > 10: return
            num = 0
            for i in range(num_digits):
                num = 10 * num + s + i
            return num
        
        numbers = []
        low_digits, high_digits = num_digits(low), num_digits(high)
        low_s = low // (10 ** (low_digits - 1))
        for num_digits in range(low_digits, high_digits + 1):
            for s in range(low_s, 10):
                number = make_number(s, num_digits)
                if not number or number < low: continue
                if number > high: break
                numbers.append(number)
            low_s = 1
        return numbers
    
    def str_to_int(self, low, high):
        digits = '123456789'
        numbers = []
        for num_digits in range(len(str(low)), len(str(high)) + 1):
            for s in range(10 - num_digits):
                number = int(digits[s: s + num_digits])
                if low <= number <= high: numbers.append(number)
        return numbers
        
    
    sequentialDigits = str_to_int # no_str_to_int
