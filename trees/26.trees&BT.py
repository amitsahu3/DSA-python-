# TREE BASICS

# class TreeNode:
#     def __init__(self, data, children = []):
#         self.data = data
#         self.children = children
    
#     def __str__(self, level = 0):
#         ret = "  " * level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level + 1)
#         return ret
    
#     def addChild(self, TreeNode):
#         self.children.append(TreeNode)
    
# tree = TreeNode('Drinks', [])
# cold = TreeNode('cold', [])
# hot = TreeNode('hot', [])
# tea = TreeNode('tea', [])
# coffee = TreeNode('coffee', [])
# alc = TreeNode('alcoholic', [])
# non_alc = TreeNode('Non-alcoholic', [])
# tree.addChild(cold)
# tree.addChild(hot)
# hot.addChild(tea)
# hot.addChild(coffee)
# cold.addChild(alc)
# cold.addChild(non_alc)
# print(tree)

# # BINARY TREE USING LINKED LIST
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None

# # 1. CREATING A BINARY TREE         tc:O(1) ; sc:O(1)
# rootnode = TreeNode('drinks')
# hot = TreeNode('hot')
# cold = TreeNode('cold')
# rootnode.leftchild = hot
# rootnode.rightchild = cold
# tea = TreeNode('tea')
# coffee = TreeNode('coffee')
# alc = TreeNode('alcoholic')
# non_alc = TreeNode('non-alcoholic')
# hot.leftchild = tea
# hot.rightchild = coffee
# cold.leftchild = alc
# cold.rightchild = non_alc

# # 2. TRAVERSAL
# # 2.1 PREORDER TRAVERSAL     (ROOTNODE-->LEFTSUBTREE-->RIGHTSUBTREE)
# # def preOrderTraversal(rootnode):
# #     if not rootnode:                # tc: O(1) ; as we keep calling the function recursively ,at the end in rightchild we are gonna get rootnode,meaning we have traversed the tree and also it will be the stopping condition otherwise we may enter the infinte loop
# #         return 
# #     print(rootnode.data)            # tc:O(1)
# #     # again calling the function recursively for left and right child
# #     preOrderTraversal(rootnode.leftchild)           #tc:O(n/2)
# #     preOrderTraversal(rootnode.rightchild)          #tc:O(n/2)

# # preOrderTraversal(rootnode)
# # tc : O(n) ; sc: O(n) as recursion uses stack memory and whenever it is calling the function it remebers the memory location of the previous call

# # 2.2 INORDER TRAVERSAL      (LEFTSUBTREE-->ROOTNODE-->RIGHTSUBTREE)
# # def inOrderTraversal(rootnode):
# #     if not rootnode:
# #         return
# #     inOrderTraversal(rootnode.leftchild)
# #     print(rootnode.data)
# #     inOrderTraversal(rootnode.rightchild)
# # inOrderTraversal(rootnode)

# # tc: O(n) ; sc: O(n) as recursion

# # 2.3 POSTORDER TRAVERSAL ( LEFTSUBTREE-->RIGHTSUBTREE-->ROOTNODE)
# # def postOrderTraversal(rootnode):
# #     if not rootnode:
# #         return
# #     postOrderTraversal(rootnode.leftchild)
# #     postOrderTraversal(rootnode.rightchild) 
# #     print(rootnode.data)
# # postOrderTraversal(rootnode)

# # tc: O(n) ; sc: O(n) as recursion

# # 2.4 LEVEL ORDER TRAVERSAL 
# import QueueLinkedList as queue
# def levelOrderTraversal(rootnode):
#     if not rootnode:
#         return
#     else:
#         customQ = queue.Queue()
#         customQ.enqueue(rootnode)
#         while not(customQ.isEmpty()):
#             root = customQ.dequeue()           # tc:O(1); to hold root we need to dequeue it so it will get accessed for printing and at the same time will be removed from queue
#             print(root.value.data)
#             if (root.value.leftchild is not None):
#                 customQ.enqueue(root.value.leftchild)
#             if (root.value.rightchild is not None):
#                 customQ.enqueue(root.value.rightchild)

