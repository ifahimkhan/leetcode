// s = "a b  c" 
//           i
// t = "ahbgdc"
//         j

// 'a' = [0]
// 'b' = [1,5,9]
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i=0;
        for (char c:s) {
            while (i < t.size() and t[i] != c) ++i;     
            if (i == t.size()) return false;
            ++i;
        }
        return true;
    }
};