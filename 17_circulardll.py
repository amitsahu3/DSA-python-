class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class circulardll:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node== self.tail.next:
                break
    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         if node.next == self.head:
    #             break
    #         node = node.next

    # CREATION    
    def createdll(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode

    # INSERTON
    def insertcdll(self,nodeValue, location):
        if self.head is None:
            print("empty list")
        else:
            newNode = Node(nodeValue)
            # begining
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
 
            # end
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            
            # middle
            else:
                tempNode = self.head
                index = 0
                while index < location-1 :
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next.prev = newNode
                tempNode.next = newNode
            return " new node is updated successfully inserted"

    # TRAVERSAL 
    def traversalcdll(self):
        if self.head is None:
            print("empty list")
        node = self.head
        while node:
            print(node.value)
            if node == self.tail:
                break
            node = node.next
        # while node.next != self.head:
        #     print (node.value)
        #     node = node.next
    
    # REVERSE TRAVERSAL
    def reverse_traversal(self):
        if self.head is None:
            print("list empty")
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:   # checking if we reached the first node or not to avoid infiinite loop 
                    break
                node = node.prev
    # SEARCHING
    def searchcdll(self, nodeValue):
        if self.head is None:
            print("empty list")
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    return node.value
                if node == self.tail: 
                    return " node not found"
                node = node.next
    # DELETION 
    def deleteNode(self, location):
        if self.head is None:
            print("empty list ")
        else:
            # from the begining
            if location == 0:
                # only one node
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                # multiple nodes
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
                    # self.tail.next = self.head.next
                    # self.head.next.prev = self.tail
                    # self.head = self.head.next
            # from the end
            elif location == -1:
                # only one node
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            # from any point 
            else:
                currnode = self.head
                index = 0
                while index < location-1:
                    currnode= currnode.next
                    index += 1
                currnode.next = currnode.next.next
                currnode.next.prev = currnode
                # tempNode = currnode.next
                # currnode.next = tempNode.next
                # tempNode.next.prev = currnode 
            print( " node deleted successfully")
    # DELETING THE ENTIRE CDLL
    def deletecdll(self):
        if self.head is None:
            print("empty list")
        else:
            node = self.head
            self.tail.next = None   # break n1-last node so infinite loop is avoided here
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None
            print("cdllist deleted successfully")


                


cdll = circulardll()

# creating cdll
cdll.createdll(5)
""" tc: O(n) while loop ; sc: O(1) newNode is the only extra node"""
# print([node.value for node in cdll]) 

# inserting 
cdll.insertcdll(1, 0)
cdll.insertcdll(3, 1)
cdll.insertcdll(4, 1)
cdll.insertcdll(9,-1)
cdll.insertcdll(11,3)
print([node.value for node in cdll])
""" tc: O(n) ; sc : O(1) as one tempNnode is created """

# # traversal
# cdll.traversalcdll()
# """ tc: O(n) ; sc : O(1) as one tempNnode is created """

# # reverse traversal
# cdll.reverse_traversal()
# """ tc: O(n) ; sc : O(1) as one tempNnode is created """

# # searching
# print(cdll.searchcdll(12))
""" tc: O(n), sc: O(1) """

# deleting nodes
# cdll.deleteNode(-1)
# """tc: O(n), sc: O(1)"""

# deleting complete cdll
cdll.deletecdll()
"""tc: O(n) ; sc: O(1)"""
print([node.value for node in cdll])