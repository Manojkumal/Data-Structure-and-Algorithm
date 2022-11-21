class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_AtEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def reverseList(self):
        prev = None
        next_ptr = None
        curr = self.head
        while curr:
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr
        # for linking the head node with last node
        self.head = prev

        

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(f"{str(temp.data)}",end=" ")
            temp = temp.next

llist = LinkedList()
llist.insert_AtEnd(6)
llist.insert_AtEnd(7)
llist.insert_AtEnd(8)
llist.insert_AtEnd(9)
llist.insert_AtEnd(10)
llist.insert_AtEnd(11)
print("Original Linked List")
llist.printLinkedList()
llist.reverseList()
print("\n")
print("Reverse Linked List")
llist.printLinkedList()