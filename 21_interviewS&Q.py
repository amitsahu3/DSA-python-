# 1. THREE IN ONE
# class Stack:
#     def __init__(self, stacksize):
#         self.n = 3
#         self.customlist = [0]*(stacksize*self.n)       # single list comprised of three list
#         self.sizes = [0] * self.n                       # list to store sizes of diff stacks
#         self.stacksize = stacksize
#     def isfull(self, stackNum):
#         if self.sizes[stackNum] == self.stacksize:          
#             return True
#         else:
#             return False
    
#     def isempty(self, stacknum):
#         if self.sizes[stacknum] == 0:
#             return True
#         else:
#             return False
    
#     def indexOftop(self, stacknum):     # to get index of top elements according to stack num
#         offset = stacknum * self.stacksize 
#         return offset + self.sizes[stacknum]-1
    
#     def push(self, stacknum, value):
#         if self.isfull(stacknum):
#             return f'stack {stacknum} is full'
#         else:
#             self.sizes[stacknum] += 1
#             self.customlist[self.indexOftop(stacknum)] = value
#             return ' pushed successfully'
        
#     def pop(self, stacknum):
#         if self.isempty(stacknum):
#             return f'stack {stacknum} is empty'
#         else:
#             poppenode = self.customlist[self.indexOftop(stacknum)]
#             self.customlist[self.indexOftop(stacknum)] = 0
#             self.sizes[stacknum] -= 1
#             return poppenode
    
#     def peek(self, stacknum):
#         if self.isempty(stacknum):
#             return 'empty stack'
#         else:
#             return self.customlist[self.indexOftop(stacknum)]
# stack = Stack(6)

# print(stack.push(0, 12))
# print(stack.push(0, 14))
# print(stack.push(1, 90))
# print(stack.push(1, 80))
# print(stack.push(2, 37))
# print(stack.push(2, 34))
# print(stack.pop(2))

# 2. stack min
# class Node:
#     def __init__(self, value = None):
#         self.value = value
#         self.next = None
    
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def __iter__(self):
#         currentnode = self.head
#         while currentnode:
#             yield currentnode
#             currentnode = currentnode.next

# class Stack:
#     def __init__(self):
#         self.ll = LinkedList()
#         self.minNode = float('inf')
#     def __str__(self):
#         values = [str(x.value) for x in self.ll]
#         return '\n'.join(values)
#     def isempty(self):
#         if self.ll.head is None:
#             return True
#         else:
#             return False

#     def push(self, value):
#         newnode = Node(value)
#         if self.isempty() :
#             self.ll.head = newnode
#             self.ll.tail = newnode
#         else:
#             newnode.next = self.ll.head
#             self.ll.head = newnode
#         if value < self.minNode:
#             self.minNode = value
#         else:
#             self.minNode = self.minNode
#         return f'minimum is: {self.minNode}'


        
#     def pop(self):
#         if self.isempty():
#             return 'empty stack'
#         else:
#             poppednode = self.ll.head
#             secondnode = poppednode.next
#             self.ll.head = secondnode
#             poppednode.next = None
#             return poppednode.value
    
# customstack =  Stack()
# print(customstack.push(1))
# print(customstack.push(2))
# print(customstack.push(10))
# print(customstack.push(-1))
# customstack.pop()
# customstack.pop()
# customstack.pop()
# # customstack.pop()
# print(customstack)

# 3. stack of stacks
# class PlateOfStacks():
#     def __init__(self, capacity):
#         self.capacity = capacity         # capacity of each stack
#         self.stacks = []            # stack of stacks[[], [], []]
#     def __str__(self):
#         return str(self.stacks)
    
#     def push(self, item):
#         if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
#             self.stacks[-1].append(item)
#         else:
#             self.stacks.append([item])

#     def pop(self):
#          # if empty stack in stacks
#          while len(self.stacks) and len(self.stacks[-1]) == 0 :
#             self.stacks.pop()
        
#         # if stacks is empty
#          if len(self.stacks) == 0:
#             return None
         
#          # pop from last stack
#          else:
#                 return self.stacks[-1].pop()
#     def pop_at(self, stacknum):
#         if len(self.stacks[stacknum]) > 0:
#             return self.stacks[stacknum].pop()
#         else:
#             return None
# customstack = PlateOfStacks(3)
# customstack.push(1)
# customstack.push(2)
# customstack.push(3)
# customstack.push(4)
# customstack.push(1)
# customstack.push(2)
# customstack.push(3)
# customstack.push(4)
# customstack.push(4)
# print(customstack)
# customstack.pop_at(-1)
# print(customstack)

# 4. Queue via Stacks
# class Stack:
#     def __init__(self):
#         self.list = []
    
#     def __str__(self):
#         values = self.list.reverse()      # to print the stack in LIFO manner
#         values = [str(x) for x in self.list]      # converting them into string
#         return '\n'.join(values)
#     def __len__(self):
#         return len(self.list)
    
#     def push(self, value):
#         self.list.append(value)
#     def pop(self):
#         if self.list == []:
#             return 'empty stack'
#         else:
#             return self.list.pop()
#     def deletestack(self):
#         self.list = []
# class Queue:
#     def __init__(self):
#         self.instack = Stack()
#         self.outstack = Stack()
#     def enqueue(self, value):
#         self.instack.push(value)
#     def dequeue(self):
#         while len(self.instack):
#             self.outstack.push(self.instack.pop())
#         result = self.outstack.pop()
#         while len(self.outstack):
#             self.instack.push(self.outstack.pop())
#         return result


# customQ = Queue()
# customQ.enqueue(1)
# customQ.enqueue(2)
# customQ.enqueue(3)
# customQ.enqueue(4)
# customQ.enqueue(5)
# customQ.enqueue(6)
# print(customQ.dequeue())

# 5 animal shelter 
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curnode = self.head
        while curnode:
            yield curnode
            curnode = curnode.next
        
class Queue:
    def __init__(self):
        self.ll = LinkedList()
    """tc ; O(1) ; sc: O(1)"""

    def __str__(self):
        values = [str(x.value) for x in self.ll]
        return ' '.join(values)
    def enqueue(self, value):
        newnode = Node(value)
        if self.ll.head is None:
            self.ll.head = self.ll.tail = newnode
        else:
            self.ll.tail.next = newnode
            self.ll.tail = newnode
    def dequeue(self, category):
        if self.ll.head is None:
            return 'empty queue'
        else:
            if category == 'na':
                poppednode = self.ll.head
                secondnode = poppednode.next
                self.ll.head = secondnode
                poppednode.next = None
                return poppednode
            else:
                currnode = self.ll.head
                prevnode = currnode
                while currnode:
                    currnode = currnode.next
                    
                    if currnode.value == category:
                        prevnode.next = currnode.next
                        poppednode = currnode
                        currnode = currnode.next
                        return poppednode
                    prevnode = prevnode.next
customQ = Queue()
customQ.enqueue('c')
customQ.enqueue('c')
customQ.enqueue('d')
customQ.enqueue('c')
customQ.enqueue('d')                
customQ.enqueue('c')
customQ.enqueue('c')
print(customQ)
print(customQ.dequeue('d').value )        
print(customQ.dequeue('c').value )  
print(customQ.dequeue('c').value )       
print(customQ)
 