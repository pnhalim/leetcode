class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]
        
        # insert the thing
        inserted_at = 0
        for i in range(len(intervals)-1):
            if newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i+1][0]:
                # insert into this spot
                intervals.insert(i+1, newInterval)
                inserted_at = i+1
                break
        if inserted_at == 0:
            if newInterval[0] < intervals[0][0]:
                intervals.insert(0, newInterval)
                inserted_at = 1
            else:
                intervals.append(newInterval)
                inserted_at = len(intervals) - 1
                
        # print(intervals)
        
        # continue merging until cannot merge
        while (inserted_at < len(intervals) and intervals[inserted_at][0] <= intervals[inserted_at - 1][1]):
            # merge 
            intervals[inserted_at - 1][1] = max(intervals[inserted_at][1], intervals[inserted_at - 1][1])
            intervals[inserted_at - 1][0] = min(intervals[inserted_at][0], intervals[inserted_at - 1][0])
            intervals.pop(inserted_at)
            
        inserted_at += 1
        
        while (inserted_at < len(intervals) and intervals[inserted_at][0] <= intervals[inserted_at - 1][1]):
            # merge 
            intervals[inserted_at - 1][1] = max(intervals[inserted_at][1], intervals[inserted_at - 1][1])
            intervals[inserted_at - 1][0] = min(intervals[inserted_at][0], intervals[inserted_at - 1][0])
            intervals.pop(inserted_at)
            
        
        return intervals
        
        
        """
        
        Cases
        
        1 - insert and it doesn't matter
        [[1,3],[6,9]] -> [>3, <6]
        [[1,3],[4,5],[6,9]]
        
        2a - insert and it overlaps with one edge
        [[1,3],[6,9]] -> [<=3,<6]
        [[1,5],[6,9]]
        
        2b - insert and it overlaps with one edge
        [[1,3],[6,9]] -> [>3,>=6]
        [[1,3],[4,9]]
        
        3 - insert and it overlaps both edges 
        [[1,3],[6,9]] -> [<=3,>=6]
        [[1,9]]
        
        
        """