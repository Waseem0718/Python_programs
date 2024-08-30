class Node:
    #creating a node
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinkedList:
    #linking the nodes
    def __init__(self):
        self.head = None

    #adding a node to the linked list
    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    #adding a new_node at the beginning of the linked list
    def add_at_beginning(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    #printing the nodes
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
ll1.add_at_beginning(50)
ll1.add_at_beginning(100)



ll1.print_ll()