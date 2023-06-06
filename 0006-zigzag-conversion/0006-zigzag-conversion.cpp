class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) { return s; }

        string answ = "";

        int colGap = numRows*2 - 2;

        for (int r = 0; r < numRows; r++) {
            for (int i = 0; i < s.length(); i++) {
                if ((i+r) % colGap == 0 || (i-r) % colGap == 0) {
                    answ += s[i];
                }
            }
        }

        return answ;
    }
};