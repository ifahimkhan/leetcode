class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        int n=0;
        for (char c:S) n+=(isalpha(c) > 0);
        vector<string> result;
        for (int mask=0;mask<(1<<n);mask++){
            string s;
            int i=0;
            for (char c:S){
                if (isalpha(c)==0) s.push_back(c);
                else {
                    s.push_back((mask & (1<<i))? toupper(c) : tolower(c));
                    i++;
                }
            }
            result.push_back(s);
        }
        return result;
    }
};