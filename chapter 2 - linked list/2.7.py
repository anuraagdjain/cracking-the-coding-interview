from linkedlist import LinkedList
from node import Node


class IRes:
    def __init__(self, result, node):
        self.result = result
        self.node = node


def print_nodes(n):
    while(n != None):
        print(n.data)
        n = n.next


def tail_and_size(n):
    ctr = 0
    while n.next:
        ctr += 1
        n = n.next
    return ctr, n


def remove_start(n, limit):
    for i in range(limit):
        n = n.next
    return n


def intersection(a, b):
    a_res, b_res = tail_and_size(a), tail_and_size(b)

    # if tail are different, no need to compare further
    if a_res[1] != b_res[1]:
        return IRes(False, None)

    list_diff = abs(a_res[0]-b_res[0])
    # remove start nodes from longer list to ensure both are of same size
    if a_res[0] > b_res[0]:
        a = remove_start(a, list_diff)
    else:
        b = remove_start(b, list_diff)

    while a != None and b != None:
        if a == b:
            return IRes(True, a)
        a = a.next
        b = b.next

    return IRes(False, None)


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(7)
    d = Node(6)
    e = Node(4)
    f = Node(9)
    g = Node(5)
    h = Node(1)
    i = Node(3)

    x = Node(1)
    y = Node(2)
    z = Node(7)

    z.next = y
    y.next = x

    i.next = h
    h.next = g
    g.next = f
    f.next = c  # with intersection
    # f.next = z # without intersection

    e.next = d
    d.next = c
    c.next = b
    b.next = a

    result = intersection(i, e)
    if result.result:
        print("Intersection found at node instance: " + str(result.node))
    else:
        print("No intersection")
