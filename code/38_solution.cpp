class Solution {
private:
    string transform(string s) {
        char prev = s[0];
        int count = 1;
        string result = "";
        for (int i=1;i<s.size();i++){
            char curr = s[i];
            if (curr == prev) count++;
            else {
                result += to_string(count);
                result.push_back(prev);
                count = 1;
                prev = curr;
            }
        }
        result += to_string(count);
        result.push_back(prev);
        return result;
    }
    
public:
    string countAndSay(int n) {
        string result = "1";
        for (int i=1;i<n;i++) result = transform(result);
        return result;
    }
};
