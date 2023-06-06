class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stac;
        int pointer = 0;
        stac.push(s[0]);
        while (++pointer < s.size()) {
            char c = s[pointer];
            if (c == '(' || c == '{' || c == '[') {
                stac.push(c);
            }
            if (c == ')') {
                if (stac.empty() || stac.top() != '(') {
                    return false;
                }
                else {
                    stac.pop();
                }
            }
            else if (c == ']') {
                if (stac.empty() || stac.top() != '[') {
                    return false;
                }
                else {
                    stac.pop();
                }
            }
            else if (c == '}') {
                if (stac.empty() || stac.top() != '{') {
                    return false;
                }
                else {
                    stac.pop();
                }
            }
        }
        if (stac.empty()) {
            return true;
        }
        return false;
    }
};