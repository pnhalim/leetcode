# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return root
        
        nodes = [root]
        
        while nodes:
            elem = nodes.pop()
            if elem.right == None and elem.left == None:
                if nodes:
                    elem.right = nodes[-1]
                    continue
                else:
                    break
            if elem.right:
                nodes.append(elem.right)
            if elem.left:
                nodes.append(elem.left)
                elem.right = elem.left
                elem.left = None
        
        return root