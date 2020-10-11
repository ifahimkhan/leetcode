class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack, used = list(), set()
        for i, c in enumerate(s):
            if c in used: continue
            #    not empty & insert c reduce lexi & not the last one
            while stack and stack[-1] > c and i < last[stack[-1]]:
                used.remove(stack.pop())
            stack.append(c)
            used.add(c)
        return "".join(stack)
