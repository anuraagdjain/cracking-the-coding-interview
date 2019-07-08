class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def add(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        return self.top.data if self.top else None

    def print_stack(self, stack_index):
        print(self.top)


class MinStack:
    def __init__(self):
        self.min = Stack()
        self.stack = Stack()

    def add(self, data):
        self.stack.add(data)
        if self.min.peek() == None or data < self.min.peek():
            self.min.add(data)

    def pop(self):
        item = self.stack.pop()
        if self.min.peek() == item:
            self.min.pop()
        return item

    def get_min(self):
        return self.min.peek()


if __name__ == "__main__":
    s = MinStack()
    s.add(5)
    s.add(-3)
    s.add(1)
    s.add(6)
    s.add(-1)
    print(s.pop())
    print(s.get_min())
    s.add(-10)
    s.pop()