# # # tc:O(n) ;sc:O(n) as n elements is to be created
# # levelOrderTraversal(rootnode)

# # 3. SEARCHING IN TREE (WE'LL USE LEVEL ORDER TRAVERSAL AS IT USES QUEUE AND QUEUE PERFORMS BETTER THAN STACK)
# # def searchTree(rootnode, target):
# #     if not rootnode:
# #         return 
# #     else:
# #         customQ = queue.Queue()
# #         customQ.enqueue(rootnode)
# #         while not(customQ.isEmpty()):
# #             root = customQ.dequeue()
# #             if root.value.data == target:
# #                 return 'found'
# #             if (root.value.leftchild is not None):
# #                 customQ.enqueue(root.value.leftchild)
# #             if (root.value.rightchild is not None):
# #                 customQ.enqueue(root.value.rightchild)
# #         return 'not found'

# # # tc: O(n), sc: O(n)
# # print(searchTree(rootnode, 'tea'))

# # 4. INSERTING A NODE IN TREE
# # we'll use level order traversal if rootnode doesnot exist assign node value to rootnode else add node to that place where space is vaccant in level order traversal
# def insertNode(rootnode, nodevalue):
#     # if rootnode doesnot exists then assign nodevalue as rootnode
#     if not rootnode:
#         rootnode = nodevalue
#     else:
#         customq = queue.Queue()
#         customq.enqueue(rootnode)
#         while not (customq.isEmpty()):
#             root = customq.dequeue()
#             # if leftchild of root is empty then assign it nodevalue else just enqueue the child
#             if root.value.leftchild is None:
#                 root.value.leftchild = TreeNode(nodevalue)
#                 return 'inserted successfully'
#             else:
#                 customq.enqueue(root.value.leftchild)
            
#             # same for the right child
#             if root.value.rightchild is None:
#                 root.value.rightchild = TreeNode(nodevalue)
#                 return 'inserted successfully'
#             else:
#                 customq.enqueue(root.value.rightchild)
# #  
# # tc: O(n), sc: O(n)

# # 5. DELETE A NODE
# # find the deepest node in level order and exchange the values b/w them and delete the deepest node
# # we can't directly delete the node as other nodes might depend on that node 

# # 5.1 getting the deeepet node
# def deepestNode(rootnode):
#     if not rootnode:
#         return
#     else:
#         customQ = queue.Queue()
#         customQ.enqueue(rootnode)
#         while not(customQ.isEmpty()):
#             root = customQ.dequeue()
#             if root.value.leftchild is not None:
#                 customQ.enqueue(root.value.leftchild)
#             if root.value.rightchild is not None:
#                 customQ.enqueue(root.value.rightchild)
#         deepestnode = root.value            # after exiting the while loop it will be the root will be deepestnode
#         return deepestnode
# # 5.2 delete deepest node    
# def deleteDeepestNode(rootnode):
#     if not rootnode:
#         return
#     else:
#         customQ = queue.Queue()
#         customQ.enqueue(rootnode)
#         while not(customQ.isEmpty()):
#             root = customQ.dequeue()

#             # if currentnode/rootnode is deepestnode
#             if root.value == deepestNode(rootnode):
#                 root.value = None
#                 return
#             # checking for rightchild
#             # first: if rightchild exists or not
#             if root.value.rightchild:
#                 if root.value.rightchild is deepestNode(rootnode):
#                 # if rightchild exists and is deepestnode ;delete and return from loop
#                     root.value.rightchild = None
#                     return
#                 else:
#                 # put in the queue for traversal
#                     customQ.enqueue(root.value.rightchild)

#             # second: if leftchild exists or not
#             if root.value.leftchild:
#                  # if currentnode/rootnode leftchild is deepestnode;if it is then return from loop
#                  if root.value.leftchild is deepestNode(rootnode):
#                      root.value.leftchild = None
#                      return
#                  else:
#                      # put in the queue for traversal
#                      customQ.enqueue(root.value.leftchild)
                    
