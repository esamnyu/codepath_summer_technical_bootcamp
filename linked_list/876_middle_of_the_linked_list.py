# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Initialize two pointers, one fast and one slow 
        fast = head 
        slow = head

        #Move the fast pointer 2x the slow pointer 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        #At this point, the slower pointer will now be at the middle node
        return slow