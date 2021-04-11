class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = deque()
        quotient = columnNumber
        
        while quotient:
            quotient -= 1
            quotient, remainder = divmod(quotient, 26)
            title.appendleft(chr(remainder + 65))
        return ''.join(title)
