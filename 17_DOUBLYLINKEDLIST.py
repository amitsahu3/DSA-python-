class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
    
    def __iter__(self):
        node = self.head 
        while node:
            yield node
            node = node.next
    
    # 1. CREATING DLL
    def createdll(self, value):
        newnode = Node(value)
        newnode.prev = newnode.next = None
        self.head = self.tail = newnode
        self.length += 1
        return 'created succesfully'
    # 2. INSERTION 
    def insertdll(self, value, index):
        newnode = Node(value)
        if index < -1 or index > self.length:
            return 'enter valid index'
        else:
            # 1. at the beginning 
            if index == 0:
                if self.head is None:       # if empty
                    self.head = newnode
                    self.tail =  newnode
                else :
                    firstnode = self.head
                    self.head = newnode
                    newnode.next = firstnode
                    firstnode.prev = newnode
            
            # 2. at the end
            elif index == -1:
                if self. head is None:
                    self.head = self.tail = newnode
                else:
                    newnode.prev = self.tail
                    self.tail.next = newnode
                    self.tail = newnode
            # 3. at any given location
            else:
                idx = 0
                currentnode = self.head
                while idx < index-1:
                    currentnode = currentnode.next
                    idx += 1
                nextnode = currentnode.next
                currentnode.next = newnode
                newnode.prev = currentnode
                newnode.next = nextnode
                nextnode.prev = newnode
            self.length += 1

        return ' inserted successfully'
    
    # 3. TRAVERSAL 
    def traversedll(self):
        if self.head is None:
            return 'empty list'
        else:
            if self.length == 1:
                return self.head
            else:
                currentnode = self.head
                while currentnode:
                    print(currentnode.value)
                    currentnode = currentnode.next
        return 'traversed successfully'
    
    # 4. REVERSE TRAVERSAL 
    def reversetraversedll(self):
        if self.head is None:
            return 'empty list'
        else:
            currentnode = self.tail
            while currentnode is not self.head:
                print(currentnode.value)
                currentnode = currentnode.prev
            return ' reverse traversed successfully'
    
    # 5. SEARCH
    def searchdll(self, target):
        if self.head is None:
            return 'empty list'
        else:
            idx = 0 
            currentnode = self.head
            while currentnode:
                if currentnode.value == target :
                    return f'found {target} at {idx}th index'
                else:
                    currentnode = currentnode.next
                    idx += 1
            return ' not found'
    
    # 6. DELETION 
    def deletedll(self, index):
        if self.head is None:
            return 'empty list'
        else:
            if index < -1 or index > self.length:
                return 'out of bounds'
            else:

                if index == 0:
                    poppednode = self.head
                    self.head = poppednode.next
                    poppednode.next.prev = None
                elif index == - 1:
                    poppednode = self.tail
                    self.tail = poppednode.prev
                    poppednode.prev.next = None
                else:
                    idx = 0
                    currentnode = self.head
                    while idx < index -1 :
                        currentnode = currentnode.next
                        idx += 1
                    poppednode = currentnode.next
                    currentnode.next = poppednode.next
                    poppednode.prev = None
                    poppednode.next.prev = currentnode
                    poppednode.next = None
                    
                return poppednode.value
            
    # 7. DELETE ENTIRE NODE
    def deletedoublyll(self):
        if self.head is None:
            return 'empty list'
        else:
            currentnode = self.head
            while currentnode:
                currentnode.prev = None
                currentnode = currentnode.next
            self.head = self.tail = None
            return 'deleted successfully'

                
                


# 1. CREATION tc:O(1) ; sc:O(1)    
doublyll = DoublyLinkedList()
doublyll.createdll(5)

# 2. INSERTION
doublyll.insertdll(10,0)
doublyll.insertdll(11,-1)
doublyll.insertdll(14,0)
doublyll.insertdll(100,2)
doublyll.insertdll(99,1)
print([node.value for node in doublyll])

# 3. TRAVERSAL  tc:O(n) ; sc:O(1)
# print(doublyll.traversedll())

# 4. REVERSE TRAVERSE     tc:O(n) ; sc:O(1)
# print(doublyll.reversetraversedll())

# 5. SEARCH LIST tc:O(n) ; sc:O(1)
# print(doublyll.searchdll(9))

# 6. DELETE NODE tc:O(n) ; sc:(1)
# print(doublyll.deletedll(9))


# 7. DELETE ENTIRE LIST  tc:O(n) ; sc:(1)
# print(doublyll.deletedoublyll())
# print([node.value for node in doublyll])