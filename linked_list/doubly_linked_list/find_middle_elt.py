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
    
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.nref:
            slow = slow.nref
            fast =  fast.nref.nref

        print(slow.data)

    
        
dll = DoublyLinkedList()
dll.insert_node(10)
dll.insert_node(20)
dll.insert_node(30)
dll.insert_node(40)
dll.insert_node(50)
dll.find_middle()