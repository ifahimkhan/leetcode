class Solution {
public:
    int lengthOfLastWord(string s) {
        int r = s.size() - 1;
        while (r >= 0 and s[r] == ' ') r--;
        int l=r;
        while (l >= 0 and s[l] != ' ') l--;
        return r >= 0 ? r - l : 0;
    }
};
