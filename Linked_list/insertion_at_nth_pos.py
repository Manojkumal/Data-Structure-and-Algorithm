class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    ## Method to count number of elements inside Linked List
    def count_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        return count

    def insert_at_index(self, data, idx):
        if idx < 0 or idx > self.count_length():
            raise Exception("Invalid Index")
    
        if idx == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == idx - 1:
                node = Node(data, iterator.next)
                iterator.next = node
                break
        
            iterator = iterator.next
            count += 1

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