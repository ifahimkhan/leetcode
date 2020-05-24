class Solution {
public:
    vector<int> arraysIntersection(vector<int>& arr1, vector<int>& arr2, vector<int>& arr3) {
        int i=0,j=0,k=0;
        vector<int> intersection;
        while (i<arr1.size() and j<arr2.size() and k<arr3.size()) {
            while (j<arr2.size() and arr2[j] < arr1[i]) j++;
            while (k<arr3.size() and arr3[k] < arr1[i]) k++;
            if (j==arr2.size() or k==arr3.size()) break;
            if (arr1[i] == arr2[j] and arr2[j] == arr3[k]) intersection.push_back(arr1[i]);
            i++;
        }
        return intersection;
    }
};
