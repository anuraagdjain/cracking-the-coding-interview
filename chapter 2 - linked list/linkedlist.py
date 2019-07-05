from node import Node
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        n = Node(data)
        if(self.head is not None):
            n.next = self.head
        self.head = n

    def list_nodes(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
