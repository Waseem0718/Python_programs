#Traversing the linked List
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

    def reverse_ll(self):
        n = self.head
        prev = None
        while n is not None:
            front = n.ref
            n.ref = prev
            prev = n
            n = front

        
        while prev is not None:
            print(prev.data,end="->")
            prev = prev.ref
        print("none")

   
ll1 = LinkedList()
ll1.add_node(10)
ll1.add_node(20)
ll1.add_node(30)
ll1.reverse_ll()
