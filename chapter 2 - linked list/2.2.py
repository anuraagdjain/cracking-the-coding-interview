from node import Node
from linkedlist import LinkedList

def return_kth_element(n, pos):
    p1 = n   # slow pointer
    p2 = n  # fast pointer
    print(p1.data,p2.data)
    for i in range(pos):
        # move the slow pointer to pos
        # pos will  be at (LENGTH - pos)
        if(p1 == None):
            return
        p1 = p1.next
    while(p1 != None):
        # loop till p1 is empty
        # p2 is at required position
        p1 = p1.next
        p2 = p2.next

if __name__ == "__main__":
    linked_list = LinkedList()            
    for i in reversed(range(50)):
        linked_list.add(i)
    return_kth_element(linked_list.head, 8)        
