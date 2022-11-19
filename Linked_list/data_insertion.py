# Creating a Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# Creating a LinkedList
class LinkedList:
    def __init__(self):
        self.head = None


# insert at the front of the linkedlist
    def insertAtBegining(self,new_data):
        # creation of new node
        new_node = Node(new_data)
        # insertion at begining
        new_node.next = self.head
        self.head = new_node
# print the linkedlist
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(f"{str(temp.data)} ", end="")
            temp = temp.next


llist = LinkedList()
llist.insertAtBegining(12)
llist.insertAtBegining(10)
llist.insertAtBegining(14)
llist.insertAtBegining(8)
llist.printLinkedList()