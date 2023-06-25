class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Recursive solution
class Solution:
    def reverseList(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return newHead

# Function to build a linked list from a list of values
def build_linked_list(lst):
    prev_node = None
    for val in reversed(lst):
        node = ListNode(val)
        node.next = prev_node
        prev_node = node
    return prev_node

# Function to print the linked list
def print_linked_list(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()

# Test cases
solution = Solution()
test_cases = [[1, 2, 3, 4, 5], [1, 2, 3], []]

for test_case in test_cases:
    print("Original List:")
    head = build_linked_list(test_case)
    print_linked_list(head)
    print("Reversed List:")
    reversed_head = solution.reverseList(head)
    print_linked_list(reversed_head)
