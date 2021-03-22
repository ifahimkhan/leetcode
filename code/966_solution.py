class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set('aeiouAEIOU')
        
        def mask_vowels(s):
            return ''.join(['_' if c in vowels else c for c in s])
        
        word_set = {w:w for w in wordlist}
        lowercase_lookup = dict()
        masked_lookup = dict()
        
        for word in wordlist:
            if word.lower() not in lowercase_lookup: 
                lowercase_lookup[word.lower()] = word
            if mask_vowels(word).lower() not in masked_lookup:
                masked_lookup[mask_vowels(word).lower()] = word
                
        responses = [
            word_set.get(query, '') or
            lowercase_lookup.get(query.lower(), '') or
            masked_lookup.get(mask_vowels(query).lower(), '')
            for query in queries
        ] 
        
        return responses
