class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        for (auto num:nums) counter[num]++;
        vector<pair<int, int>> freq;
        for (auto [num, count]: counter) freq.push_back({num, count});

        auto partition = [&](int l, int r) {
            int m = l + (r - l) / 2;
            int pivot = freq[m].second;
            swap(freq[l], freq[m]);
            int i = l, j = r;
            while (i < j) {
                while (i < r and freq[i].second >= pivot) ++i;
                while (j > l and freq[j].second <= pivot) --j;
                if (i < j and freq[i].second < freq[j].second) swap(freq[i], freq[j]);                     
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
        
        vector<int> result;
        for (int i=0; i<k; i++) result.push_back(freq[i].first);
        return result;
    }
};