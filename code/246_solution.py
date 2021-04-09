class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {'6': '9', '9': '6', '8': '8', '0': '0', '1': '1'}
        strobo_number = []
        for d in num:
            if d not in mapping: return False
            strobo_number.append(mapping[d])
        return ''.join(reversed(strobo_number)) == num
