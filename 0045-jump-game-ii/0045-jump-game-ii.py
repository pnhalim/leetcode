class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        
        curr_index = len(nums) - 1
        
        while (curr_index > 0):
            earliest_possible_jump = curr_index
            
            for i, n in enumerate(nums):
                if (i + n >= curr_index):
                    earliest_possible_jump = i
                    break
            
            curr_index = earliest_possible_jump
            count += 1
            
        return count
     
# [2,3,1,1,4]
 
# [2,3,-,-,4]
    
    
# [2,3,1,1,4]
# [2,3,2,1,0]

# [2,3,0,1,4]
# [2,3,2,1,0]