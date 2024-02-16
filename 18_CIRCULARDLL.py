class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
        self.length = 0
class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length= 0 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    # 1. CREATE CDLL
    def create(self, value):
        newnode = Node(value)
        self.head = self.tail = newnode
        newnode.next = newnode.prev = newnode
        self.length += 1
        return ' created succesfully'
    
    # 2. INSERT 
    def insertcdll(self, value, index):
        newnode = Node(value)
        if self.head is None:
            return 'empty list'
        else:
            if index == 0:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.tail.next = newnode
                
                self.head = newnode
            elif index == -1:
                newnode.prev = self.tail
                self.tail.next = newnode
                newnode.next = self.head
                self.tail = newnode
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
        
    # 3. TRAVERSE
    def traversecdll(self):
        if self.head is None:
            return 'empty list'
        else:
            currentnode = self.head
            while currentnode:
                print(currentnode.value)
                currentnode = currentnode.next
                if currentnode == self.head:
                    break
            return 'traversed successfully'
    # 4. REVERSE TRAVERSE
    def reversetraverse(self):
        if self.head is None:
            return 'empty list'
        else:
            currentnode = self.tail
            while currentnode:
                print(currentnode.value)
                if currentnode == self.head:
                    break
                currentnode = currentnode.prev
            return 'traversed successfull'
    
    # 5. SEARCH
    def searccdll(self, target):
        if self.head is None:
            return 'empty list'
        else:
            currentnode = self.head
            idx = 0
            while currentnode:
                if currentnode.value == target:
                    return f'found {target} at {idx}th position'
                if currentnode == self.tail:
                    break
                currentnode = currentnode.next
                idx += 1
            return ' not found'    
    
    # 6. DELETE A NODE
    def deletenode(self, index):
        if self.head is None:
            return 'empty list'
        else:
            if self.length == 1:
                self.head.next = self.head.prev = None
                self.head = self.tail = None
            else:
                if index == 0:
                    poppednode = self.head
                    self.tail.next = poppednode.next
                    self.head = poppednode.next
                    self.head.prev = self.tail
                    
                elif index == -1:
                    poppednode = self.tail
                    prevnode = poppednode.prev
                    self.tail = prevnode
                    prevnode.next = self.head
                    self.head.prev = prevnode
                    poppednode.next = None
                    
                else:
                    idx = 0
                    currentnode = self.head
                    while idx < index-1:
                        currentnode = currentnode.next
                        idx += 1
                        if currentnode == self.head:
                            break
                    poppednode = currentnode.next
                    poppednode.next.prev = currentnode
                    currentnode.next = poppednode.next
                self.length -= 1
                return poppednode.value
    # DELETE ENTIRE LIST
    def deletecdll(self):
        if self.head is None:
            return 'empty list'
        else:
            self.tail.next = None
            currentnode = self.head
            while currentnode:
                currentnode.prev = None
                currentnode = currentnode.next
            self.head = None
            self.tail = None
            self.length = 0
            return 'deleted successfully'


                


        


cdll = CircularDoubleLinkedList() 

# 1.CREATE tc:o(1) ; sc:o(1)
cdll.create(5)

# 2. INSERT  tc: O(n) ; sc:O(1)
cdll.insertcdll(2 , 0)
cdll.insertcdll(9 , 0)
cdll.insertcdll(3 , 2)
cdll.insertcdll(10, -1)

# 3. TRAVERSE  tc: O(n) ; sc:O(1)
# cdll.traversecdll()
print([node.value for node in cdll])

# 4. REVERSE TRAVERSE tc:O() ; sc:O()
# print(cdll.reversetraverse())

# 5. SEARCH  tc:O(n) ; sc:O(1)
# print(cdll.searccdll(1))

# 6. DELETE 
# print(cdll.deletenode(2))
# print([node.value for node in cdll])
print(cdll.length)

# 7. DELETE THE LIST
print(cdll.deletecdll())
print([node.value for node in cdll])
print(cdll.length)