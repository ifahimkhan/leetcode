class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowels{'a','e','i','o','u','A','E','I','O','U'};
        int l=0,r=s.size()-1;
        while (l < r) {
            if (vowels.count(s[l]) and vowels.count(s[r])) {
                swap(s[l], s[r]);
                l++;
                r--;
            }
            if (not vowels.count(s[l])) l++;
            if (not vowels.count(s[r])) r--;
        }
        return s;
    }
};
