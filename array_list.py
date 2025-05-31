class ArrayList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def append(self, element):
        self.data.append(element)