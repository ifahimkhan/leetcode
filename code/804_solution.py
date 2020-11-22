class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        char_to_codes = dict(zip(
                list('abcdefghijklmnopqrstuvwxyz'),
                [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
                 "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            ))
        return len(set(["".join(char_to_codes[char] for char in word) for word in words]))
