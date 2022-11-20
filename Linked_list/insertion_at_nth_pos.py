class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None


    def insert_at_nth_pos(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return 

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(f"{str(temp.data)} ",end="")
            temp = temp.next


llist = LinkedList()
llist.insert_at_nth_pos(10)
llist.insert_at_nth_pos(11)
llist.insert_at_nth_pos(12)
llist.insert_at_nth_pos(13)
llist.printLinkedList()