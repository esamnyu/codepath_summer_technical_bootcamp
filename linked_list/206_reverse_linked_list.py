# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head # Head of the linkedlist 
        # Don't need this 
        # while curr.next != None:
        # Use this instead
        while curr:
            # Keep track of the next node 
            nxt = curr.next
            # reverse the pointer
            curr.next = prev
            # Previous points to curr aka the past element 
            prev = curr
            # set curr to the tracked next element 
            curr = nxt 
        return prev # curr will eventually reach Null, and prev will be at the head 