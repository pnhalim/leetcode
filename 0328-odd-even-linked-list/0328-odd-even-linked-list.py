# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = None
        odd_head = None
        even = None
        even_head = None
        i = 1
        
        while (head):
            if i % 2 == 0:
                # even
                if even:
                    even.next = head
                else:
                    even_head = head
                even = head
            else:
                # odd
                if odd:
                    odd.next = head
                else: 
                    odd_head = head
                odd = head
            head = head.next
            i += 1
        
        # merge
        if not odd:
            return even_head
        odd.next = even_head
        if even:
            even.next = None
        return odd_head