class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda k: k[0])
        
        width = 0
        x = points[0][0]
        
        for i in range(1, len(points)):
            width = max(width, points[i][0] - x)
            x = points[i][0]
        
        return width
        