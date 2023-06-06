class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map; // (char, index)
        int longest = 0;
        int start = 0;
        for (int i = 0; i < s.length(); i++) {
            if (map.find(s[i]) != map.end() && map[s[i]] >= start) {
                // move start to 1 past the index of map
                start = map[s[i]] + 1;
            }
            map[s[i]] = i;
            if (i - start + 1 > longest) {
                longest = i - start + 1;
            }
        }
        return longest;
    }
};