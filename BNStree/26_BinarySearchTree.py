# 1. CREATE BST
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
    
# 2. INSERT NODE
def insertNode(rootnode, nodevalue):
    # if rootnode doesnot exist:
    if rootnode.data is None:
        rootnode.data = nodevalue
    
    # if rootnode exists , then compare left and right subtree
    elif nodevalue <= rootnode.data:

        # if leftchild doesnot exists
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(nodevalue)
        
        # else call recursively with leftchild
        else:
            insertNode(rootnode.leftchild, nodevalue)
    
    # compare to rightchild
    else:
        # if rightchild doesnot exists
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(nodevalue)
        
        # else call recursively with leftchild
        else:
            insertNode(rootnode.rightchild, nodevalue)
        
    return 'inserted successfully'


# 1. CREATE BST
newBST = BSTNode(None)
# tc :O(1) ; sc:O(1)

# 2. INSERT NODE
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)


# tc:O(logn) ; sc:O(logn) ; we are recursively traversing one subtree only, i.e. dividing at each step

# 3. TRAVERSAL 

# 3.1 PREORDER TRAVERSAL (ROOT-->LEFTSUBTREE-->RIGHTSUBTREE)
def preOrderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preOrderTraversal(rootnode.leftchild)
    preOrderTraversal(rootnode.rightchild)

# tc:O(n), sc:O(n)

# 3.2 INOREDER TRAVERSAL    (LEFTSUBTREE-->ROOTNODE-->RIGHTSUBTREE)
def inOrderTraversal(rootnode):
    if not rootnode:
        return 
    inOrderTraversal(rootnode.leftchild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightchild)

# tc:O(n), sc:O(n)

# 3.3 POSTORDER TRAVERSAL   (LEFTSUBTREE-->RIGHTSUBTREE-->ROOTNODE)
def postOrderTraversal(rootnode):
    if not rootnode:
        return
    postOrderTraversal(rootnode.leftchild)
    postOrderTraversal(rootnode.rightchild)
    print(rootnode.data)

# tc:O(n), sc:O(n)

# 3.4 LEVEL ORDER TRAVERSAL
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

# tc:O(n), sc:O(n)

# 4. SEARCH A NODE
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


# 5. DELETE A NODE

# finding the min node(for finding the successor) which is always in the left subtree(often with rightchild of rootnode)
def minNode(BSTnode):
    current = BSTnode
    while (current.leftchild is not None):
        current = current.leftchild
    return current

# we will use rootnode to delete
def deleteNode(rootnode, nodevalue):
    # if rootnode is none then return rootnode itself
    
    if rootnode is None:
        return None
    
    # if rootnode.data < value, then call recursively the left child
    if  nodevalue < rootnode.data :
        rootnode.leftchild = deleteNode(rootnode.leftchild, nodevalue)
        

    # if rootnode.data > value,then call recursively the right child
    elif nodevalue > rootnode.data :
        rootnode.rightchild = deleteNode(rootnode.rightchild, nodevalue)

    # if rootnode.data = value
    else:
        # after traversing the tree we reached to the node to be deleted(rootnode)

        # 1. node to be deleted contains one child
        # 1.1 for leftchild (if leftchild is empty then use temp to store and return rightchild after deleting the rootnode)
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        
        # 1.2 for rightchild (if rightchild is empty then use temp to store and return leftchild after deleting the rootnode)
        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        
        # 2. node to be deleted has two childs
        tempnode = minNode(rootnode.rightchild)     # find successor
        print(f'rn:{rootnode.data}')
        print(f'tempnode:{tempnode.data}')
        deletedData = rootnode.data
        print(deletedData)
        rootnode.data = tempnode.data                         # exchange values b/w successor and rootnode
        print(rootnode.data)
        minNode(rootnode.rightchild).data = deletedData         # data has changed but the node still remains same 
        rootnode.rightchild = deleteNode(rootnode.rightchild, nodevalue)        # delete the successor node, and attach the nodes with root(as we find successor in the rightsubtree of rootnode)
        print(rootnode.rightchild)
        # print(f'rn.rc:{rootnode.rightchild.data}')
        # to delete the swapped value we recursively find the node and simply delete it in the rightsubtree
    return rootnode
# tc: O(logn) ; sc:O(logn)
# deleteNode(newBST, 30)

# 6. DELETE THE BINARY SEARCH TREE
def deleteBST(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return ' BST deleted'

print(deleteBST(newBST))
levelOrderTraversal(newBST)