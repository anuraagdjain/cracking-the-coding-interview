from node import Node


def loop_detection(head):
    fast = head
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if(fast == slow):
            break

    if fast == None or fast.next == None:
        print(" No Loop")
        return
    # head is K node away from loop start
    # fast is LOOP_SIZE - K away from loop start
    slow = head
    while(slow != fast):
        fast = fast.next
        slow = slow.next
    print(slow.data, fast.data)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c

    loop_detection(a)
