class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # sort points by X_start in each point
        points.sort(key=lambda x: x[0])
        
        # go through the points array continuously 
        interval = points[0][1]
        count = 1
        
        for i in range(1, len(points)):
            if points[i][0] > interval:
                # point is outside the interval
                interval = points[i][1]
                count += 1
            else:
                interval = min(interval, points[i][1])

        return count