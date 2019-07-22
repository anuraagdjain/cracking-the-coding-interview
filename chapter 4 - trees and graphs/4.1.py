class QNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__length = 0

    def enqueue(self, data):
        n = QNode(data)
        self.__length += 1
        if self.__rear:
            self.__rear.next = n
        self.__rear = n
        if self.__front == None:
            self.__front = self.__rear

    def dequeue(self):
        if self.__front == None:
            return "No data"
        item = self.__front
        self.__front = self.__front.next if self.__front.next else None
        if item == self.__rear:
            self.__rear = None
            self.__front = None
        self.__length -= 1
        return item.data

    def is_empty(self):
        return self.__length == 0

    def print_queue(self):
        f = self.__front
        while(f):
            print(f.data)
            f = f.next


class GraphNode:
    def __init__(self, data, adjacents=[]):
        self.data = data
        self.adjacents = adjacents


def print_tree(tree, level=0):
    if tree == None:
        return '\\'
    # if tree.visited:
    #     return
    tree.visited = True
    print_tree(tree.left, level + 1)
    print('  ' * level + str(tree.data))
    print_tree(tree.right, level + 1)


def bfs_path(source, dest):
    queue = Queue()
    parent_nodes = {}
    queue.enqueue(source)
    path_found = False
    while not queue.is_empty():
        item = queue.dequeue()
        if item == dest:
            path_found = True
            break

        for n in item.adjacents:
            if not parent_nodes.get(item.data):
                parent_nodes[item.data] = []
            parent_nodes[item.data].append(n.data)
            queue.enqueue(n)

    # path printing
    if path_found:
        path_queue = []
        path = []
        path_queue += parent_nodes[source.data]
        while not len(path_queue) == 0:
            item = path_queue[0]
            path_queue = path_queue[1:]
            if parent_nodes.get(item):
                path.append(item)
                if (dest.data) in parent_nodes[item]:
                    break
                # push all the child nodes
                path_queue.append(parent_nodes[item])
        path.insert(0, source.data)
        path.insert(len(path)+1, dest.data)
        print(path)

        """
        # path prining using queue
        path_queue = []
        map(lambda i: path_queue.enqueue(i), parent_nodes[source.data])
        while not path_queue.is_empty():
            item = path_queue.dequeue()
            if parent_nodes.get(item):
                path.append(item)
                if (dest.data) in parent_nodes[item]:
                    break
                # push all the child nodes to queue
                map(lambda i: path_queue.enqueue(i), parent_nodes[item])
        path.insert(0, source.data)
        path.insert(len(path)+1, dest.data)
        print(path)
        """

    print("path found" if path_found else "no path")


if __name__ == "__main__":
    a = GraphNode(1)
    b = GraphNode(2)
    c = GraphNode(3)
    d = GraphNode(4)
    e = GraphNode(5)
    f = GraphNode(6)
    a.adjacents = [b]
    b.adjacents = [e, c]
    c.adjacents = [d, f]
    f.adjacents = [e]
    bfs_path(c, f)
