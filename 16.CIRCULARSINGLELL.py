class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    # def __str__(self) :     # will return node value when print is called for node
    #     return str(self.value)
    
class CircularSingleLinkedList:
    def __init__(self):      
        self.head = None
        self.tail = None
        self.length = 0 

    # PRINTING THE CSLL
    def __str__(self):
        tempNode = self.head
        result = ' '
        while tempNode is not None:
            result += str(tempNode.value)
            tempNode = tempNode.next
            if tempNode == self.head:
                break
            result += ' --> '
        return result
    # 1. APPEND IN CSLL
    def append(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail =  newnode
            newnode.next = newnode
        else:
            self.tail.next = newnode
            newnode.next = self.head
            self.tail = newnode
        self.length += 1
        return 'appendded successfully'
    
    # 2. PREPEND
    def prepend(self, value):
        if self.head is None:
            self.append(value)
        else:
            newnode = Node(value)
            newnode.next = self.head
            self.head = newnode
            self.tail.next = newnode
        self.length += 1

    # 3. INSERT AT ANY GIVEN LOCATION
    def isnertcsll(self, value, location):
        if location < -1 or location > self.length:
            return ' enter valid index'
        else:
            newnode = Node(value)
            if self.head is None or location == -1:
                self.append(value)
            elif location == 0:
                self.prepend(value)
            else:
                idx = 0
                currnode = self.head
                while idx < location-1:
                    currnode = currnode.next
                    idx += 1
                nextnode = currnode.next
                newnode.next = nextnode
                currnode.next = newnode
                self.length += 1

        return 'inserted successfully'
    
    # 4. TRAVERSAL 
    def traversecsll(self):
        if self.head is None:
            print('empty list')
        else:
            currentnode = self.head
            while currentnode is not None:
                print(currentnode.value)
                currentnode = currentnode.next
                if currentnode == self.head :
                    break

    # 5. SEARCH LIST
    def searachcsll(self, target):
        if self.head is None:
            return ' empty list'
        else:
            currnode = self.head
            while currnode:
                if currnode.value == target:  
                    return 'found'
                currnode = currnode.next
                if currnode == self.head:
                    break
            return 'not found'      
        
    # 6. GET() METHOD : returns the node value for given index
    def get(self, index):
        if index < -1 or index > self.length:
            return ' out of bound index'
        if self.head is None:
            return 'empty list'
        if index == -1:
            return self.tail
        else:
            currnode = self.head
            idx = 0
            while idx <= index-1:
                currnode = currnode.next
                idx += 1
                if currnode == self.head:
                    break
            # return f'{currnode.next} at {index}th position'
            return currnode

    # 7. SET () : set a value at a particular position
    def set_value(self, index, value):
        if self.head is None:
            return 'empty list'
        else:
            node = self.get(index)
            node.value = value
            return ' updated successfully'
        
    # 8. POP_FIRST()
    def pop_first(self):
        if self.head is None:
            return 'empty list'
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            return popped_node
        else:
            popped_node = self.head
            second_node = popped_node.next
            popped_node.next = None
            self.head = second_node
            self.tail.next = second_node
            self.length -= 1
            return popped_node
    
    # 9. POP() METHOD
    def pop(self):
        if self.length == 0:
            return 'empty list'
        elif self.length == 1:
            popped_node = self.head
            popped_node.next = None
            self.head = None
            self.tail = None
            return popped_node
        else:
            idx = 0
            currentnode = self.head
            while idx < self.length -2:
                currentnode = currentnode.next
                idx += 1
            popped_node = currentnode.next
            popped_node.next = None
            self.tail = currentnode
            currentnode.next = self.head
            self.length -= 1
            return popped_node
    
    # 10. REMOVE
    def remove_node(self, index):
        if index < -1 or index > self.length:
            return 'index out of bounds'
        else:
            if self.head is None:
                return ' empty list'
            elif index == 0:
                return self.pop_first()
            elif self.length == 1 or index == -1:
                return self.pop()
            else:
                idx = 0
                currentnode = self.head
                while idx < index-1 :           # can use get method also
                    currentnode = currentnode.next
                    idx += 1
                    if currentnode == self.head:
                        break
                poppednode = currentnode.next
                currentnode.next = poppednode.next
                poppednode.next = None
                self.length -= 1
                return poppednode
            
    # 10. DELETE ALL NODES
    def deletell(self):
        # if self.head is None:
        #     return 'empty list'
        # else:
        #     currentnode =  self.head
        #     while currentnode :
        #         prevnode = currentnode
        #         currentnode = currentnode.next
        #         prevnode.next = None
        #         if currentnode == self.head :
        #             break
        #     currentnode.next = None
        #     self.head = self.tail = None
        #     return 'deleted'
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0


        



csll = CircularSingleLinkedList()

# 1. CREATING A CSLL: tc:O(1), sc:O(1)

# 2. APPENDING 
csll.append(1)
csll.append(2)
csll.append(3)
csll.append(4)


# 3. PREPEND  tc:O(1), sc:O(1)
csll.prepend(10)

# 3. INSERT  tc:O(n), sc:O(1)
csll.isnertcsll(90, 2)

# 4. TRAVERSAL  tc:O(n), sc:O(1)
# csll.traversecsll()
# print(csll)
# print(csll.length)

# 5. SEARCH IN LIST  tc:O(n), sc:O(1)
# print(csll.searachcsll(90))

# 6. GET METHOD  tc:O(n) ; sc:O(1)
# print(csll.get(3))

print(csll)
# 7. SET() METHOD  tc:O(n) ; sc:O(1)
# print(csll.get(3).value)
# csll.set_value(3,11)

# 8. POP_FIRST() : remove and return the first node   tc:O(1) ; sc:O(1)
# print(csll.pop_first().value)

# 9. POP()  tc:O(n); sc:O(1)
# print(csll.pop().value)

# 10. REMOVE NODES   tc:O(n) ; sc :O(1)
# print(csll.remove_node(3).value)

# 11. DELETE THE ENTIRE LIST  tc:O(1) ; sc:O(1)
print(csll.deletell())
print(csll)