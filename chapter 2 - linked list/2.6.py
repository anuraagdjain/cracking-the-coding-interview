from node import Node
from linkedlist import LinkedList


class PRes:
    def __init__(self, node, result):
        self.result = result
        self.node = node


def print_nodes(n):
    while(n != None):
        print(n.data)
        n = n.next


def palindrome(l, list_length):
    is_odd = list_length % 2 != 0
    rev_list = LinkedList()
    for i in range(list_length/2):
        rev_list.add(l.data)
        l = l.next

    # is list is odd no. Skip middle element
    if is_odd:
        l = l.next

    rev = rev_list.head
    # compare if rest of list (l) and copied data(rev) are same
    while(l != None and rev != None):
        if(l.data != rev.data):
            return False
        l = l.next
        rev = rev.next
    return l == None and rev == None


def recursive_palindrome(head, list_length):
    if head == None or list_length <= 0:
        print(head.data, list_length)
        # even
        return PRes(head, True)
    elif list_length == 1:
        # odd
        return PRes(head.next, True)

    res = recursive_palindrome(head.next, list_length - 2)
    if not res.result or res.node == None:
        # not palindrone return Failure
        return res
    res.result = head.data == res.node.data  # check if data is same
    res.node = res.node.next
    return res


if __name__ == "__main__":
    l = LinkedList()
    l.add(0)
    l.add(1)
    l.add(2)
    l.add(1)
    l.add(0)
    print(palindrome(l.head, l.length()))
    print(recursive_palindrome(l.head, l.length()).result)
