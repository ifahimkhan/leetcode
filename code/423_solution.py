class Solution:
    def originalDigits(self, s: str) -> str:
        char_frequency = Counter(s)
        digits = [0] * 10
        
        digits[0] = char_frequency['z']
        digits[2] = char_frequency['w']
        digits[4] = char_frequency['u']
        digits[6] = char_frequency['x']
        digits[8] = char_frequency['g']
        
        digits[1] = char_frequency['o'] - digits[0] - digits[2] - digits[4]
        digits[3] = char_frequency['t'] - digits[2] - digits[8]
        digits[5] = char_frequency['f'] - digits[4]
        digits[7] = char_frequency['s'] - digits[6]
        
        digits[9] = char_frequency['i'] - digits[5] - digits[6] - digits[8]
        
        return ''.join([str(digit) * freq for digit, freq in enumerate(digits)])
