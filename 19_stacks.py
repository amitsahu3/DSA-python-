# # 1. without size limit
# class Stack:
#     def __init__(self):
#         self.list = []

#     def __str__(self):
#         values = self.list.reverse()      # to print the stack in LIFO manner
#         values = [str(x) for x in self.list]      # converting them into string
#         return '\n'.join(values)
#     """ tc: O(1) ; sc: O(1)creating an empty list only """
#     # 1. empty method
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
    
#     # 2. push 
#     # as size is not defined hence simple append method is used
#     def push(self, value):
#         self.list.append(value)
#         return "element inserted successfully"

#     # 3. pop
#     def pop(self):
#         if self.isEmpty():
#             return " empty stack"
#         else:
#             return self.list.pop()
    
#     # 4. peek         # to see the top value in stack
#     def peek(self):
#         if self.isEmpty():
#             return "empty list"
#         else:
#             return self.list[len(self.list)-1] # return self.list[0]
    
#     # 5. entire stack deletion
#     def delete(self):
#         self.list = []
#         print("stack deleted successflly")
# customStack = Stack()
# # 1. isEmpty
# #print(customStack.isEmpty())
# #""" tc: O(1) checking if the list is empty or not ; sc: O(1) as no additional space is required"""

# # 2. push
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# """tc: O(n)/O(n2) as it is amortized constant ,every time the list reach its limit required memory along with some additional memory is allocated, if more and more space is required then it may reach to O(n2 ; sc: O(1) as we are appending just one element at the end"""
# print(customStack)


# # # # 3. pop
# # print(customStack.pop())
# # # """tc: O(1) ; sc:O(1)"""
# # print("after pop")
# # print(customStack)

# # # 4. peek
# # print(customStack.peek())
# # """tc: O(1) as accessing last element directly; sc: O(1) as no new space is created"""

# # 5. delete entire stack
# customStack.delete()
# """tc: O(1) as accessing last element directly; sc: O(1) as no new space is created"""
# print(customStack)

# # 2 . STACK WITH SIZE LIMIT
# class Stack:
#     def __init__(self, maxSize):
#         self.maxSize = maxSize
#         self.list = []
    
#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)
#     """tc: O(1), sc: O(1) only initialising """

#     # 1. isEmpty
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False

#     # 2. isFull
#     def isFull(self):
#         if len(self.list) == self.maxSize:
#             return True
#         else:
#             return False
#     """tc: O(1), sc: O(1) only comparing the values """

#     # push
#     def push(self, value):
#         if self.isFull():
#             return "stack full"
#         else:
#             self.list.append(value)
#             return " appended successfully"

#     # pop
#     def pop(self):
#         if self.isEmpty():
#             return " empty stack"
#         else:
#             return self.list.pop()
    
#     # peek
#     def peek(self):
#         if self.isEmpty():
#             return " stack empty"
#         else:
#             return self.list[len(self.list)-1]

#     # delete
#     def delete(self):
#         self.list = None

# customStack = Stack()

# 3. USING LINKED LIST
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None   

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linkedlist]
        return '\n'.join(values)

    # 1. EMPTY
    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
    """tc : O(1) ; sc : O(1)"""

    # 2. PUSH
    def push(self, value):
        node = Node(value)
        node.next = self.linkedlist.head
        self.linkedlist.head = node
    """tc : O(1) ; sc : O(1)"""

    # 3. POP
    def pop(self):
        if self.isEmpty():
            return " empty stack"
        else:
            nodeValue = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return nodeValue
    """ tc: O(1) ; sc : O(1)"""

    # 4. PEEK
    def peek(self):
        if self.isEmpty():
            return " stack empty"
        else:
            nodeValue = self.linkedlist.head.value
            return nodeValue
    """ tc: O(1) ; sc : O(1) """

    # 5. DELETE
    def delete(self):
        self.linkedlist.head = None
        return " deleted successfully"
    """ tc: O(1) ; sc : O(1) """  



customStack = Stack()

# 1. empty
#print(customStack.isEmpty())

# 2. push
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("--------------")

# # 3. pop
# customStack.pop()
# print(customStack)

# # 4. peek
# print(customStack.peek())

# 5. delete
print(customStack.delete())








    