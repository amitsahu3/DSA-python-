# single linked list
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.middle_idx = 0

    # PRINTING THE LINKED LIST
    def __str__(self):
        tempNode = self.head
        result = ' '
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += ' --> '
            tempNode = tempNode.next
        return result
        
        

    # APPEND METHOD to add node to the current instance of object(empty list, at the end)  ; TC and SC = O(1)
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    # PREPEND METHOD (to add at the beginning) , TC and SC = O(1)
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1    

    # 1. INSERTING AT ANY GIVEN POSITION           # tc:O(n)  ; sc:O(1)
    def insertsll(self, value, location):
        # checking for false index
        if location < 0 or location > self.length:
                print('invalid index') 
        
        else:
            newNode = Node(value)
            # checking if empty or not
            if self.length == 0:
                self.append(newNode)
            else:
                # at the beginning
                if location == 0:
                    self.prepend(newNode)    

                # at the end
                elif location == self.length - 1:
                    self.append(newNode)

                # at any positon
                else:
                    tempNode = self.head
                    index = 0
                    while index < location-1:
                        index += 1
                        tempNode = tempNode.next
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                
                    self.length += 1
    # 2.TRAVERSAL
    def traversal_sll(self):
        if self.head is None:
            print('empty list')
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next
    
    # 3. SEARCH
    def search_sll(self, target):
        if self.head is None:
            print('empty list')
        else:
            currentNode = self.head
            index = -1
            while currentNode :

                if currentNode.value == target:
                    return f'found at {index}th position'
                index += 1
                currentNode = currentNode.next
            return 'not found'
        
    # 4. GET()
    def get(self, index):
        if index < 0 or index > self.length:
            return ' index out of bounds'
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current
    
    # 5. SET()
    def set_value(self, index, value):
        # currentNode = self.head
        # idx = 0
        # while idx < index:
        #     currentNode = currentNode.next
        #     idx += 1
        # currentNode.value = value

        # usinf get()
        temp = self.get(index)      # it will return the object(index, value)
        if temp:
            temp.value = value
    
    # 6. POP FIRST : rmoves first node from sll and returns that node(moving head to second node and updating the first node next to none)
    def pop_first(self):
        poppedNode = self.head
        if poppedNode is None:
            return 'empty list'
        else:
            if self.length == 1:
                self.head = None
                self.tail = None
                poppedNode.next = None
                return poppedNode.value
            
            self.head = self.head.next
            poppedNode.next = None
            self.length -= 1
            return poppedNode.value
    
    # 7. POP : deletes and returns the last element
    def pop(self):
        if self.length == 0 :
            return 'empty list'
        poppedNode = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return poppedNode.value
    
    # 7. REMOVE 
    def removenode(self, index):

        # if index < -1 or index > self.length:
        #     return 'index out of bounds'
        # currentNode = self.head
        # idx = 0
        # if self.length == 0:
        #     return 'empty list'
        # elif self.length == 1:
        #     return self.pop_first()
        # elif index == (self.length -1 )or index == -1 :
        #     return self.pop()
        # else:
        #     while idx < index-1 :
        #         currentNode = currentNode.next
        #         idx += 1
        #     poppedNode = currentNode.next
        #     currentNode.next = poppedNode.next
        #     poppedNode.next = None
        #     self.length -= 1
        #     return poppedNode.value

        # using get() method
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1 or index == -1:
            return self.pop()
        prev_node = self.get(index-1)
        poppedNode = prev_node.next
        prev_node.next = poppedNode.next
        poppedNode.next = None
        self.length -= 1
        return poppedNode.value
    
    # 8. DELETE ALL NODES
    def deleteAllNodes(self):
        if self.length == 0:
            return 'empty list'
        self.head = None
        self.tail = None 
        self.length = 0
        return ' deleted successfully'
    
    # 9. REVERSAL LINKED LIST
    def reversell(self):
        prevnode = None
        currentnode = self.head
        while currentnode is not None:
            nextnode = currentnode.next
            currentnode.next = prevnode
            prevnode = currentnode
            currentnode = nextnode
        self.head, self.tail = self.tail, self.head
    # 10. FINDING THE MIDDLE ELEMENT
    def findmiddle(self):
        middle_idx = self.length//2 
        idx = 0
        currentnode = self.head
        while idx < middle_idx:
            currentnode = currentnode.next
            idx += 1
        return currentnode.value
    
    # 11. REMOVE DUPLICATES
    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node
    

    # merging and sorting two linkedlist
    def mergelist(self, l1, l2):
        prehead = Node(-1)
 
        prev = prehead
        while l1 and l2:
            if l1.value <= self.list2.value:
                prev.next = self.list1
                self.list1 = self.list1.next
            else:
                prev.next = self.list2
                self.list2 = self.list2.next            
            prev = prev.next
 
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = self.list1 if self.list1 is not None else self.list2
 
        return prehead.next
    
    def remove_nodes(self, val):
        #head = self.head
        dummy_sll = SingleLinkedList()
        dummy_head = Node(-1)
        dummy_head.next = self.head
        prevnode = dummy_head
        currnode = self.head
        while currnode:
            #print(currnode.value)
            if currnode.value == val:
                prevnode = currnode.next 
                # print(prevnode.value)
                dummy_sll.append(prevnode.value)
                currnode = prevnode.next
            else:
                # print(prevnode.next.value)
                dummy_sll.append(prevnode.next.value)
                prevnode = currnode
                currnode = currnode.next
        print(dummy_sll)
        




         
        

   

                


sll1 = SingleLinkedList()
sll2 = SingleLinkedList()
# 1. INSERTION  tc:O(n)  ; sc:O(1)
sll1.append(1)
sll1.append(2)
sll1.append(3)
sll1.prepend(4)
sll1.append(5)
sll1.append(3)
sll1.append(6)
# sll2.append(1)
# sll2.append(2)
# sll2.append(3)
# sll2.prepend(4)
# sll2.append(9)
# sll.prepend(100)
# sll.insertsll(89,-1)

# 2. TRAVERSAL  tc:O(n) ; sc:(1)
# print(sll)
# sll.traversal_sll()

# 3. SEARCH  tc: O(n) ; sc(1)
# print(sll.search_sll(10))

# 4. Get()              # tc:O(n) ; sc:O(1)
# print(sll.get(2).value)          

# 5. SET()              # tc:O(n) ; sc:O(1)
# print(sll)
# sll.set_value(2,90)
# print(sll)

# 6. POP FIRST             # tc:O(1) ; sc:O(1)
# print(sll)
# print(sll.pop_first())
# print(sll.pop_first())
# print(sll)

# 7. POP                    # tc : O(n) ; sc :O(1)
# print(sll)
# print(sll.pop())
# print(sll)

# 7. REMOVE                    # tc : O(n) ; sc :O(1)
# print(sll)
# print(sll.length)
# print(sll.removenode(1))
# print(sll)
# print(sll.length)

# 7. DELETE ALL NODES                    # tc : O(1) ; sc :O(1)
# print(sll.deleteAllNodes())
# print(sll1)
# print(sll1.length)
# print(sll2)
# print(sll2.length)
# print(sll.findmiddle())
print(sll1)
#sll1.remove_nodes(3)

class Solution(object):
    def reverselist(self, head):
        prevnode = None
        currnode = head
        while currnode is not None:
            nextnode = currnode.next
            currnode.next = prevnode
            prevnode = currnode
            currnode = nextnode
        return prevnode.value
solution = Solution()
print(solution.reverselist(sll1.head))