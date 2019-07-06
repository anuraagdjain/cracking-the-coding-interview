from linkedlist import LinkedList
from node import Node


def print_nodes(n):
    while(n != None):
        print(n.data)
        n = n.next


def sum_list(a, b, carry):
    if a == None and b == None and carry == 0:
        return None
    val = carry

    if a != None:
        val += a.data
    if b != None:
        val += b.data
    result = Node(val % 10)

    if a != None or b != None:
        more = sum_list(
            None if a == None else a.next,
            None if b == None else b.next,
            1 if val >= 10 else 0,
        )
        result.next = more

    return result


def front_padding(head, nos):
    # nos = how many 0's to add in front
    for i in range(nos):
        if head != None:
            n = Node(0)
            n.next = head
            head = n
    return head


def list_length(a):
    ctr = 0
    while a != None:
        ctr += 1
        a = a.next
    return ctr


class PartialSum:
    def __init__(self):
        self.sum = None
        self.carry = 0


def forward_sum(a, b):
    if a == None and b == None:
        ps = PartialSum()
        return ps
    sum = 0
    result = forward_sum(a.next, b.next)
    sum = result.carry + a.data + b.data
    # to ensure there is connection between the results from last to first.
    # first 7+5 = 12; carry = 1 and value 2 is returned.
    # as we progress to first number carry and prev number must be linked.
    f = Node(sum % 10)
    f.next = result.sum
    ps = PartialSum()
    ps.sum = f
    ps.carry = sum/10
    return ps


def forward_list(a, b):
    a_len, b_len = list_length(a), list_length(b)
    if a_len != b_len:
        if b_len > a_len:
            # adding 0's in a list
            a = front_padding(a, b_len - a_len)
        else:
            # adding 0's in b list
            b = front_padding(b, a_len - b_len)
    forward_sum(a, b)
    print_nodes(forward_sum(a, b).sum)


if __name__ == "__main__":
    a = LinkedList()
    a.add(6)
    a.add(1)
    a.add(7)

    b = LinkedList()
    b.add(2)
    b.add(9)
    b.add(5)

    print("result")
    result = sum_list(a.head, b.head, 0)
    print_nodes(result)

    print()
    print("forward_order_sum")
    c = LinkedList()
    c.add(7)
    c.add(1)
    c.add(6)

    d = LinkedList()
    d.add(5)
    d.add(9)
    d.add(2)

    """
       6->1->7
     + 2->9->5
     -----------
       9  1  2
     -----------       
    """
    c.list_nodes()
    print()
    d.list_nodes()
    print("Result")
    forward_list(c.head, d.head)
