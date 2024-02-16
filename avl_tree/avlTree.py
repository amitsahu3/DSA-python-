class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1

# 1. TRAVERSAL
# 1.1 PREORDER TRAVERSAL        (ROOT-->LEFTSUBTREE-->RIGHTSUBTREE)
def preOrderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preOrderTraversal(rootnode.leftchild)
    preOrderTraversal(rootnode.rightchild)

# 1.2 INOREDER TRAVERSAL    (LEFTSUBTREE-->ROOTNODE-->RIGHTSUBTREE)
def inOrderTraversal(rootnode):
    if not rootnode:
        return 
    inOrderTraversal(rootnode.leftchild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightchild)

# 1.3 POSTORDER TRAVERSAL   (LEFTSUBTREE-->RIGHTSUBTREE-->ROOTNODE)
def postOrderTraversal(rootnode):
    if not rootnode:
        return
    postOrderTraversal(rootnode.leftchild)
    postOrderTraversal(rootnode.rightchild)
    print(rootnode.data)

# 1.4 LEVEL ORDER TRAVERSAL
import QueueLinkedList as queue
def levelOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootnode)
        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            print(root.value.data)

            # now move to left and right subtree/child
            if root.value.leftchild is not None:
                customQ.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQ.enqueue(root.value.rightchild)
# 2. SEARCH A NODE
def searchNode(rootnode, nodevalue):
    # if not rootnode:
    #     return
    # else:
        print(rootnode.data)
        if rootnode.data == nodevalue:
            return 'found'

        # searching in the left subtree if nodevalue <= rootnode
        elif nodevalue < rootnode.data:
            if rootnode.leftchild.data == nodevalue:
                return 'found'
            else:
                return searchNode(rootnode.leftchild, nodevalue)
        # searching in the rightt subtree if nodevalue > rootnode
        else:
            if rootnode.rightchild.data == nodevalue:
                return 'found'
            else:
                return searchNode(rootnode.rightchild, nodevalue)
        
# tc:O(logn); sc:O(logn) as the tree is divided into two subtree     

# 3. INSERTION 
# after every node insertion we check if tree is balanced or not
# helper functions

# 3.1 getHeight() : to get height of nodes
def getHeight(rootnode):

    # if not rootnode or is none then return 0
    if not rootnode:        
        return 0
    
    # else return height of the node passed as rootnode
    return rootnode.height  

# 3.2 right rotate
def rightRotate(disbalancedNode):

    # as LL condition so need to update leftchild
    newRoot = disbalancedNode.leftchild     
    disbalancedNode.leftchild = disbalancedNode.leftchild.rightchild
    newRoot.rightchild = disbalancedNode
    # updating the height of disbalanced node and then rootnode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftchild), getHeight(disbalancedNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild), getHeight(newRoot.rightchild))
    #print(disbalancedNode.height)
    #print(newRoot.height)
    return newRoot

# tc:O(1) ; sc:O(1)
# 3.3 leftrotate
def leftRotate(disbalancednode):
    newRoot = disbalancednode.rightchild
    # print(f'newroot:{newRoot.data}')
    # print(f"newroot.rc.data:{newRoot.rightchild.data}")
    disbalancednode.rightchild = disbalancednode.rightchild.leftchild
    # print(f'disbalancednode.rc:{disbalancednode.rightchild}')
    newRoot.leftchild = disbalancednode
    # print(f'newroot.leftchild:{newRoot.leftchild.data}')
    disbalancednode.height = 1 + max(getHeight(disbalancednode.leftchild), getHeight(disbalancednode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild), getHeight(newRoot.rightchild))
    # print(f'disbalancedheigt:{disbalancednode.height}')
    # print(f'newroot.height:{newRoot.height}')
    return newRoot

# tc:O(1) ; sc:O(1)

# 3.4 getBalance : to check if AVL tree is Balanced or not\
def getBalance(rootnode):
    if not rootnode:        
        return 0
    #print(getHeight(rootnode.leftchild) - getHeight(rootnode.rightchild))
    return getHeight(rootnode.leftchild) - getHeight(rootnode.rightchild)

# tc:O(1) ; sc:O(1)    

