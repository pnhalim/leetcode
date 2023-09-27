# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, True, 0), (root, False, 0)]
        max_val = 0
        
        while (len(stack) > 0):
            node, is_right, val = stack.pop()
            
            if node.left:
                if is_right:
                    stack.append((node.left, False, val + 1))
                else:
                    stack.append((node.left, True, 0))
            else:
                if val > max_val:
                    max_val = val
            
            if node.right:
                if not is_right:
                    stack.append((node.right, True, val + 1))
                else:
                    stack.append((node.right, False, 0))
            else:
                if val > max_val:
                    max_val = val
                    
        return max_val