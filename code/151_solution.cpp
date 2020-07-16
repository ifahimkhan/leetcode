// the sky is blue
// // two pointers reverse
// eulb si yks eht
// // reverse individual words
//  eulb si yks eht
//  ^   ^
//  l   r
//  blue si yks eht
//       ^ ^ 
//       l r
//       ...
// blue is sky the

// // pop back to remove trailing space

// a good   example  word_length 7
//        ^        ^
//        l        it
// a good example 
//                ^
//                l


class Solution {
public:
    string reverseWords(string s) {
        // 1. remove multiple spaces between words by shiftting words to left
        auto r = s.begin(), l = s.begin();
        while (*r == ' ') ++r;
        while (r < s.end()) {
            int ws = 0;
            while (r < s.end() and *r != ' ') {
                ++r;
                ++ws;
            }
            while (ws) {
                swap(*l, *(r - ws));
                ++l;
                --ws;
            }
            ++l;
            while (r < s.end() and *r == ' ') ++r;
        }
        // 2. get rid of trailing spaces
        // while (*(s.end() -1) == ' ') s.pop_back();
        while (not s.empty() and s.back() == ' ') s.pop_back();

            
        // 3. reverse the string
        // l = s.begin(), r = s.end() - 1;
        // while (l < r) {
        //     swap(*l, *r);
        //     ++l;
        //     --r;
        // }
        reverse(s.begin(), s.end());
            
        // 4. reverse individual words
        l = s.begin();
        for (r = s.begin(); r <= s.end(); ++r) {
            if (*r == ' ' or r == s.end()) {
                reverse(l, r);
                l = r + 1;
            }
        }
        return s;
    }
};





