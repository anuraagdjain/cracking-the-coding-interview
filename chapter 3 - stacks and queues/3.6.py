class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.__length__ = 0

    def add(self, data):
        n = Node(data)
        self.__length__ += 1
        if(self.head is not None):
            n.next = self.head
        self.head = n

    def add_last(self, data):
        n = Node(data)
        self.__length__ += 1
        if self.head:
            self.head.next = n
        else:
            self.head = n

    def remove_head(self):
        item = self.head
        self.head = self.head.next
        self.__length__ -= 1
        return item

    def peek(self):
        return self.head.data if self.head else None

    def list_nodes(self):
        node = self.head
        while node:
            print(node.data.category, node.data.name, node.data.pos)
            node = node.next

    def length(self):
        return self.__length__


class Animal:
    def __init__(self, category, name):
        self.category = category
        self.name = name
        self.pos = 0


class AnimalQueue:
    def __init__(self):
        self.pos = 0  # timestamp or unique value to keep track b/w lists
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def enqueue(self, data):
        self.pos += 1
        data.pos = self.pos
        if data.category == 'dog':
            self.dogs.add_last(data)
        elif data.category == 'cat':
            self.cats.add_last(data)
        else:
            self.pos -= 1
            print("Wrong animal category")

    def dequeue_any(self):
        dog, cat = self.dogs.peek(), self.cats.peek()
        item = self.dogs.remove_head() if dog.pos < cat.pos else self.cats.remove_head()
        print("Removed: ", item.data.category, item.data.name)

    def dequeue_cat(self):
        item = self.cats.remove_head() if self.cats.length() > 0 else 'No data'
        if isinstance(item, str):
            print(item)
        else:
            print("Removed: ", item.data.category, item.data.name)

    def dequeue_dog(self):
        item = self.dogs.remove_head() if self.dogs.length() > 0 else 'No data'
        if isinstance(item, str):
            print(item)
        else:
            print("Removed: ", item.data.category, item.data.name)

    def print_list(self):
        self.cats.list_nodes()
        self.dogs.list_nodes()


if __name__ == "__main__":
    a = AnimalQueue()
    a.enqueue(Animal('cat', 'a'))
    a.enqueue(Animal('dog', 'b'))
    a.enqueue(Animal('cat', 'c'))
    a.dequeue_any()
    a.dequeue_dog()
    a.dequeue_dog()  # no data
    a.dequeue_cat()
    a.enqueue(Animal('dog', '12'))
    a.print_list()
