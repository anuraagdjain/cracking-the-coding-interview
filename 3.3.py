class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def add(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return "Empty Stack"
        item = self.top.data
        self.top = self.top.next
        self.length -= 1
        return item

    def peek(self):
        return self.top.data if self.top else None

    def print_stack(self):
        top = self.top
        while top:
            print(top.data)
            top = top.next


class PlateStack:
    stack_threshold = 3  # items per stack

    def __init__(self):
        self.stacks = []
        self.current_stack_index = -1  # since no stack is assinged initally

    def add(self, data):
        if len(self.stacks) == 0 or self.is_stack_full():
            self.current_stack_index += 1
            self.stacks.append(Stack())
        self.stacks[self.current_stack_index].add(data)

    def pop(self):
        if len(self.stacks) == 0:
            return "No Stack Present"
        last_stack = self.get_last_stack()
        item = last_stack.pop()
        if last_stack.length == 0:
            self.stacks.pop()
            self.current_stack_index -= 1
        return item

    def is_stack_full(self):
        # check if last stack is full
        return self.get_last_stack().length == self.stack_threshold

    def get_last_stack(self):
        return self.stacks[self.current_stack_index]

    def print_stacks(self):
        for i, s in enumerate(self.stacks, start=0):
            print("STACK: ", i)
            s.print_stack()


if __name__ == "__main__":
    p = PlateStack()
    p.add(1)
    p.add(3)
    p.add(3)

    p.add(4)

    p.print_stacks()

    print("Pop: ", p.pop())

    p.add(5)
    p.add(15)

    p.print_stacks()
