class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if self.items else None

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1] if self.items else None

    def __repr__(self):
        return repr(self.items)
