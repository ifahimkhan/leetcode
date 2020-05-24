class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> numbers;
        for (int i=1;i<n/2+1;i++) numbers.insert(numbers.end(), initializer_list<int>{i, -i});
        if (n & 1) numbers.push_back(0);
        return numbers;
    }
};
