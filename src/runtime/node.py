class Node:
    def __init__(self, value = 0):
        self.value = value

    def setValue(self, value):
        self.value = value
        return self

    def print(self):
        print(self.value)
