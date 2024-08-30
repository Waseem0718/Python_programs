class Node:
    #creating a node
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinkedList:
    #linking the nodes
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def delete_node_at_beginning(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.ref
            

    def print_ll(self):
        if self.head is None:
            print("LL is Empty")
        else:
            n = self.head
            while n is not None:
                 print(n.data,end="->")
                 n = n.ref
            print("None") 
        
ll1 = LinkedList()
ll1.add_node(20)
ll1.add_node(30)
ll1.add_node(40)
ll1.delete_node_at_beginning()
ll1.print_ll()