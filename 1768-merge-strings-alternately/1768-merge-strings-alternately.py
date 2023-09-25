class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        ans = []
        while (p < len(word1) and p < len(word2)):
            ans.append(word1[p])
            ans.append(word2[p])
            p += 1
        while (p < len(word1)):
            ans.append(word1[p])
            p += 1
        while (p < len(word2)):
            ans.append(word2[p])
            p += 1
        
        return ''.join(ans)