class Solution {
public:
    string longestPalindrome(string s) {
        int left_ans = 0;
        int right_ans = 0;
        // look for odd palindromes
        for (int i = 0; i < s.length(); i++) {
            int left = i - 1;
            int right = i + 1;
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                left--; 
                right++;
            }
            left++; 
            right--;
            if (right-left > right_ans-left_ans) {
                right_ans = right;
                left_ans = left;
            }
        }
        // look for even palindromes
        for (int i = 0; i < s.length(); i++) {
            int left = i;
            int right = i + 1;
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                left--; 
                right++;
            }
            left++; 
            right--;
            if (right-left > right_ans-left_ans) {
                right_ans = right;
                left_ans = left;
            }
        }
        
        return s.substr(left_ans, right_ans-left_ans + 1);
    }
};