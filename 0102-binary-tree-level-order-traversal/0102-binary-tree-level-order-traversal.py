# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        dq = deque([(0, root)])
        
        while dq:
            level, node = dq.popleft()
            if level >= len(ans):
                ans.append([node.val])
            else:
                ans[level].append(node.val)
            
            if node.left:
                dq.append((level + 1, node.left))
            if node.right:
                dq.append((level + 1, node.right))
                
        return ans
        