class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        sim_pairs = defaultdict(set)
        for w1, w2 in similarPairs:
            sim_pairs[w1].add(w2)
            sim_pairs[w2].add(w1)
            
        if len(sentence1) != len(sentence2): return False
        
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2: continue
            if w2 not in sim_pairs[w1]: return False
        return True
