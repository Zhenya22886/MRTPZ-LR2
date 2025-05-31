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

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Invalid index")
        return self.data[index]