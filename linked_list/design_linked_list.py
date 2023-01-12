# Create a separate class including next and val 
# Define a node first as it is not in the current class
# Functions on a linkedlist become a little more intuitive once a node is defined 
class Node(object):
    def __init__(self, val):
        self.val = val
        # next should be set to none as that is default          
        self.next = None 

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        # None can be considered NULL in this case
        self.size = 0

    def get(self, index: int) -> int:
        # Check for invalid index values
        if index < 0 or index >= self.size:
            return -1
        # Check if the list is empty
        if self.head == None:
            return -1
        # Initialize a new pointer at the head of the list
        curr = self.head
        # Traverse the list to find the node at the specified index
        for i in range(index):
            curr = curr.next
        # Return the value of the node at the specified index
        return curr.val

    
    def addAtHead(self, val: int) -> None:
        # Create a new node called curr 
        curr = Node(val) 
        # The head pointer is still referencing an existing node          
        curr.next = self.head 
        # head pointer now references curr, the first node in the linkedlist         
        self.head = curr
        self.size +=1
        
    def addAtTail(self, val: int) -> None:
        curr = Node(val)
        if self.head == None:
        # Linked list is empty, head is the same as tail
        # Head pointer points to the newly created node 
            self.head = curr
        # Else traverse the linkedlist to find the tail
        else:
            temp = self.head
            # Check for temp.next- we care about the next element 
            while temp.next != None:
                temp = temp.next
            temp.next = curr 
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
            # Check for invalid index values
            if index < 0 or index > self.size:
                return
            # Create a new node
            curr = Node(val)
            # If adding at the head
            if index == 0:
                curr.next = self.head
                self.head = curr
            else:
                # Traverse the list to find the node before the specified index
                temp = self.head
                for i in range(index-1):
                    temp = temp.next
                # Update the next pointers
                # 
                # Here is the step 3:
                #1. We set the next pointer of the new node to the node that is currently at the specified index
                curr.next = temp.next
                #2. We set the next pointer of the node before the specified index to the new node
                temp.next = curr
            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        # Check for invalid index values
        if index < 0 or index >= self.size:
            return
        # If deleting the head
        if index == 0:
            # Head pointer points to the next node 
            self.head = self.head.next
        else:
            # Traverse the list to find the node before the specified index
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            # Update the next pointers
            temp.next = temp.next.next
        self.size -= 1
 
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)