class Node:
    #creating a node
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None
        
class DoublyLinkedList:
    #linking the nodes
    def __init__(self):
        self.head = None
    #traverse in forward direction
    def print_ll_fd(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                 print(n.data,end="<->")
                 n = n.nref
            print("None") 
    #traverse in backward direction
    def print_ll_bd(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n.nref is not None:
                 n = n.nref
            while n is not None:
                 print(n.data,end="<->")
                 n = n.pref
            print("None") 
    
        
dll = DoublyLinkedList()
dll.print_ll_fd()
