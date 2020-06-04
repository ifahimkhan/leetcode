class Solution {
public:
    int calculateTime(string keyboard, string word) {
        unordered_map<char, int> key_loc;
        for (int i=0;i<keyboard.size();i++) key_loc[keyboard[i]] = i;
        int total = 0, prev = 0;
        for (char c:word) {
            total += abs(key_loc[c] - prev);
            prev = key_loc[c];
        }
        return total;
    }
};