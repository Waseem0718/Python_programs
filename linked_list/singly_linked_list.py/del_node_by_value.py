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

    def delete_node_at_given_value(self,x):
        if self.head is None:
            print("Linked list is empty")
        else:
            if x == self.head.data: #if the given value is equal to 1st node then we delete that node 
                self.head = self.head.ref
            else: #if the given value is in between the nodes then we change previous node ref of the given node 
                n = self.head
                while n.ref is not None:
                    if n.ref.data == x:
                        break
                    n = n.ref

                n.ref = n.ref.ref
            
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
ll1.add_node(10)
ll1.add_node(20)
ll1.add_node(30)
ll1.add_node(40)
ll1.delete_node_at_given_value(30)
ll1.print_ll()