class Solution {
public:
    int myAtoi(string s) {
        stringstream ss; 
        ss << s;
        int result = 0;
        ss >> result;
        return result;

        /*
        double answ = 0;
        int i = 0;
        bool neg = false;
        // read 0s and sign
        while (i < s.length()) {
            if (s[i] == '-') {
                neg = true;
                break;
            }
            else if (s[i] == '+') {
                break;
            }
            else if (s[i] != '0') {
                break;
            }
            i++;
        }
        // read the number
        while (i < s.length()) {
            if (s[i] < '0' || s[i] > '9') { break; }
            answ *= 10;
            answ += atoi(&s[i]);
            i++;
        }
        cout << answ;
        return 1;
        */
    }
};