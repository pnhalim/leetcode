class Solution {
public:    
    int getSum(int a, int b) {
        int carry = (a & b) << 1;
        int normal = (a ^ b);
        while (carry != 0b0) {
            a = carry;
            b = normal;
            carry = (a & b) << 1;
            normal = (a ^ b);
        }
        return normal;
    }
};
