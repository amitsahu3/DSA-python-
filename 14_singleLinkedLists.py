class Node:
    def __init__(self, value = None):   # O(1)
        
        # as a node has value and location of next node
        self.value = value
        self.next = None

class singlell:
    def __init__(self):    # tc:O(1) ; sc:O(1)
        self.head = None
        self.tail = None

    def __iter__(self):     # function for printing the list 
        node = self.head
        while node:
            yield node
            node = node.next

    # INSERTION IN SINGLE LINKED LIST
    def insertsll(self, value, location):
        newNode = Node(value)                # creating a new node and specify value to it

    # inserting in empty list  
        if self.head is None:      # O(1) assigning oly        # checking if list is empty or not( None means we dont have any node in our list )
            self.head = newNode             # setting head and tail references to new node
            self.tail = newNode
        
    # inserting 
        else:
            # at the begining
            if location == 0:
                newNode.next = self.head  # O(1)    # as head stores the reference of first element and we traverse list alaways from head(it breaks the link b/w initial first node and head and creates link b/w itself and the  initial first node)
                self.head = newNode                 # now the head stores the reference of newNode into it making it the first node
            # at the end
            elif location  == -1:
            #     newNode.next = None       # as last node alwayas has None
            #     self.tail.next = newNode  # O(1)  # as tail refers to the last node,accessing next value of tail, means we are accessing the next refernce last node (creates link b/w last node and newnode)
            #     self.tail = newNode               # creating refernce b/w tail and new node
                node = self.head
                while node.next is not None:
                    node = node.next 
                node.next = newNode
            

            # as we are adding at the begining and the end so we store the value of first and last node in head and tail,so thats why we are changing links and values to them
            else:
                tempNode = self.head        # we have to traverse and find the location and also we start from head so storing it in tempNode
                index = 0
                # traverse till recach loaction and keep storing the next node
                while index < location -1:
                    tempNode = tempNode.next    # O(n)
                    index += 1
                # now tempNode = current node so we need to find the next node as we have to insert b/w thesw two
                nextNode = tempNode.next    # as tempNode is current node and so its next value is next node ,we assign that next value to the newly created next node
                tempNode.next = newNode     # as tempNode is current node so assigning its next refernce the value of new node
                newNode.next = nextNode     # assiging newNodes next value to nextNode as it stores nextNodes location
                if tempNode == self.tail:
                    self.tail = newNode
            # it is kind of exchanging numbers ,storing next value of current node/tempNode to an empthy next node ,then empty tempNodes next to newNode and finally empty newNode next to nextNode

# TRAVERSAL
    def traversesll(self):  # self as it is inside a class and initialises itself
        if self.head is None:   # no nodes ; O(1)
            print("SLL doesn't exist. ")    # O(1)
        else:
            node = self.head    # O(1) ; we take a variable node and initialise it with head as it contains value of first node and we travers from first node
            while node is not None :    # node becomes none means its the end of list as none is sstored on the last node
                print(node.value)   # O(n)
                node = node.next     # we point towards next node by using next keyword

# SEARCHING 
    def searchsll(self, nodeValue):
        if self.head is None:   # O(1) as only checking head is None or not
            print("list doesnt exist")
        else:
            node = self.head    # O(1)
            while node is not None: # O(n) looping through any loop  
                if node.value == nodeValue:
                    return node.value   # O(1)
                node = node.next        # if node.value is not nodeValue then move to the next node
            return " the value doesnot exist "  # if we cant find the element in this loop means it doesnot exist in the list 
# DELETION NODES
    def deleteNode(self, location):
        # if node is empty or not
        if self.head is None:
            print("lsit is empty !")
        else:
            # from the begining
            if location == 0:
                if self.head == self.tail:  # if head and tail point to the same element,means there's only one node in the list
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            # from the end        
            elif location == -1:
                if self.head == self.tail:  # if head and tail point to the same element,means there's only one node in the list
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next.next is not None: # O(n)
                        node = node.next    # for looping like i++
                    node.next = None
                    self.tail = node
            # from anywhere
            else:
                 tempNode = self.head
                 index = 0
                 while index < location-1:
                        tempNode = tempNode.next    # O(n)
                        index += 1
                 nextNode = tempNode.next
                 tempNode.next = nextNode.next
# DELETING THE ENTIRE LIST
    def deletlist(self):
        if self.head is None:
            print("ll is empty ")
        else:
            self.head = None
            self.tail = None




sll = singlell()

# INSERTION
sll.insertsll(2,0)
sll.insertsll(1,1)
sll.insertsll(3,1)
sll.insertsll(4,1)
sll.insertsll(0,0)
sll.insertsll(0,3)
sll.insertsll(5,-1)

""" space comp :O(1) as we are creating only two new nodes that are tempNode and nextNode so no more extra space is required"""

# PRINTING ELEMENTS
print([node.value for node in sll]) 

# # TRAVERSAL
sll.traversesll()       
# """ space cpx: O(1) as we only create one extra node for traversal """


# # SEARCHING
# print(sll.searchsll(88))
# """ space cpx: O(1) as we only create one extra node for traversal """

# # DELETION
# sll.deleteNode(-1)
# print([node.value for node in sll]) 
# """ tc: O(n), sc: O(1) as few variables are needed """

# deleting the entire list 
# sll.deletlist()
# print([node.value for node in sll])
""" tc: O(1), as we are setting the head and tail value to None; sc: O(1) as no new space is created"""
