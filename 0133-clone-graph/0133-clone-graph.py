"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        copied_nodes = {}
        
        def copyNode(node_to_copy: Optional['Node']) -> Optional['Node']:
            
            deep_copy = Node(node_to_copy.val, [])
            copied_nodes[deep_copy.val] = deep_copy
            
            for n in node_to_copy.neighbors:
                if n.val not in copied_nodes:
                    deep_copy.neighbors.append(copyNode(n))
                else:
                    deep_copy.neighbors.append(copied_nodes[n.val])
            
            return deep_copy
            
        
        
        return copyNode(node)