# INSERT NODE
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)       # if rootnode is none; return with a new node
    elif nodeValue < rootNode.data:
        rootNode.leftchild = insertNode(rootNode.leftchild, nodeValue)
    else:
        rootNode.rightchild = insertNode(rootNode.rightchild, nodeValue)

    # updating the height of rootnode then checking the balance after adding node at each recursive call  back
    rootNode.height = 1 + max(getHeight(rootNode.leftchild), getHeight(rootNode.rightchild))
    balance = getBalance(rootNode)
    # print(f'rn.height:{rootNode.height}')
    # print(f'balance:{balance}')

    # left left : then right rotate
    if balance > 1 and nodeValue < rootNode.leftchild.data:
        return rightRotate(rootNode)
    
    # left right : leftrotate rootnode.leftchild , then right rotate
    if balance > 1 and nodeValue > rootNode.leftchild.data:
         # then leftrotate rootnode lC
        rootNode.leftchild = leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)

    # right right : then left rotate
    if balance < -1 and nodeValue > rootNode.rightchild.data : 
        return leftRotate(rootNode)
    
    # right left : rightrotate rootnode.leftchild , then left rotate
    if balance < -1 and nodeValue < rootNode.rightchild.data:
        rootNode.rightchild = rightRotate(rootNode.rightchild)
        return leftRotate(rootNode)
    # print(rootNode.data)
    return rootNode
# tc: O(logn) ; sc: O(logn)

# 4. DELETE A NODE

# helper function 
# getMinValueNode : to get successor when we delete node having two children
def getMinValueNode(rootnode):
    if rootnode is None or rootnode.leftchild is None:
        return rootnode
    return getMinValueNode(rootnode.leftchild)

def deleteNode(rootnode, nodevalue):
    # CASE 1. ROOTNODE IS NONE
    # if rootnode is none; return rootnode
    if not rootnode:
        return rootnode
    
    # CASE 2. ROTATION IS NOT REQUIRED
    # if nodevalue < rootnode
    elif nodevalue < rootnode.data:
        rootnode.leftchild = deleteNode(rootnode.leftchild, nodevalue)

    # if nodevalue > rootnode
    elif nodevalue > rootnode.data:
        rootnode.rightchild = deleteNode(rootnode.rightchild, nodevalue)

    # if rootnode.data =  nodevalue
    else:

        # single leaf nodes
        # if rootnode.lc is none
        if rootnode.leftchild is None:
            temp = rootnode.rightchild      # store rightchild in temp
            rootnode = None
            return temp         # it will be the right/leftchild of parentnode of the deleted node

        # if rootnode.rc is none
        elif rootnode.rightchild is None:
            temp = rootnode.lefttchild      # store lefttchild in temp
            rootnode = None
            return temp 
        
        # two leaf nodes(find successor)
        temp = getMinValueNode(rootnode.rightchild)         # successor is in rootnode's rightsubtree
        rootnode.data = temp.data

        # call delete method recursively for right child inorder to delete the successor
        rootnode.rightchild = deleteNode(rootnode.rightchild, temp.data)

    # CASE 3. ROTATION IS REQUIRED
    # find balance
    rootnode.height = 1 + max(getHeight(rootnode.leftchild), getHeight(rootnode.rightchild))
    balance = getBalance(rootnode)

    # 1. LL: rightrotate
    if balance > 1 and getBalance(rootnode.leftchild) >= 0:
        return rightRotate(rootnode)
    
    # 2. RR: leftrotate
    if balance < -1 and getBalance(rootnode.rightchild) <= 0:
        return leftRotate(rootnode)
    
    # 3. LR: leftrotate rootnode.lc , rightrotate rootnode
    if balance > 1 and getBalance(rootnode.leftchild) <= 0:
        rootnode.leftchild = leftRotate(rootnode.leftchild)
        return rightRotate(rootnode)
    
    # 4. RL: rightrotate rootnode.rc, leftrotate rootnode
    if balance < -1 and getBalance(rootnode.rightchild) >= 0:
        rootnode.rightchild = rightRotate(rootnode.rightchild)
        return leftRotate(rootnode)

    return rootnode
# tc: O(logn) ; sc: O(logn)

# 5. DELETE ENTIRE AVL TREE
def deleteAVLTree(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return 'AVL tree deleted '
    
newAVL = AVLNode(5)  
newAVL = insertNode(newAVL, 10)     # taking newAVL every time as rootnode(newAVL initially) changes after rotation
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = insertNode(newAVL, 25)
newAVL = insertNode(newAVL, 30)
newAVL = insertNode(newAVL, 35)
newAVL = insertNode(newAVL, 40)
# print("---")
deleteAVLTree(newAVL)

levelOrderTraversal(newAVL)

