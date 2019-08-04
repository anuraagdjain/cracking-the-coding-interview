class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def length(self):
        ctr = 0
        node = self.head
        while node:
            ctr += 1
            node = node.next
        return ctr


def inorder_print(root, arr, level=0):
    if root:
        if not level < len(arr):
            arr.append(LinkedList())
        arr[level].add(root.data)
        inorder_print(root.left, arr, level+1)
        # print("  "*level + str(root.data))
        inorder_print(root.right, arr, level+1)


if __name__ == "__main__":
    arr_linked_list = []
    arr = []
    z = TreeNode(0)
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    c.left = b
    c.right = d
    b.left = z
    b.right = a
    d.left = e
    d.right = f
    inorder_print(c, arr_linked_list)
    for index, ll in enumerate(arr_linked_list):
        print("level ", index)
        ll.list_nodes()
