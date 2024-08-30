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
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def insert_node_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            
            n.nref = new_node
            new_node.pref = n
            new_node.nref =None

        
dll = DoublyLinkedList()
dll.insert_node(10)
dll.insert_node(20)
dll.insert_node(30)
dll.insert_node_at_end(40)
dll.print_fd()

        