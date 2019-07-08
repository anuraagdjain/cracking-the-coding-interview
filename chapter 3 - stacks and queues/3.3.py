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

    def remove_bottom(self):
        top = self.top
        prev = None
        while top.next:
            prev = top
            top = top.next
        prev.next = None
        return top.data

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

    def pop_at(self, stack_index):
        if stack_index > self.current_stack_index:
            return "Invalid Stack. Starting from 0"
        # pop specific stack's top value
        return self.left_shift(stack_index, True)

    def left_shift(self, stack_index, remove_top):
        stack = self.stacks[stack_index]
        item = None
        if remove_top:
            item = stack.pop()
        else:
            item = stack.remove_bottom()

        if stack.length == 0:
            del self.stacks[stack_index]
        elif len(self.stacks) > stack_index + 1:
            n = self.left_shift(stack_index+1, False)
            stack.add(n)
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

    # print("Pop: ", p.pop())

    p.add(5)
    p.add(15)

    print("AT:", p.pop_at(1))

    p.print_stacks()
