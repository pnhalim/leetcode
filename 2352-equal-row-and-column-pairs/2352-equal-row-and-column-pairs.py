class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        # hash map of rows with count
        m = {}
        for row in grid:
            row = ','.join([str(c) for c in row])
            if row not in m.keys():
                m[row] = 1
            else:
                m[row] += 1
                
        # check columns
        count = 0
        for c in range(len(grid)):
            col = ','.join([str(grid[r][c]) for r in range(len(grid))])
            if col in m.keys():
                count += m[col]
        
        return count