from node import Node

def print_nodes(n):
    while(n != None):
        print(n.data)
        n = n.next

def delete_middle_node(n):
    # TODO: last node case 
    if n == None or n.next == None:
        return False
    else:
        n.next = n.next.next
    return True                
 
if __name__ == "__main__":
    n = Node('a')
    n.next =  Node('b')
    n.next.next =  Node('c') 
    n.next.next.next =  Node('d')
    n.next.next.next.next =  Node('e')
    n.next.next.next.next.next =  Node('f') 
    
    delete_middle_node(n.next.next)
    print_nodes(n)

