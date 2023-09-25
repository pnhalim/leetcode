class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        m1 = {}
        m2 = {}
        for c in word1:
            m1[c] = m1.get(c, 0) + 1
        for c in word2:
            m2[c] = m2.get(c, 0) + 1

        m1_keys = sorted(m1.keys())
        m2_keys = sorted(m2.keys())
        
        for c1, c2 in zip(m1_keys, m2_keys):
            if c1 != c2:
                return False

        return sorted(m1.values()) == sorted(m2.values())