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
    
    def searching_node(self,target):
        n = self.head
        while n.nref is not None:
            if n.data == target:
                break
            n = n.nref
        
        if n.data == target:
            print("found")
        else:
            print("Not found")

    
        
dll = DoublyLinkedList()
dll.insert_node(10)
dll.insert_node(20)
dll.insert_node(30)
dll.searching_node(10)