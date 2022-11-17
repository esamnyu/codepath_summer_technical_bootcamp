# Create a separate class including next and val 
# Define a node first as it is not in the current class
# Functions on a linkedlist become a little more intuitive once a node is defined 
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.val = val 
        # None can be considered NULL in this case
        self.head = None 

    def get(self, index: int) -> int:
        

    def addAtHead(self, val: int) -> None:
        

    def addAtTail(self, val: int) -> None:
        

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)