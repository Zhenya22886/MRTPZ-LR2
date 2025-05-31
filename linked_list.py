class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def length(self):
        return self._length

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1

    def get(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Invalid index")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


    def insert(self, element, index):
        if index < 0 or index > self._length:
            raise IndexError("Invalid index")

        new_node = Node(element)

        if index == 0:  # вставка на початок
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self._length == 0:
                self.tail = new_node
        elif index == self._length:  # вставка в кінець (аналог append)
            self.append(element)
            return
        else:  # вставка в середину
            current = self.head
            for _ in range(index):
                current = current.next
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node

        self._length += 1

    def delete(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Invalid index")

        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            if self._length == 1:
                self.tail = None
        elif index == self._length - 1:
            removed_data = self.tail.data
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            removed_data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev

        self._length -= 1
        return removed_data


