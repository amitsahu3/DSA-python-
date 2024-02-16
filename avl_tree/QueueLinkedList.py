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