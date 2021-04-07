class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[~0][0] != char:
                stack.append([char, 1])
            else:
                stack.append([stack[~0][0], 1 + stack[~0][1]])

            if stack[~0][1] % k == 0:
                for _ in range(k):
                    stack.pop()
        return ''.join([char for char, _ in stack])
