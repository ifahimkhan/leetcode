class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        auto lcp = [](string s1, string s2) {
            int i=0;
            while (i<s1.size() and s1[i] == s2[i]) i++;
            return s1.substr(0, i);
        };
        return strs.size() ? accumulate(strs.begin(), strs.end(), strs[0], lcp) : "";
    }
};
