class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split()[::-1]
        return ' '.join(ans)