# # 5.3 delete the target node
# def deleteNode(rootnode, node):
#     if not rootnode :
#         return
#     else:
#         customq = queue.Queue()
#         customq.enqueue(rootnode)
#         while not(customq.isEmpty()):
#             root = customq.dequeue()
#             if root.value.data == node:
#                 dnode = deepestNode(rootnode)       # getting the deepest node
#                 root.value.data = dnode.data        # target node's data is changed to deepestnode
#                 deleteDeepestNode(rootnode)         # deepestnode is then deleted
#                 return ' deleted successfully'
#             if root.value.leftchild is not None:
#                 customq.enqueue(root.value.leftchild)
#             if root.value.rightchild is not None:
#                 customq.enqueue(root.value.rightchild)
#         return 'failed to delete'
                
                
# # print(deleteNode(rootnode, 'cold'))
# # tc: O(n); sc:O(n) ;sc O(n) as we are creating a customq

# # 6. DELETE ENTIRE TREE
# def deleteBT(rootnode):
#     if not rootnode:
#         return 
#     else:
#         rootnode.data = None
#         rootnode.leftchild = None
#         rootnode.rightchild = None
# # deleteBT(rootnode)
# # tc: O(1); sc:O(1)

# ----------------------------------------------------------------------------------------------------------------------
# USING PYTHON LIST
# ----------------------------------------------------------------------------------------------------------------------
# 1. CREATING A BINARY TREE ; tc:O(1), sc:O(n) 
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0      # to get last used index
        self.maxSize = size
    def printBT(self):
         return self.customList
            
    # 2. INSERTION
    def insertnode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return 'full tree'
        else:
            self.customList[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1
            return ' inserted successfully'
    # 3. SEARCH
    def searchNode(self, value):
        if self.customList == []:
            return 'empty tree'
        for item in self.customList:
            if item == value:
                return 'found'
        return 'not found'
    
    # 4. TRAVERSAL

    # 4.1 PREORDER TRAVERSAL    (ROOT-->LEFTSUBTREE-->RIGHTSUBTREE)
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    # 4.2 INORDER TRAVERSAL     (LEFTSUBTREE-->ROOTNODE-->RIGHTSUBTREE)
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)
    
    # 4.3 POSTORDER TRAVERSAL       (LEFTSUBTREE-->RIGHTSUBTREE-->ROOTNODE)
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.customList[index])

    # 4.4 LEVEL ORDER TRAVERSAL (BY LEVELS, as we insert in this oreder only)
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):  
            print(self.customList[i])  

    # 5. DELETE A NODE  
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'empty tree'
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return 'deleted successfully'
    
    # 6. DELETE ENTIRE LIST
    def deleteBT(self):
        self.customList = None
        self.lastUsedIndex = 0
        return " tree deleted"
# 1. CREATING A BINARY TREE  
newBT = BinaryTree(8)
# tc:O(1), sc:O(n)

# 2. INSERTION
newBT.insertnode('drinks')
newBT.insertnode('hot')
newBT.insertnode('cold')
newBT.insertnode('tea')
newBT.insertnode('coffee')
newBT.insertnode('alcoholic')
newBT.insertnode('non alcoholic')
# tc: O(1); sc:O(1)

# 3. SEARCH
# print(newBT.searchNode('cola'))
# tc : O(n) ; sc:o(1)
print(newBT.printBT())
print(newBT.lastUsedIndex)

# 4. TRAVESRSAL

# 4.1 preordertraversal
# newBT.preOrderTraversal(1)
#  tc: O(n) ; sc:O(n) as recursion uses stack memory

# 4.2 inordertraversal
# newBT.inOrderTraversal(1)

# 4.3 postorder traversal
# newBT.postOrderTraversal(1)

# 4.4 level order traversal
# newBT.levelOrderTraversal(3)

# 5. DELETE A NODE
# newBT.deleteNode('cold')

# 6. DELETE ENTIRE LIST
newBT.deleteBT()
print(newBT.printBT())
print(newBT.lastUsedIndex)






