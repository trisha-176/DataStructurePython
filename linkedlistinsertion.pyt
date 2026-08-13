class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

   
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    
    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 0

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    
    def display(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) if elements else "List is empty")
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return

        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40) 
    ll.display()          

    ll.insert_at_beginning(5)
    ll.display()          

    ll.insert_at_position(15, 2)
    ll.display()          

    ll.insert_at_position(100, 10)  

    ll.delete_at_beginning()
    ll.display()
    ll.delete_at_end()
    ll.display()
    ll.delete_at_position(1)
    ll.display()

