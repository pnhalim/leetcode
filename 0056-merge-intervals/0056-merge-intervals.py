class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # treat as a stack
        intervals = sorted(intervals, key=lambda l: l[0], reverse=True)
        ans = []
        
        while (len(intervals) > 1):
            l = intervals.pop()
            r = intervals.pop()
            
            if (l[0] <= r[0] and r[0] <= l[1]):
                intervals.append([l[0], max(l[1], r[1])])
            else:
                ans.append(l)
                intervals.append(r)
                
        ans.append(intervals[-1])
        return ans
        
        