class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def make_key(t):
            i, x = t
            identifier, words = x.split(' ', maxsplit=1)
            return words[0].isnumeric() * i, words, identifier
        
        logs = [(i, x) for i, x in enumerate(logs, 1)]
        logs.sort(key=make_key)
        return [log[1] for log in logs]
