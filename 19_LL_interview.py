from LINKEDLIST_19 import LinkedList
from LINKEDLIST_19 import Node

# # 1. remove duplicates
# def removedup(ll):
#    if ll.head is None:
#        return 
#    else:
#        currentNode = ll.head
#        visited = set([currentNode.value])   # sc: O(n) as temp Buffer is created ,adding first element to the set
#        while currentNode.next:
#            if currentNode.next.value in visited:    # comparing with the next element
#                currentNode.next = currentNode.next.next # if present then refer to the node after that 
#            else:
#                visited.add(currentNode.next.value)
#            return ll
#ll = linkedlist()
# ll.generate(10, 0, 99)
#print(ll)
# removedup(ll)
# """tc: O(n) ; sc: O(n) as tempbuffer is created """
# print(ll)

# # 2. find nth to last element
# def findelement(ll,n):
#     pointer1 = ll.head
#     pointer2 = ll.head
#     # moving pointer n places apart as when p2 reaches last node p1 will be at the nth position from last
#     for i in range(n):
#         if pointer2 is None:
#             return None
#         pointer2 = pointer2.next
    
#     # moving both pointers at the same pace and using p2 in while loop as we need to stop when p2 reaches last node
#     while pointer2:
#         pointer1 = pointer1.next
#         pointer2 = pointer2.next
#     return pointer1
# """tc: O(n) while loop ; sc: O(1) p1 and p2 are created only"""          
# print(findelement(ll,3))

# 3. partition a linked list around a given value 
# """logic : add lesser elements to the begining of linked list and greater elements to the end of linked list"""
# def partition(ll, value):
#     curNode = ll.head
#     ll.tail = ll.head
#     while curNode:
#         nextNode = curNode.next
#         curNode.next = None

#         # adding the lesser values to the begining of the LL
#         if curNode.value < value:
#             curNode.next = ll.head
#             ll.head = curNode
        
#         # adding at the end of linked list
#         else:
#             ll.tail.next = curNode
#             ll.tail = curNode
#         curNode = nextNode
#     # incase all elements are less than value and tail is not set to none

#     if ll.tail.next is not None:
#         ll.tail.next = None
# partition(ll,50)
# """tc : O(n) ; sc : O(1) as two nodes are created next and temp"""

# # 4. sum linked list
# def sumlist(llA, llB):
#     n1 = llA.head
#     n2 = llB.head
#     carry = 0   # to store carry
#     llC = linkedlist()  # to store sum
#     while n1 or n2 :
#         result = carry
#         if n1:
#             result += n1.value
#             n1 = n1.next
#         if n2:
#             result += n2.value
#             n2 = n2.next
#         llC.add(int(result % 10))
#         carry = result /10
#     print(llC)

# llA = linkedlist()
# llA.add(7)
# llA.add(1)
# llA.add(6)
# llB = linkedlist()
# llB.add(5)
# llB.add(9)
# llB.add(2)
# sumlist(llA, llB)
# """tc : O(n) ; sc : O(n) as creating temporary ll and adding the values to it"""

# # 5. intersection
# def intersection(llA, llB):
#     # checking if they point to the same tail or not
#     if llA.tail is not llB.tail:
#         return " not intersecting"
#     else:
#         lenA = len(llA)
#         lenB = len(llB)

#         # identifying longer and shorte lists
#         shorter = llA if lenA < lenB else llB
#         longer = llB if lenA < lenB else llA
#         diff = len(longer) - len(shorter)

#         # identifying first node of longer and shorter lls
#         longerNode = longer.head
#         shorterNode = shorter.head

#         # we will traverse to the difference of the nodes first then start traversing both at the same time
#         for i in range(diff):
#             longerNode = longer.next
        
#         # while loop to start traversing both at the same time till we reach the intersection
#         while shorterNode is not longerNode:    # loop will run till shorterNode and longerNode are same 
#             shorterNode = shorterNode.next
#             longerNode = longerNode.next
#         return longerNode

# # helper addition method
# def addsameNode(llA, llB, value):
#     tempNode = Node(value)
#     llA.tail.next = tempNode
#     llA.tail = tempNode
#     llB.tail.next = tempNode
#     llB.tail = tempNode


# llA = linkedlist()
# llB = linkedlist()
# llA.add(7)
# llA.add(1)
# llA.add(6)
# llB.add(5)
# llB.add(9)
# llB.add(2)   
# addsameNode(llA, llB, 99) 

# print(intersection(llA, llB))
# """ tc : O(A+B) based on number of nodes in A and B ; sc : O(1)"""

# ll = LinkedList()
# ll.add(11)
# ll.add(3) 
# ll.add(9)
# ll.add(10)
# ll.add(15)
# print(ll)

# 1. REMOVE DUPLICATES
def removeduplicates(ll):
    if ll.head is None:
        return ' empty list'
    currentnode = ll.head
    # prevnode = None
    while currentnode:
        runner = currentnode
        while runner.next:
            if runner.next.value == currentnode.value:
                runner.next = runner.next.next
                ll.length -= 1
            else:
                runner = runner.next
        # prevnode = currentnode
        currentnode = currentnode.next
    # customll.tail = prevnode
    # print(ll.head, ll.tail, ll.length)
    return ll

# print(removeduplicates(ll))

# 2. Nth ELEMENT FROM LAST
def returnelement(ll, n):
    index = ll.length - n
    idx = 0
    currentnode = ll.head
    while idx < index -2 :
        currentnode = currentnode.next
        id += 1
    return currentnode.value

# print(returnelement(ll, 4))

# 3. PARTITION 
def partition(ll, x):
    if ll.head is None:
        return 'empty list'
    ll1 = LinkedList()
    ll1.add(x)
    currentnode = ll.head
    while currentnode:
        if currentnode.value == x:
            currentnode = currentnode.next
        if currentnode.value < x:
            newnode = Node(currentnode.value)
            newnode.next = ll1.head
            ll1.head = newnode
            currentnode = currentnode.next
        else:
            ll1.add(currentnode.value)      
            currentnode = currentnode.next
    return ll1
# print(partition(ll, 10))

# 4. SUM LINKED LIST
# llA = LinkedList()
# llA.add(7)
# llA.add(1) 
# llA.add(6)        
# llB = LinkedList()
# llB.add(5)
# llB.add(9) 
# llB.add(2)   

def sumll(llA, llB):
    num1 = [str(node.value) for node in llA]
    num2 = [str(node.value )for node in llB]
    final_num1 = []
    final_num2 = []
    for i in range(len(num1)):
        numA =  num1.pop()
        final_num1.append(numA) 
    for i in range(len(num2)):
        numB =  num2.pop()
        final_num2.append(numB) 
    n1 = ''.join(final_num1)
    n2 = ''.join(final_num2)
    finalsum = int(n1)+int(n2)
    print(final_num1, final_num2)
    print(n1, n2)
    print(finalsum)
    final_sum_list = list(str(finalsum))
    print(final_sum_list)
    reversed_list = []
    result = LinkedList()
    for _ in range(len(final_sum_list)):
        digit = final_sum_list.pop()
        newnode = Node(int(digit))
        result.add(newnode)
    return result

# print(sumll(llA, llB))

# 5. INTERSECTION
llA = LinkedList()
llA.add(7)
llA.add(1) 
llA.add(6)        
llB = LinkedList()
llB.add(5)
llB.add(9) 
llB.add(2)        

 
