# import QueueLinkedList as queue
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None
    
# newBT = TreeNode('drinks')
# leftchild = TreeNode('hot')
# tea = TreeNode('tea')
# coffee = TreeNode('coffee')
# leftchild.leftchild = tea
# leftchild.rightchild = coffee
# rightchild = TreeNode('cold')
# newBT.leftchild = leftchild
# newBT.rightchild = rightchild



# #1 TRAVERSAL

# #1. PREORDER TRAVERSAL(visiting all the left subtrees first0)
# def PreOrderTraversal(rootNode):
#     if not rootNode:        # tc: O(1) ; as we keep calling the function recursively ,at the end in rightchild we are gonna get rootnode,meaning we have traversed the tree and also it will be the stopping condition otherwise we may enter the infinte loop
#         return
#     print(rootNode.data)       # tc:O(1)

#     # again calling the function recursively for left and right child
#     PreOrderTraversal(rootNode.leftchild)   #tc:O(n/2)
#     PreOrderTraversal(rootNode.rightchild)  #tc:O(n/2)

# # tc : O(n) ; sc: O(n) as recursion uses stack memory and whenever it is calling the function it remebers the memory location of the previous call

# #2. INEORDER TRAVERSAL(leftsubtree-->rootnode-->rightsubtree)
# def InOrderTreaversal(rootNode):
#     if not rootNode:
#         return
#     InOrderTreaversal(rootNode.leftchild)
#     print(rootNode.data)
#     InOrderTreaversal(rootNode.rightchild)
# # tc: O(n) ; sc: O(n) as recursion

# #3. POST ORDER TRAVERSAL (leftsubtree--> rightsubtree-->rootnode)
# def PostOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     PostOrderTraversal(rootNode.leftchild)
#     PostOrderTraversal(rootNode.rightchild)
#     print(rootNode.data)
# # tc: O(n) ; sc: O(n) as recursion 

# #3. LEVEL ORDER TRAVERSAL(level by level)
# def LevelOrderTraversal(rootNode):
#     if not rootNode:        # tc:O(1)
#         return
#     else:
#         # create a custom queue
#         customQ = queue.Queue()     # tc:O(1)
#         customQ.enqueue(rootNode)   # tc:O(1)
#         while not (customQ.isEmpty()):      # tc:O(n) ; while custom queue is not empty loop will run
#             root = customQ.dequeue()        # tc:O(1); to hold root we need to dequeue it so it will get accessed for printing and at the same time will be removed from queue
#             print(root.value.data)
#             if (root.value.leftchild is not None): # tc:O(1)
#                 customQ.enqueue(root.value.leftchild)
#             if (root.value.rightchild is not None): # tc:O(1)
#                 customQ.enqueue(root.value.rightchild)
# # tc:O(n) ;sc:O(n) as n elements is to be created

# #2. SEARCHING
# def seachBT(rootNode,nodeValue):
#         if not rootNode:        # tc:O(1)
#             return
#         else:
#         # create a custom queue
#             customQ = queue.Queue()     # tc:O(1)
#             customQ.enqueue(rootNode)   # tc:O(1)
#         while not (customQ.isEmpty()):      # tc:O(n) ; while custom queue is not empty loop will run
#             root = customQ.dequeue()        # tc:O(1); to hold root we need to dequeue it so it will get accessed for printing and at the same time will be removed from queue
#             if root.value.data == nodeValue:
#                 return " success"
            
#             if (root.value.leftchild is not None): # tc:O(1)
#                 customQ.enqueue(root.value.leftchild)

#             if (root.value.rightchild is not None): # tc:O(1)
#                 customQ.enqueue(root.value.rightchild)
#         return 'not found'
# # tc:O(n) ; sc:O(n) as n elements is to be created

