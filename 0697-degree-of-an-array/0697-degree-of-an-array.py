class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        degrees = {} # <num, degree>
        locations = {} # <num, [start, end]>
        
        # fill in degrees and locations
        for i, n in enumerate(nums):
            if n in degrees:
                degrees[n] += 1
                locations[n][1] = i
            else:
                degrees[n] = 1
                locations[n] = [i, i]
        
        # find max degree and return the diff between start and end
        max_degree = 0
        max_nums = nums[0]
        for n, d in degrees.items():
            if d > max_degree:
                max_degree = d
                max_nums = [n]
            elif d == max_degree:
                max_nums.append(n)
        
        # find shortest length
        shortest = 50000
        for n in max_nums:
            shortest = min(shortest, locations[n][1] - locations[n][0] + 1)
        return shortest