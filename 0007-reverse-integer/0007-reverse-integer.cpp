class Solution {
public:
    int reverse(int x) {
        bool neg = x < 0;
        // if (neg) { x *= -1; }
        long double y = 0;
        while (abs(x) > 0) {
            y *= 10;
            y += x % 10;
            x /= 10;
        }
        return (y >= pow(-2.0,31.0) && y <= pow(2.0,31.0) - 1.0) ? y : 0;
    }
};