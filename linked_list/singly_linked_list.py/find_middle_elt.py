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
    #using tortoise and  hare algoritm
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.ref:
            fast = fast.ref.ref
            slow = slow.ref
          

        print(slow.data)

        

ll1 = LinkedList()
ll1.add_node(10)
ll1.add_node(20)
ll1.add_node(30)
ll1.add_node(40)
ll1.add_node(50)
ll1.add_node(60)
ll1.add_node(70)
ll1.find_middle()

    
    
    