# #3. INSERTION
# def insertNodeBT(rootNode, nodevalue):
#     # if rootnode doesnot exists then assign nodevalue as rootnode
#     if not rootNode:
#         rootNode = nodevalue
#     else:
#         customQ = queue.Queue()
#         customQ.enqueue(rootNode)
#         while not(customQ.isEmpty()):
#             root = customQ.dequeue()

#             # if leftchild of root is empty then assign it nodevalue else just enqueu the child
#             if (root.value.leftchild is not None):        # root.value.left is location of leftchild not data of left child
#                 customQ.enqueue(root.value.leftchild)
#             else: 
#                 root.value.leftchild = nodevalue
#                 return ' insertion success'
#             # if rightchild of root is empty then assign it nodevalue else just enqueu the child
#             if (root.value.rightchild is not None):
#                 customQ.enqueue(root.value.rightchild)
#             else:
#                 root.value.leftchild = nodevalue
#                 return 'insertion success'
#         return ' can not insert'
# # tc:O(n) ; sc:O(n) as n elements is to be created
# # print(insertNodeBT(newBT,'cola'))

# # #4. DELETTION

# #4.1. getting the deepest node
# def getDeepestNode(rootnode):
#     if not rootnode:
#         return
#     else:
#         customQ = queue.Queue()
#         customQ.enqueue(rootnode)
#         while not (customQ.isEmpty()):
#             root = customQ.dequeue()
#             if root.value.leftchild is not None:
#                 customQ.enqueue(root.value.leftchild)
#             if root.value.rightchild is not None:
#                 customQ.enqueue(root.value.rightchild)
#         # at the end root will have the value of the last node
#         deepestnode = root.value
#         return deepestnode
# # tc:O(n) ; sc:O(n) as taversal only
# # deepestnode = getDeepestNode(newBT)
# # print(deepestnode.data)

# #4.2. delete deepest nodes
# def deleteDeepestNode(rootnode, dnode):
#     if not rootnode:
#         return
#     else:
#         customQ = queue.Queue()
#         customQ.enqueue(rootnode)
#         while not (customQ.isEmpty()):
#             root = customQ.dequeue()

#             # if currentnode/rootnode is deepestnode
#             if root.value is dnode:
#                 root.value = None
#                 return 

#             # checking for rightchild
#             # first: if rightchild exists or not
#             if root.value.rightchild:
#                 # if currentnode/rootnode rightchild is deepestnode ;if it is then return from loop
#                 if root.value.rightchild is dnode:
#                     root.value.rightchild = None
#                     return 
#                 else:
#                     # put in the queue for traversal
#                     customQ.enqueue(root.value.rightchild)

#             # second: if leftchild exists or not
#             if root.value.leftchild:
#                 # if currentnode/rootnode leftchild is deepestnode;if it is then return from loop
#                 if root.value.leftchild is dnode:
#                     root.value.leftchild = None
#                     return
#                 else:
#                     # put in the queue for traversal
#                     customQ.enqueue(root.value.leftchild)

# # newnode = getDeepestNode(newBT)
# # print(newnode)
# # deleteDeepestNode(newBT, newnode)
# # LevelOrderTraversal(newBT)

# #5. DELETE A GIVEN NODE
# def deleteNodeBT(rootnode, node):
#     if not rootnode:
#         return " the BT doesnot exist"
#     else:
#         customQ = queue.Queue()
#         customQ.enqueue(rootnode)
#         while not (customQ.isEmpty()):
#             root = customQ.dequeue()

#             # if root is dnode then swap it with the deepest node and delete the deepest node
#             if root.value.data == node:
#                 dnode = getDeepestNode(rootnode)
#                 root.value.data = dnode.data        # setting the current node with the value of deepest node 
#                 deleteDeepestNode(rootnode, dnode)  # deleting the deepest node
#                 return 'deleted successfully'
            
