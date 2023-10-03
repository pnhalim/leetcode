class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for ana in strs:
            key = list(ana)
            key.sort()
            key = ''.join(key)
            if key in anagrams:
                anagrams[key].append(ana)
            else:
                anagrams[key] = [ana]
        return anagrams.values()