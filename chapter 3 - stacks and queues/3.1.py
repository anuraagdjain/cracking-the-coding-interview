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


class FixedStack:
    number_of_stack = 3  # total stack

    def __init__(self, stack_size):
        self.stack_sizes = [0] * self.number_of_stack
        self.stack_size = stack_size  # items per stack
        self.stack = [None] * self.number_of_stack * self.stack_size

    def add(self, stack_index, data):
        # check if stack_index is valid
        if stack_index > self.number_of_stack - 1:
            print("Invalid Stack")
            return

        # check if stack has space
        if not self.is_stack_full(stack_index):
            self.stack_sizes[stack_index] += 1
            self.stack[self.get_stack_pos(stack_index)] = data
        else:
            print("No Space in stack")

    def length(self, stack_index):
        return self.stack_sizes[stack_index]

    def peek(self, stack_index):
        if self.length(stack_index) == 0:
            print("Stack Empty")
            return
        return self.stack[self.get_stack_pos(stack_index)]

    def pop(self, stack_index):
        if self.length(stack_index) == 0:
            print("Stack Empty")
            return
        item = self.stack[self.get_stack_pos(stack_index)]
        self.stack[self.get_stack_pos(stack_index)] = None
        self.stack_sizes[stack_index] -= 1
        return item

    def print_stack(self, stack_index):
        print(self.stack)

    def get_stack_pos(self, stack_index):
        return (stack_index * self.stack_size) + self.stack_sizes[stack_index] - 1

    def is_stack_full(self, stack_index):
        return self.stack_sizes[stack_index] == self.stack_size


if __name__ == "__main__":
    s = FixedStack(3)
    s.add(0, 5)
    s.add(0, 3)
    s.add(0, 1)
    s.add(1, 6)
    s.add(2, 8)
    print(s.peek(0))
    print(s.peek(1))
    print(s.peek(2))
    print(s.pop(0))
    s.print_stack(0)
