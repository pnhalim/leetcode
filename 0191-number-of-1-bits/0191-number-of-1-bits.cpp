class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n != 0b0) {
            if (n & 0b1) {
                count++;
            }
            n = n>>1;
        }
        return count;
    }
};