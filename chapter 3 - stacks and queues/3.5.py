class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__length = 0

    def add(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.__length += 1

    def pop(self):
        if self.__length == 0:
            return "Empty Stack"
        item = self.top.data
        self.top = self.top.next
        self.__length -= 1
        return item

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.__length == 0

    def print_stack(self):
        top = self.top
        while top:
            print(top.data)
            top = top.next


def sort_stack(stack):
    s2 = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not s2.is_empty() and s2.peek() > temp:
            # push element larger than temp to stack
            stack.add(s2.pop())
        s2.add(temp)  # add stack's data to s2
    while not s2.is_empty():
        # move back s2's data to stack
        stack.add(s2.pop())
    stack.print_stack()


if __name__ == "__main__":
    s = Stack()
    s.add(1)
    s.add(7)
    s.add(-10)
    s.add(51)
    s.add(1)
    s.add(10)
    s.add(-3)
    s.add(5)
    sort_stack(s)
