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

    def insert_node_after(self,data,x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.nref = n.nref
            new_node.pref = n
            n.nref = new_node
           
            
      

        
dll = DoublyLinkedList()
dll.insert_node(10)
dll.insert_node(20)
dll.insert_node(30)
dll.insert_node_after(40,30)
dll.print_fd()
