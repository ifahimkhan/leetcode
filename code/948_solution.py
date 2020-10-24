class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = collections.deque(sorted(tokens))
        max_score, score = 0, 0
        while tokens and (P >= tokens[0] or score >= 1):
            while tokens and P >= tokens[0]:
                P -= tokens.popleft()
                score += 1
            max_score = max(max_score, score)

            if tokens and score >= 1:
                P += tokens.pop()
                score -= 1
        return max_score
