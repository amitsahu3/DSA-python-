# #1. USING LIST WIHTOUT LIMIT
# class Queue:
#     def __init__(self):
#         self.items = []
#     def __str__(self):
#         # creating another list to store converted items
#         values = [str(x) for x in self.items]
#         return ' '.join(values)
    
#     # 1. isEmpty
#     def isEmpty(self):
#         if self.items == [ ]:
#             return True
#         else:
#             return False
#     """ tc:O(1) ; sc O(1)"""
    
#     # 2. enqueue
#     def enqueue(self, value):
#         self.items.append(value)
#         return " element isnserted at the end"
#     """ tc: O(1)/O(N)/O(N2) as append is ammortised ; sc : o(1) only one element is added each time"""
    
#     # 3. dequeue
#     def dequeue(self):
#         if self.isEmpty():
#             return " empty queue"
#         else:
#             return self.items.pop(0)
#     """tc: O(n) if starting element is removed then all elements have to be shifted towards left ; sc: O(1) removing one element"""
    
#     # 4. peek 
#     def peek(self):
#         if self.isEmpty():
#             return " empty list"
#         else:
#             return self.items[0]
#     """ tc : O(1); sc :O(1)"""

#     # 5. delete 
#     def deleteQueue(self):
#         self.items = []
#         return " deleted successfully"
# customQueue = Queue()

# #1. isEmpty
# #print(customQueue.isEmpty())
 
# #2. enqueue
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# print(customQueue)

# # 3. dequeue
# # print(customQueue.dequeue())

# #4. peek
# #print(customQueue.peek())
# #print(customQueue)
# print(customQueue.deleteQueue())
# print(customQueue)

# #2. WITH FIXED SIZE
# """ it helps in dealing the problem with expanding size as it will become circular queue"""

# class Queue:
#     def __init__(self, maxSize):
#         self.items = maxSize * [None]   # if we want an empty list, we need to set all cells to none on python
#         self.maxSize = maxSize
#         # initially s and t are both -1
#         self.start = -1
#         self.top = -1
#     """tc : O(1) sc : O(n)"""    
#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return ' '.join(values)

#     # 1. isFull
#     def isFull(self):
#         if self.top + 1 == self.start:  # means no space as t is just behind s
#             return True
#         elif self.start == 0 and self.top + 1 == self.maxSize: # means no space as s is at start(0) and t is at the end of queue
#             return True 
#         else:
#             return False
#     """tc : O(1) ; sc : O(1)"""

#     # 2. isEmpty
#     def isEmpty(self):
#         if self.top == -1:  # as we change top when we enqueue and if t = -1 means therse no element inserted 
#             return True
#         else:
#             return False
#     """tc : O(1) ; sc : O(1)"""

#     # 3. enqueue
#     def enqueue(self ,value):
#         if self.isFull():
#             return " queue is full"
#         else:
#             if self.top + 1 == self.maxSize:    # top is at the end we need to reset it to 0
#                 self.top = 0 
#             else:
#                 self.top +=1  # if not at the end of list than increment by 1
#                 # also need to update start
#                 if self.start == -1:    # means no element in the list
#                     self.start = 0  # if so, then we need to update start to 0
#             self.items[self.top] = value
#             return " element isnerted at the end"
#     """tc : O(1) ; sc: O(1)"""

#     # 4. dequeue
#     def dequeue(self):
#         if self.isEmpty():
#             return " empty queue"
#         else:
#             # first return the value to be deleted and start variable to start
#             firstElement = self.items[self.start]
#             start = self.start

#             # if only element in the list, set start and top to -1
#             if self.start == self.top:
#                 self.start = -1
#                 self.top = -1
            
#             # if start is at the end so we need to bring it back to begining
#             elif self.start + 1 == self.maxSize:
#                 self.start = 0

#             # else increment start by 1
#             else:
#                 self.start += 1

#             # after setting start we need to update that blank to none
#             self.items[start] = None
#             return firstElement
#     """tc : O(1) ; sc : O(1)"""

#     # 5. peek
#     def peek(self):
#         if self.isEmpty():
#             return " empty queue"
#         else:
#             return self.items[self.start]
#     """tc : O(1) ; sc : O(1)"""

#     # 6. delete
#     def delete(self):
#        self.items = self.maxSize * [None]
#        self.start = -1
#        self.top = -1
#     """tc : O(1) ; sc : O(1)"""

# customQueue = Queue(3)
# # #1. isFull
# # print(customQueue.isFull())

# # #2. isEmpty
# # print(customQueue.isEmpty())

# #3. enqueue
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# print(customQueue)

# #4. dequeue
# # print(customQueue.dequeue())

# #5. peek
# # print(customQueue.peek())
 
# #6. delete
# customQueue.delete()
# print(customQueue)

#3. QUEUE WITH LINKED LIST
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):      # to make linked list iterable
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()
    """tc ; O(1) ; sc: O(1)"""

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)
     # 1. enqueue
    def enqueue(self, value):
        newNode = Node(value)

        # if no nodes
        if self.linkedlist.head == None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        # if nodes exist already
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode
    """ tc: O(1) ; sc: O(1)"""

    # 2. isEmpty(used inside dequeue method)
    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False
    """ tc: O(1) ; sc: O(1)"""

    # 3. dequeue
    def dequeue(self):
        if self.isEmpty():
            return "empty queue"
        else:
            tempNode = self.linkedlist.head
            # if only single node
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            # more than one element
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempNode
    """ tc: O(1) ; sc: O(1)"""

    # 4. peek
    def peek(self):
        if self.isEmpty():
            return " queue full"
        else:
            return self.linkedlist.head
    """ tc: O(1) ; sc: O(1)"""

    # delete
    def deleteQueue(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None
        return " deleted successfully"
    """ tc: O(1) ; sc: O(1)"""



# customQueue = Queue()

# # 1. enqueue
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# print(customQueue)

# # # 3. dequeue
# # customQueue.dequeue()
# # print(customQueue)

# # 4. peek
# # print(customQueue.peek())

# # delete
# print(customQueue.deleteQueue())

# 4. USING COLLECTION MODULES
# from collections import deque

# customQueue = deque(maxlen = 3)

# customQueue.append(1)
# customQueue.append(2)
# customQueue.append(3)
# # print(customQueue)
# # customQueue.append(4)
# # print(customQueue)

# # print(customQueue.popleft())
# # print(customQueue)
# print(customQueue.clear())
# print(customQueue)

# 5. USING QUEUE MODULE
# import queue as q

# customQueue = q.Queue(maxsize = 3)
# #print(customQueue.empty())  # true
# # print(customQueue.qsize())  # 0
# customQueue.put(1)
# customQueue.put(2)
# customQueue.put(3)
# #print(customQueue.qsize())  # 3
# #print(customQueue.full())   # true
# print(customQueue.get())
# print(customQueue.qsize())
# print(customQueue)

# 6. USING MULTIPROCESSING MODULE
# from multiprocessing import Queue

# customQueue = Queue(maxsize = 3)
# customQueue.put(1)
# print








