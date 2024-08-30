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

    def segregate_odd_even(self):
        #Print even nodes
        temp = self.head
        while temp is not None:
            if temp.data % 2 == 0:
                print(temp.data,end="->")
            temp = temp.ref
        #print odd nodes
        temp = self.head
        while temp is not None:
            if temp.data % 2 != 0:
                print(temp.data,end="->")
            temp = temp.ref
        print("None")

ll1 = LinkedList()
ll1.add_node(1)
ll1.add_node(2)
ll1.add_node(3)
ll1.add_node(4)
ll1.add_node(5)
ll1.add_node(6)

ll1.segregate_odd_even()