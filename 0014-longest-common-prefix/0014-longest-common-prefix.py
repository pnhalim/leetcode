class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find min len string in list
        minlen = min([len(s) for s in strs])
        
        i = 0
        prefix = ""
        # iterate up to s
        while (i < minlen):
            val = strs[0][i]
            for s in strs:
                if (s[i] != val):
                    val = ""
            if val == "":
                return prefix
            else:
                prefix += val
            i += 1
            
        return prefix