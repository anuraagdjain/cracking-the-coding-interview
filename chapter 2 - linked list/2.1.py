from node import Node
from linkedlist import LinkedList

def hash_set_remove_dups(n): 
    hash_val = set()
    prev_node = None
    while(n != None):
        if n.data in hash_val:
            prev_node.next = n.next
        else:
            hash_val.add(n.data)
            prev_node = n
        n = n.next      
    return n        
            
if __name__ == "__main__":
    linked_list = LinkedList()            
    linked_list.add(0)
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(1)
    linked_list.add(4)
    linked_list.add(2)
    print('List')
    linked_list.list_nodes()
    hash_set_remove_dups(linked_list.head)
    print('After removing dups')
    linked_list.list_nodes()