class Solution {
public:
    bool isPalindrome(int x) {
        stringstream ss;
        ss << x;
        string s = "";
        ss >> s;
        int l = 0;
        int r = s.length()-1;
        while (r > l) {
            if (s[r] != s[l]) {
                return false;
            }
            r--; l++;
        }
        return true;
    }
};