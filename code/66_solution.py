class Solution:
    def variant_1(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            digits[i] = 0
        else:
            digits[0] = 1
            digits.append(0)
        return digits

    def variant_2(self, digits, carry=1):
        i = len(digits) - 1
        while carry and i >= 0:
            carry, digits[i] = divmod(digits[i] + carry, 10)
            i -= 1
        return [carry] + digits if carry else digits
        
    plusOne = variant_2