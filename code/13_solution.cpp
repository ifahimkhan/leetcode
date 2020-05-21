class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> mapping({
            {'M',1000}, 
            {'D',500}, 
            {'C',100}, 
            {'L',50}, 
            {'X',10}, 
            {'V',5}, 
            {'I',1}
        });
        int total = 0;
        for (int i=1;i<s.size();i++){
            int ln = mapping[s[i-1]], rn = mapping[s[i]];
            total += (ln < rn) ? -ln : ln;
        }
        return total + mapping[s[s.size()-1]];
    }
};
