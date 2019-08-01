class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data >= node.data:
            if root.left == None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)


def search_tree(root, data):
    if root is None:
        return "No Data found"
    elif root.data == data:
        return root
    elif root.data < data:
        return search_tree(root.right, data)
    return search_tree(root.left, data)


def inorder_print(root, level=0):
    if root:
        inorder_print(root.left, level+1)
        print("  "*level + str(root.data))
        inorder_print(root.right, level+1)


def balanced_bst(arr):
    if not arr:
        return None
    mid = len(arr)/2
    root = TreeNode(arr[mid])  # mid element as root
    # print("mid", arr[mid])
    # print("high", arr[mid+1:])
    # print("low", arr[:mid])
    # recursive for low and high part of array
    root.left = balanced_bst(arr[:mid])
    root.right = balanced_bst(arr[mid+1:])
    return root


if __name__ == "__main__":
    arr = []
    for i in range(1, 15):
        arr.append(i)
    r = balanced_bst(arr)
    print(inorder_print(r))
