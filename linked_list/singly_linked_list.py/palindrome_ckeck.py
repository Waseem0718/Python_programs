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
    
    def print_ll(self):
        if self.head is None:
            print("LL is Empty")
        else:
            n = self.head
            while n is not None:
                 print(n.data,end="->")
                 n = n.ref
            print("None") 
            
    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def palindrome_check(self):
        #finding the middle element
        if self.head is None or self.head.ref is None:
            return True
        
        slow = self.head
        fast = self.head

        while fast and fast.ref:
            slow = slow.ref
            fast = fast.ref.ref

        temp = slow
        prev = None
        #revrsing the second half
        while temp is not None:
            front = temp.ref
            temp.ref = prev
            prev = temp
            temp = front

        start = self.head
        #checking first half and second half
        while prev is not None:
            if start.data != prev.data:
                return "False"
            else:
                start = start.ref
                prev = prev.ref
        return "True"
    
ll1 = LinkedList()
ll1.add_node(20)
ll1.add_node(30)
ll1.add_node(40)
ll1.add_node(30)
ll1.add_node(20)
print(ll1.palindrome_check())

