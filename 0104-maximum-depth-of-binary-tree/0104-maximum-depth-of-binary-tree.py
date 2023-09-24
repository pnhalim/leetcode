# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if (not root):
            return 0
        
        stack = []
        root.val = 1
        max_depth = 1
        stack.append(root)
        while (len(stack) > 0):
            # dfs
            node = stack.pop()
            
            if (node.val > max_depth):
                max_depth = node.val
            
            if (node.left):
                node.left.val = node.val + 1
                stack.append(node.left)
            if (node.right):
                node.right.val = node.val + 1
                stack.append(node.right)
                
        return max_depth
                
        