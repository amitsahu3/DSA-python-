class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class circularsll():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # CREATION
    def createcsll(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        return "the csll created"
    
    #   INSERTION
    def insertcsll(self, value, location):
        if self.head is None:
            return "head ref is None"
        else:
            newNode = Node(value)

            # at the begining
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            
            # at the end 
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next =  newNode
                self.tail =  newNode

            # at the middle
            else:
                tempNode = self.head        # created to traverse and store current node value
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1 
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return " node has been successfully inserted"

    # TRAVERSAL
    def traversecsll(self):
        if self.head is None:
            print("empty list")
        else:
            tempNode = self.head
            while tempNode :     # while tempNode exist
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:      # stopping condition,check if we've reached the last node or not (last node ref to first node )
                    break
    # SEARCHING 
    def searchcsll(self, nodeValue):
        if self.head is None:
            print("empty list")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:      # as if we dont stop at tail ,loop will run infinetly
                    return " not found"
    """ we can get into infinite loop as csll is looped,so every time we visit the node ,we check if its the tail value or not"""  

    def deletecsll(self, location):
        if self.head is None :
            print("list empty")
        else:
            # deleting from the begining
            if location == 0:
                # if only one node
                if self.head == self.tail:  # only one element 
                    self.head = None
                    self.tail = None
                    self.head.next = None # the first element as it is rferenced by head 
                
                # more than one node
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            
            # deleting from the end
            elif location == -1:
                # for single element 
                if self.head == self.tail:
                    self.head = None
                    self.tail = None                    
                    self.head.next = None
                
                # more than one element
                else:
                    node = self.head    # temp nodeused to loop the ll
                    while node.next.next != self.head:
                        node = node.next
                    node.next = self.head
                    self.tail = node
            
            # deleting from any position
            else:
                tempNode = self.head
                index = 0
                while index < location-1: # O(n)
                        tempNode = tempNode.next    # for looping like i++
                        index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # deleting the entire node
    def deletecsllALL(self):
        self.head = None
        self.tail.next = None
        self.tail

        # another method
        # node = self.head
        # while node.next != self.head:
        #     node = node.next
        # node.next = None
        # self.head = None
        # self.tail = None

# creating csll object
csll = circularsll()

# creating csll
csll.createcsll(1)
""" tc: O(1); sc:O(1) as we have just created one node """

# insert csll
""" tc:O(n) ; sc:(1) only two nodes are created  """
csll.insertcsll(0,0)
csll.insertcsll(2,1)
csll.insertcsll(3,1)
csll.insertcsll(2,-1)
csll.insertcsll(9,-1)

# # # traversal
# # csll.traversecsll()
# # """ tc:O(n); sc:O(1) creating only one tempNode """

# # # searching
# # print(csll.searchcsll(4))
# """ tc: O(n); sc:O(1) as one tempNode created"""

# # # deleting
# csll.deletecsll(-1)
# """ tc: O(n) as one loop ; sc: O(1) as only two extra nodes are created  """

# deleting the entire csll
#csll.deletecsllALL()
""" tc: O(1) as we are setting everthing to none ; sc: O(1)"""
print([node.value for node in csll])

