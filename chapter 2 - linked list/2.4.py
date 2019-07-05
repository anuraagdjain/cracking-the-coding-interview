from linkedlist import LinkedList
from node import Node
def print_nodes(n):
    while(n != None):
        print(n.data)
        n = n.next


def two_buffer_partition(n, partition):
    high_node = None
    low_node = None
    while(n != None):
        new_node = Node(n.data)
        if(n.data < partition):
            if low_node == None:
                low_node = new_node
            else:
                new_node.next = low_node
                low_node = new_node
        else:
            if high_node == None:
                high_node = new_node
            else:
                new_node.next = high_node
                high_node = new_node
        n = n.next
    
    # merging nodes
    final_node = low_node

    # travel to last node
    while(low_node.next != None):
        low_node = low_node.next
    # connect last node of low val to high val node        
    low_node.next = high_node

    # print the final nodes
    print_nodes(final_node)

def partition(n, partition):
    head = n
    tail = n
    while(n != None):
        next = n.next
        print_nodes(next)
        if n.data < partition:
            n.next = head
            head = n
        else:
            tail.next = n
            tail = n
        n=next
    tail.next = None        
    return head

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(10)
    linked_list.add(5)
    linked_list.add(8)
    linked_list.add(5)
    linked_list.add(3)
    linked_list.list_nodes()
    print('-------')
    linked_list.head = partition(linked_list.head, 5)
    print('-------')
    two_buffer_partition(linked_list.head, 5)
    print('-------')
    linked_list.list_nodes()
    print('-------')
