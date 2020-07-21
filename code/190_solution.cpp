class Solution {
    vector<uint8_t> mapping;
public:
    Solution() {mapping.resize(256,0);};
    
    uint8_t reverseByte(uint8_t n) {
        if (not mapping[n] and n) {
            uint8_t r=0;
            for (int i=0;i<8;i++) {
                r = (r << 1) | ((n >> i) & 1);
            };
            mapping[n] = r;
        }
        return mapping[n];
    }
    
    uint32_t reverseBits(uint32_t n) {
        uint32_t r = 0;
        r |= reverseByte((n >> 0) & 0b11111111) << 24;
        r |= reverseByte((n >> 8) & 0b11111111) << 16;
        r |= reverseByte((n >> 16) & 0b11111111) << 8;
        r |= reverseByte((n >> 24) & 0b11111111) << 0;
        return r;
    }    
};

// 12345678
// 21436587
// 43218765
// 87654321    
