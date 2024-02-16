#improved code
# class Node:
#     def __init__(self, value= None):
#         self.value = value
#         self.next = None
#         self.prev = None

# class doublell:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node =node.next
#     def createdll(self, nodevalue):
#         newnode= Node(nodevalue)
#         newnode.next =None
#         newnode.prev=None
#         self.head =newnode
#         self.tail = newnode
#         return " created successfully"
    
#     def countnodes(self, dll):        # in order to check if the ll is as long as the given loaction
#         self.count = 0
#         for _ in dll:
#             self.count+=1
#         return self.count  
#     def insert(self, nodevalue, location):        # if insertion is called and list is empty then create a list with the value
#         if self.head is None:
#             self.createdll(nodevalue)
#         else:
#             if location <= (self.countnodes(dll)):
#                 newnode = Node(nodevalue)
#                 if location == 0 :
#                     newnode.prev = None
#                     newnode.next = self.head
#                     self.head.prev = newnode
#                     self.head = newnode
#                 elif location == -1:
#                     newnode.next = None
#                     newnode.prev = self.tail
#                     self.tail.next = newnode
#                     self.tail = newnode
#                 else:
#                     index = 0
#                     tempnode = self.head
#                     while index<location-1:
#                         tempnode=tempnode.next
#                         index+=1
#                     newnode.next = tempnode.next
#                     newnode.prev = tempnode
#                     newnode.next.prev = newnode
#                     tempnode.next = newnode
                
#         return " inserted successfully"
class Node:
    def __init__(self, value):
        self.value = value   # defining value and prev and next references of the node
        self.next = None
        self.prev = None
    
class doublyll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # CREATING DLL
    def createdll(self, nodeValue):
        node = Node(nodeValue)  # initialising the node
        node.prev = None        # setting prev to none
        node.next = None        # setting next to none
        self.head = node        # setting head to node
        self.tail = node        # setting tail to node
        return " dll created"
    
    # INSERTION
    def insertNode(self,nodeValue, location):
        if self.head is None :
            print("dll empty")
        else:
            newNode = Node(nodeValue)

            # at the begining
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode 
            
            # at the end 
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            
            # at any location
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                # newNode.next = tempNode.next
                # tempNode.next.prev = newNode
                # newNode.prev = tempNode
                # tempNode.next = newNode 
    # TRAVERSAL
    def traversedll(self):
        if self.head is None:
            print("emepty list")
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next
    # REVERSE TRAVERSAL
    def reverseTraversedll(self):
        if self.head is None:
            print('empty list')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    # SEARCHING
    def searchdll(self, nodevalue):
        if self.head is None:
            return "empty list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodevalue:
                    return tempNode.value
                tempNode = tempNode.next
            return "not found"
    
    # DELETION
    def deleteNode(self,location):
        if self.head is None:
            return " empty list"
        else:
            # from the begining
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            
            # from the end
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            
            # middle of the list
            else:
                tempNode = self.head
                index = 0
                while index < location-1 :
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                nextNode.next.prev = tempNode
    # DELETING THE ENTIRE LIST
    def deletedll(self):
        node = self.head
        while node:
            node.prev = None
            node = node.next
        self.head = None
        self.tail = None
         







dll = doublyll()    # object creation

# creating dll
dll.createdll(5)     

# inserting
dll.insertNode(2,0)
dll.insertNode(3,1)
dll.insertNode(10,-1)
dll.insertNode(8,2)
"""tc:O(n) while loop ; sc:O(1) as two new nodes only """
print([node.value for node in dll])

# # traversing
# dll.traversedll()
# """tc:O(n) while loop ; sc:O(1) only one tempNode is created """

# # reverser traversing
# dll.reverseTraversedll()
# """tc:O(n) while loop ; sc:O(1) as two new nodes only """

# # searching
# print(dll.searchdll(9))
# """ tc:O(n) while loop; sc:O(1) tempNode only"""

# deletion
# dll.deleteNode(2)
# """ tc: O(n) while loop; sc: O(1) as only two variables"""

# entire list deletion
dll.deletedll()
""" tc:O(n) as while loop ; sc:O(1) as only one node is created"""
print([node.value for node in dll])
    
