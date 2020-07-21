class Solution {
public:
    string reverseWords(string s) {
        // 1. reverse individual words and make sure words are one space apart
        auto r = s.begin(), l = s.begin();
        while (*r == ' ') ++r; // find the start of the first word
        while (r < s.end()) {
            // move r to the first space after the current word
            int ws = 0;
            while (r < s.end() and *r != ' ') {
                ++r;
                ++ws;
            }
            // swap to reverse the word and make it start at l
            // very tricky, reverse(l, r) would work indeed, 
            // but will become O(N^2) time for cases with lots of multiple spaces
            auto ll = l, rr = r - 1;
            int n = min(ws, (int)((r - l) /2));
            while (n) {
                swap(*ll, *rr);
                ++ll;
                --rr;
                --n;
            }
            
            // move l to the second position after end of the word
            l += ws + 1;
            
            // move r to the start of next word
            while (r < s.end() and *r == ' ') ++r;
        }

        // 2. get rid of trailing spaces
        while (not s.empty() and s.back() == ' ') s.pop_back();
            
        // 3. reverse the string
        reverse(s.begin(), s.end());
        return s;
    }
};
