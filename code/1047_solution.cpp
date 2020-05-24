class Solution {
public:
    string removeDuplicates(string S) {
        string s = "";
        for (char c:S){
            if (s.size() and s.back() == c) s.pop_back();
            else s.push_back(c);
        }
        return s;
    }
};
