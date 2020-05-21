class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> last_loc;
        int l=0, max_length=0;
        for (int i=0;i<s.size();i++){
            char c=s[i];
            if (last_loc.count(c)) l = max(l, last_loc[c]+1);
            max_length = max(max_length, i - l + 1);
            last_loc[c] = i;
        }
        return max_length;
    }
};
