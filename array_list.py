class ArrayList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def append(self, element):
        self.data.append(element)

    def insert(self, element, index):
        if index < 0 or index > len(self.data):
            raise IndexError("Invalid index")
        self.data.insert(index, element)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Invalid index")
        return self.data.pop(index)

    def deleteAll(self, element):
        self.data = [x for x in self.data if x != element]

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Invalid index")
        return self.data[index]

    def clone(self):
        new_list = ArrayList()
        new_list.data = self.data.copy()
        return new_list

    def reverse(self):
        self.data.reverse()

    def findFirst(self, element):
        try:
            return self.data.index(element)
        except ValueError:
            return -1

    def findLast(self, element):
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == element:
                return i
        return -1

    def clear(self):
        self.data.clear()

    def extend(self, other):
        self.data += other.data.copy()
