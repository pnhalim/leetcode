class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # sort points by X_start in each point
        points.sort(key=lambda x: x[0])
        
        # go through the points array continuously 
        interval = points[0]
        count = 1
        
        for i in range(1, len(points)):
            if points[i][0] > interval[1]:
                # point is outside the interval
                interval = points[i]
                count += 1
            else:
                interval[0] = max(interval[0], points[i][0])
                interval[1] = min(interval[1], points[i][1])

        return count