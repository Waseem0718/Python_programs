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
    
    def find_length(self):
        cnt = 0
        n = self.head
        while n is not None:
            n = n.nref
            cnt += 1

        print(f"The length of the DLL is {cnt}")
    
        
dll = DoublyLinkedList()
dll.insert_node(10)
dll.insert_node(20)
dll.insert_node(30)
dll.find_length()
