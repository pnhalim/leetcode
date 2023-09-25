class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        curr_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1
        max_count = curr_count
        for i in range(1, len(s)-k+1):
            if s[i-1] in vowels:
                curr_count -= 1
            if s[i+k-1] in vowels:
                curr_count += 1
            if curr_count > max_count:
                max_count = curr_count   
        return max_count