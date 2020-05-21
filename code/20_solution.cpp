class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> match({{'{','}'}, {'[',']'}, {'(',')'}});
        stack<char> open;
        for (char c: s) {
            if (match.count(c)) open.push(c); 
            else if (open.empty() or match[open.top()] != c) return false;
            else open.pop();
        }
        return open.empty();
    }
};
