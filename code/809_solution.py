class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        total = 0
        
        def rle(s):
            if not s: return [], []
            chars, counts, count = [], [], 0
            for i, char in enumerate(s):
                if not chars:
                    chars.append(char)
                elif char != chars[-1]:
                    counts.append(count)
                    chars.append(char)
                    count = 0
                count += 1
            counts.append(count)
            return chars, counts

        s_chars, s_counts = rle(S)
        for word in words:
            if len(word) > len(S): continue
            w_chars, w_counts = rle(word)
            if len(s_chars) != len(w_chars): continue
            for (s_char, w_char, s_count, w_count) in zip(s_chars, w_chars, s_counts, w_counts):
                if s_char == w_char:
                    if s_count == w_count: continue
                    elif s_count < w_count: break
                    elif s_count >= 3: continue
                    else: break
                else:
                    break
            else:
                total += 1
        return total