#             # same for left and right children
#             if root.value.leftchild is not None:
#                 customQ.enqueue(root.value.leftchild)
#             if root.value.rightchild is not None:
#                 customQ.enqueue(root.value.rightchild)
#         return " failed to delete"
# # tc:O(n) ; sc:O(n) as n elements is to be created and enqueue in customQ
# # print(deleteNodeBT(newBT, 'hot'))
# # LevelOrderTraversal(newBT)

# #5. DELETE BINARY TREE

# def deleteBT(rootNode):
#     rootNode.data = None
#     rootNode.leftchild = None
#     rootNode.rightchild = None
#     return 'deleted successfully'
# print(deleteBT(newBT))
# LevelOrderTraversal(newBT) 
#--------------------------------------------------------------------------------------------------------------------------------
# USING PYTHON LIST
#----------------------------------------------------------------------------------------------------------------------------------
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.LastUsedIndex = 0      # to get last index used
        self.maxSize = size

    #1. INSERTION (we insert nodes in level order traversal)
    def insertNode(self, value):
        if self.LastUsedIndex +1 == self.maxSize:       # if full
            return " tree full"
        self.customList[self.LastUsedIndex+1] = value   # value at next index
        self.LastUsedIndex += 1     # increase lastusedindex to the last object location 
        return ' inserted successfully'
# tc:O(1); sc:O(1)

    #2. SEARCHING
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "success"
        return " not found"
#tc: O(n) as traversing the list ; sc:O(1) as one value at a time is compared 
    
    #2. TRAVERSAL

#2.1 PREORDER TRAVERSAL (ROOT->LEFT SUBTREE->RIGHT SUBTREE)
    def preOrderTraversal(self,index):  # as we start from 1 not 0 index hence index is given
        
        # stopping conditon, if all elements have been traversed(index = maxsize-1)
            if index > self.LastUsedIndex:
                  return
        
            print(self.customList[index])   # printig rootnode
            # leftsubtree
            self.preOrderTraversal(index*2)
            # print(index)

            # rightsubtree
            self.preOrderTraversal(index*2+1) 
            #print(index)
             
#2.2 INORDER TRAVERSAL (LEFT SUBTREE->ROOTNODE->RIGHT SUBTREE)
    def inOrderTraversal(self, index):
        if index > self.LastUsedIndex:
            return
        
        # left subtree
        self.inOrderTraversal(index*2)
        #rootnode
        print(self.customList[index])
        #right subtree
        self.inOrderTraversal(index*2+1)

#2.3 INORDER TRAVERSAL (LEFT SUBTREE->RIGHT SUBTREE->ROOTNODE)
    def postOrderTraversal(self,index):
        if index > self.LastUsedIndex:
            return
        # left subtree
        self.postOrderTraversal(index*2)
        #right subtree
        self.postOrderTraversal(index*2+1) 
        #rootnode
        print(self.customList[index])
# tc: O(n); sc:O(n)
#2.4 LEVELORDER TRAVERSAL (LEVEL BY LEVEL)
    def levelOrderTraversal(self,index):
        for i in range(index, self.LastUsedIndex+1):
            print(self.customList[i])
# tc:O(n) ; sc:O(n)

#3. DELETE A NODE  (FIND DEEPEST NODE AND REPLACE THE VALUE OF THE NODE TO BE DELETED BY THE DEEPEST NODE )
    def deleteNode(self,value):
        if self.LastUsedIndex == 0:
            return " empty list"
        for i in range(1, self.LastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.LastUsedIndex]
                self.customList[self.LastUsedIndex] = None
                self.LastUsedIndex -= 1
                return " deleted successfully"

#4. DELETE ENTIRE LIST
    def deleteBT(self):
        self.customList = None
        self.LastUsedIndex = 0
        return " tree deleted"

newBT = BinaryTree(8)
newBT.insertNode('drinks')
newBT.insertNode('hot')
newBT.insertNode('cold')
newBT.insertNode('tea')
newBT.insertNode('coffee')
newBT.deleteNode('hot')
print(newBT.deleteBT())






