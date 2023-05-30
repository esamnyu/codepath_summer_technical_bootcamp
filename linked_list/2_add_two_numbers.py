# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new linked list to store the result
        result = ListNode()
        current = result  # Keep track of the current node in the result list
        
        # Initialize variables to keep track of the current nodes in each list
        # and a carry variable to store any carry-over from addition
        current1 = l1
        current2 = l2
        carry = 0

        # Iterate until both lists are exhausted
        while current1 is not None or current2 is not None:
            # Initialize variables to store the values of the current nodes
            # (if they exist) and the sum of the values
            value1 = 0
            value2 = 0
            sum = 0

            # If the current node in l1 exists, store its value
            if current1 is not None:
                value1 = current1.val
                # move on to the next node in l1
                current1 = current1.next
            # If the current node in l2 exists, store its value
            if current2 is not None:
                value2 = current2.val
                # move on to the next node in l2
                current2 = current2.next
        
            # Add the values and the carry, and store the result in sum
            sum = value1 + value2 + carry

            # If the sum is greater than 9, set carry to 1 and store the
            # ones digit of the sum as the value for the new node
            if sum > 9:
                carry = 1
                sum %= 10
            # If the sum is less than or equal to 9, set carry to 0 and
            # store the sum as the value for the new node
            else:
                carry = 0

            # Create a new node with the value of sum and append it to the result list
            current.next = ListNode(sum)
            current = current.next  # Move on to the next node in the result list

        # If there is a carry remaining after both lists are exhausted,
        # create a new node with the value of carry and append it to the result list
        if carry > 0:
            current.next = ListNode(carry)
        # This version does not require a head, next suffices for the head 
        # Return the head of the result list
        return result.next
