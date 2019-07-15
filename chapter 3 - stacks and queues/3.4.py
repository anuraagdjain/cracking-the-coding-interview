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


class MyQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def add(self, data):
        self.rear.add(data)

    def remove(self):
        # shift data from  rear to front
        if self.front.is_empty():
            while not self.rear.is_empty():
                self.front.add(self.rear.pop())
        item = self.front.pop()
        return item

    def print_queue(self):
        print("Front")
        self.front.print_stack()
        print("Rear")
        self.rear.print_stack()


if __name__ == "__main__":
    q = MyQueue()
    for i in range(0, 6):
        q.add(i)
    print("REMOVE 0", q.remove())
    print("REMOVE 1", q.remove())
    q.print_queue()
    print("REMOVE 2", q.remove())
    q.add(190)
    q.print_queue()
    print("REMOVE 3", q.remove())
    print("REMOVE 4", q.remove())
    print("REMOVE 5", q.remove())
    q.print_queue()  # 190 is present in rear
