# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases - empty lists? are they the same length? Different length? 
        # Pointer usage; cur is the current listnode 
        # Iterate through both lists and compare 
            dummy = cur = ListNode(0)
            while list1 and list2:
                # Accounts for l1 < l2 
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
                # Doesn't account for l1=l2 or l1>l2
                else:
                    cur.next = list2
                    list2 = list2.next
                    # Move the cur pointer forward 
                    cur = cur.next

                 
            # Append the remaining nodes
            # Append whichever is empty  
            cur.next = list1 or list2
            return dummy.next