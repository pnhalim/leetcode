class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        degrees = {}     # <num, degree>
        locations = {}  # <num, [start, end]>
        
        # fill degree and locations dicts
        for i, n in enumerate(nums):
            if n in degrees:
                degrees[n] += 1
                locations[n][1] = i
            else:
                degrees[n] = 1
                locations[n] = [i, i]
        
        # find greatest degree
        greatest_degree = 0
        greatest_nums = []
        for n, d in degrees.items():
            if d > greatest_degree:
                greatest_degree = d
                greatest_nums = [n]
            elif d == greatest_degree:
                greatest_nums.append(n)
        
        # find shortest end - start from locations
        shortest = float('inf')
        for n in greatest_nums:
            shortest = min(shortest, locations[n][1] - locations[n][0] + 1)
        
        return shortest