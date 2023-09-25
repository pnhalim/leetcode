class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for elem in arr:
            dic[elem] = dic.get(elem, 0) + 1
        lis = dic.values()
        return len(lis) == len(set(lis))