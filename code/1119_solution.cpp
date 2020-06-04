class Solution {
public:
    string removeVowels(string S) {
        int i=0;
        unordered_set<char> vowels = {'a','e','i','o','u'};
        while (i<S.size()) {
            if (vowels.count(S[i])) S.erase(i, 1);
            else i++;
        }
        return S;
    }
};