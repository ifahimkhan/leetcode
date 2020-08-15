class Solution {
public:
    vector<int> findPermutation(string s) {
        vector<int> secret;
        for (int i = 0; i <= s.size(); ++i) {
            if (i == s.size() || s[i] == 'I') {
                int n = secret.size();
                for (int j = i + 1; j > n; --j) {
                    secret.push_back(j);
                }
            }
        }
        return secret; 
    }
};
