# Creating a Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# Creating a LinkedList
class LinkedList():
    def __init__(self):
        self.head = None


# insert at the front of the linkedlist
    def insertAtEnd(self,new_data):
        # creation of new node
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
        # insertion at end
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
# print the linkedlist
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(f"{str(temp.data)} ", end="")
            temp = temp.next


llist = LinkedList()
llist.insertAtEnd(12)
llist.insertAtEnd(10)
llist.insertAtEnd(14)
llist.insertAtEnd(8)
llist.printLinkedList()