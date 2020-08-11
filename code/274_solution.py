class Solution:
    def h_index_by_sort(self, citations):
        # O(NlogN) time for sort, O(logN) time for binary search. 
        # O(1) space if inplace sort, O(N) otherwise.
        citations.sort()
        if not citations or citations[-1] == 0: return 0
        N = len(citations)
        l, h = 0, N - 1
        while l < h:
            i = (l + h) // 2
            if N - i > citations[i]: l = i + 1
            else: h = i
        return N - l 
    

    def h_index_by_count(self, citations):
        # O(N) time O(N) space. 
        N = len(citations)
        papers_with_citation = [0] * (N + 1)
        for citation in citations:
            papers_with_citation[min(N, citation)] += 1
        
        h = N
        accum = 0
        for num_papers in reversed(papers_with_citation):
            accum += num_papers
            if h <= accum: break
            h -= 1            
        return h
    
    hIndex = h_index_by_count # h_index_by_sort
