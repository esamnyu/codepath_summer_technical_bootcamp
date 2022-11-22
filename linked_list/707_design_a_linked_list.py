# Create a separate class including next and val 
# Define a node first as it is not in the current class
# Functions on a linkedlist become a little more intuitive once a node is defined 
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self, val):
        self.head = None
        # None can be considered NULL in this case
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or self.size < 0 or index>=self.size:
            return None
        if self.head == None:
            return None 
       # Initialize a new pointer 
        curr = self.head
        #Go up until the chosen index and return the value
        for i in range(index)
            curr = curr.next
        return self.val

    
    def addAtHead(self, val: int) -> None:
        curr = Node(val) 
        curr.next = self.head 
        self.head = curr
        
        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
        # Remember to delete at head, in the middle, and at the end 
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)