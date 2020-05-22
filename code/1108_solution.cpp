class Solution {
public:
    string defangIPaddr(string address) {
        string formatted_address;
        for (char c:address) {
            if (c == '.') formatted_address += "[.]";
            else formatted_address.push_back(c);
        }
        return formatted_address;
    }
};
