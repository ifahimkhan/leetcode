# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):       
        while True:
            over_five = rand7()
            if over_five != 7: break
        over_five = 1 if over_five & 1 else 0
        
        while True:
            rand5 = rand7()
            if rand5 <= 5: break
        return 5 * over_five + rand5
