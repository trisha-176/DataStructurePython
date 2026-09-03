class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self._head = None

    def append(self, item):
        new_node = Node(item)

        if not self._head:
            self._head = new_node
            new_node.next = new_node
            return

        current = self._head

        while current.next != self._head:
            current = current.next

        current.next = new_node
        new_node.next = self._head

    def delete(self, key):
        if not self._head:
            return

        current = self._head
        prev = None

        while True:
            if current.data == key:

                
                if prev is None:
                    if current.next == self._head:
                        self._head = None
                    else:
                        last = self._head
                        while last.next != self._head:
                            last = last.next

                        self._head = current.next
                        last.next = self._head

                
                else:
                    prev.next = current.next

                return

            prev = current
            current = current.next

            if current == self._head:
                break

    def iterate(self):
        if not self._head:
            return

        current = self._head

        while True:
            yield current.data
            current = current.next

            if current == self._head:
                break



list = CircularSinglyLinkedList()

list.append(10)
list.append(20)
list.append(30)
list.append(40)

print("After insertion:")
for item in list.iterate():
    print(item, end=" ")

list.delete(20)

print("\nAfter deletion:")
for item in list.iterate():
    print(item, end=" ")