class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]
        
        start = 0
        end = 0
        
        for i in range(len(intervals)):
            if newInterval[0] >= intervals[i][0]:
                start = i
            if newInterval[1] >= intervals[i][0]:
                end = i

        if newInterval[0] <= intervals[start][1]:
            newInterval[0] = min(newInterval[0], intervals[start][0])
            print(1)
        else:
            start += 1
            print(2)
        
        if newInterval[1] >= intervals[end][0]:
            newInterval[1] = max(newInterval[1], intervals[end][1])
            print(3)
        else:
            end -= 1
            print(4)
            
        result = intervals[0:start]
        result.append(newInterval)
        print(end + 1, len(intervals))
        for i in range(end + 1, len(intervals)):
            result.append(intervals[i])
        return result