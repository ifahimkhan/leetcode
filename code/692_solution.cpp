class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> counter;
        for (auto word:words) counter[word]++;
        vector<pair<string, int>> freq;
        for (auto [word, count]: counter) freq.push_back({word, count});

        auto comparator = [&](int i, int j) {
            if (freq[j].second == freq[i].second) return freq[i].first < freq[j].first;
            else return freq[i].second > freq[j].second; 
        };
        
        auto partition = [&](int l, int r) {
            int m = l + (r - l) / 2;
            swap(freq[l], freq[m]);
            int i = l, j = r;
            while (i < j) {
                while (i < r and comparator(i, l)) ++i;
                while (j > l and comparator(l, j)) --j;
                if (i < j and comparator(j, i)) swap(freq[i], freq[j]);                     
            }   
            swap(freq[j], freq[l]); 
            return j;
        };
        
        function<void(int, int, int)> quickselect = [&](int l, int r, int k) {
            int m = partition(l, r);
            int d = m - l + 1;
            if (d == k) return;
            if (d < k) quickselect(m+1, r, k-d);
            if (d > k) quickselect(l, m-1, k);
        };
        
        quickselect(0, freq.size()-1, k);
        
        vector<string> result;
        for (int i=0; i<k; i++) result.push_back(freq[i].first);
        return result;        
    }
};