class Solution {
public:
    string longestDupSubstring(string S) {
        auto find_duplicate = [&S](int L){
            unordered_set<string_view> seen;
            for (int i=0;i+L<=S.size();i++) {
                auto [it, inserted] = seen.emplace(S.data() + i, L);
                if (not inserted) return i;
            }
            return -1;
        };
        
        int l=1, h=S.size();        
        while (l < h) {
            int m = l + (h - l) / 2;
            if (find_duplicate(m) != -1) l = m + 1;
            else h = m;
        }
        int i = find_duplicate(l - 1);
        return S.substr(i, l-1);
    }
};
