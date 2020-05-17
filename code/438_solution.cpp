class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.size() < p.size()) return {};
        unordered_map<char, int> req_freq, window;
        for (char c:p) req_freq[c]++;
        for (int i=0;i<p.size();i++) if (req_freq.count(s[i])) window[s[i]]++;
        int to_match = req_freq.size();
        for (auto kv:window) to_match -= kv.second == req_freq[kv.first];
        if (not to_match) result.push_back(0);
        for (int r=p.size(),l=0;r<s.size();r++,l++){
            char in_char=s[r], out_char=s[l];
            if (req_freq.count(in_char)) {
                if (window[in_char] == req_freq[in_char]) to_match++;
                if (window[in_char]+1==req_freq[in_char]) to_match--;
                window[in_char]++;
            }
            if (req_freq.count(out_char)){
                if (window[out_char] == req_freq[out_char]) to_match++;
                if (window[out_char]-1==req_freq[out_char]) to_match--;
                window[out_char]--;
            }
            if (not to_match) result.push_back(l+1);
        }
        return result;
    }
};