class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    def print_fd(self):
        if self.head is None:
            print("DLL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end="<->")
                n = n.nref
            print("None")

    def insert_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def del_node_by_value(self,x):
        if self.head == None:
            print("Linked list is empty")
        else:
            if x == self.head.data:
                self.head = self.head.nref
            else:
                n = self.head
                while n.nref is not None:
                    if n.nref.data == x:
                        break
                    n = n.nref
                
                n.nref = n.nref.nref
                              
            

dll = DoublyLinkedList()
dll.insert_node(10)
dll.insert_node(20)
dll.insert_node(30)
dll.insert_node(40)
dll.insert_node(50)
dll.del_node_by_value(20)
dll.print_fd()

    