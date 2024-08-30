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


def begin_point_of_loop(linkedList):
        slow = linkedList.head
        fast = linkedList.head
        
        while fast and fast.ref:

            slow = slow.ref
            fast = fast.ref.ref


            if slow == fast:
                slow = linkedList.head

                while slow != fast:
                    slow = slow.ref
                    fast = fast.ref

                return slow.data
        
        return "None"

ll1 = LinkedList()
ll1.add_node(10)
ll1.add_node(20)
ll1.add_node(30)
ll1.add_node(40)
#creating a loop last node points to the second node
second_node = ll1.head.ref
n = ll1.head
while n.ref:
    n = n.ref
n.ref = second_node
print(begin_point_of_loop(ll1))