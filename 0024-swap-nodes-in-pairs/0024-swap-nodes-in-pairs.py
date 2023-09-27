# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        node = head
        
        while (node and node.next):
            left = node
            right = node.next
            
            # swap
            temp_next = right.next
            right.next = left
            left.next = temp_next
            
            # make sure the prev node points to right (new left)
            if prev:
                prev.next = right
            else:
                head = right
            prev = left
            node = prev.next
            
        return head