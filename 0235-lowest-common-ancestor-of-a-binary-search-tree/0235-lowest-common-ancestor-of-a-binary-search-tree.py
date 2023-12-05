# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def bin_search(root: 'TreeNode', target: 'TreeNode') -> list:
            ans = []
            curr = root
            
            while curr.val != target.val:
                ans.append(curr)
                if (curr.val < target.val):
                    curr = curr.right
                else:
                    curr = curr.left
            
            ans.append(curr)
            return ans
        
        p_dfs = bin_search(root, p)
        q_dfs = bin_search(root, q)
        q_dfs = set([n.val for n in q_dfs])
        
        # look in the dfs list for the lowest common ancestor
        for n in p_dfs[::-1]:
            if n.val in q_dfs:
                return n
            
        # should not happen
        return None