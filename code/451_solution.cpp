class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> char_freq;
        int max_freq = 0;
        for (auto c:s) {
            char_freq[c]++;   
            max_freq = max(max_freq, char_freq[c]);
        }
        
        unordered_map<int, vector<char>> buckets;
        for (auto t:char_freq) {
            int freq = t.second;
            char c = t.first;
            if (not buckets.count(freq)) buckets[freq] = {c};
            else buckets[freq].push_back(c);
        }
        
        string result;
        for (int i=max_freq;i;i--) {
            if (buckets.count(i)) {
                for (char c:buckets[i]) result += string(i, c);
            }
        }
        return result;
    }
};