class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start_pos = 0
        running_total = 0
        total = 0
        
        for i in range(0, len(gas)):
            running_total += gas[i] - cost[i]
            total += gas[i] - cost[i]
            
            if running_total < 0:
                start_pos = i + 1
                running_total = 0
                        
        return start_pos if total >= 0 else -1
            
        
# [1,2,3,4,5]
# [3,4,5,1,2]

# [-1,-1,-1,4,-1]
# [-1,-2,-3,1,0] -> ends in a positive number, choose the first positive number without a negative number after