# 1. CREATION
class Heap:
    def __init__(self, size):
        self.customlist = (size+1) * [None]     # as we start from index 1 to keep calculations easy 
        self.heapsize = 0
        self.maxsize = size+1       # not use 0 cell 
# tc : O(1) ; sc :O(n) as fixed size list

# 2. PEAK
def peakHeap(rootnode):
    if not rootnode:
        return 'empty heap'
    return rootnode.customlist[1]
# tc : O(1) ; sc :O(1)  accessing an element by index

# 3. SIZE OF HEAP
def sizeHeap(rootnode):
    if not rootnode:
        return 'empty heap'
    return rootnode.heapsize
# tc = sc = O(1)

# 4. TRAVERSAL

# 4.1 PREORDER TAVERSAL(ROOT-->LST-->RST)
# 4.2 INORDER TRAVERSAL(LST-->ROOT-->RST)
# 4.3 POSTORDER TRAVERSAL(LST-->RST-->ROOT)
# 4.4 LEVEL ORDER TRAVERSAL(WITH EACH LEVEL)
def levelOrderTraversal(rootnode):
    if not rootnode:
        return 
    for i in range(1, rootnode.heapsize+1):
        print(rootnode.customlist[i])
# tc : O(n) ; sc:O(1)

# 5. INSERT ELEMENT
# a) insert at the last index
# b) adjust it in accordance with the properties of BH
def heapify(rootnode, index, heaptype):      #index of node we want to make adjustments for
    # finding parentindex by index//2 as both lc and rc have same parent
    parentindex = int(index/2)
    if index <= 1:      # either empty or only one node
        return
    
    # for min heap
    if heaptype == 'min':

        # if current value is smaller than parent value then swap them
        if rootnode.customlist[index] < rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp

        # after this call heapify recursively to check if all nodes are adjusted or not
        heapify(rootnode, parentindex, heaptype )

    # for max heap
    elif heaptype == 'max':

        # opposite of min heap
        if rootnode.customlist[index] > rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
        heapify(rootnode, parentindex, heaptype)

# tc = sc = O(logn) 

def insertnode(rootnode, nodevalue, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
        return 'BH is full'
    
    # insert at the last index
    rootnode.customlist[rootnode.heapsize+1] = nodevalue
    rootnode.heapsize += 1
    # call heapify for the currentnode to check if the BH is adjusted or not
    heapify(rootnode, rootnode.heapsize, heaptype)  # heapsize has been updated to current index so using rootnode we are accessing the latest inserted value
    return 'value inserted successfully'

# tc : O(logn) sc: O(logn)

# 6. EXTRACT A NODE FROM BH
# the only element that can be extracted from heap is rootnode(index=1) other indexes can't be directly accessed (property of heap)
# extract rootnode -- > replace rootnode value with last element --> then make adjustments if needed
# if min heap swap rootnode value with leftchild recursively 
def heapifyExtract(rootnode, index, heaptype):
    # find left and rightchild for rootnode
    leftindex = index * 2
    rightindex = index*2 + 1
    swapchild = 0

    # check if rootnode has children or not
    if rootnode.heapsize < leftindex:
        return
    
    # only one node and if its leftchild(do adjustments)
    elif rootnode.heapsize == leftindex:
        if heaptype == 'min':
            if rootnode.customlist[index] > rootnode.customlist[leftindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return
        
        # for maxheap
        else:
            if rootnode.customlist[index] < rootnode.customlist[leftindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return
        
    # two children: find smallest child and swap with parents (min heap) and greatestchild for (max heap)
    else:

        # finding the smallest child for min heap
        if heaptype == 'min':
            if rootnode.customlist[leftindex] < rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            # swapping with parent node
            if rootnode.customlist[index] > rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
        
        # finding the bigger child for max heap
        else:
            if rootnode.customlist[leftindex] > rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            # swapping
            if rootnode.customlist[index] < rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp

        # call recursively for swapchild as we made adjustments for binary tree and will continue to the next node
        heapifyExtract(rootnode,swapchild, heaptype )

def extractNode(rootnode, heaptype):
    if rootnode.heapsize == 0 :
        return 
    else:
        extractedNode = rootnode.customlist[1]      # always located at location 1
        rootnode.customlist [1] = rootnode.customlist[rootnode.heapsize]     # swapping with last node
        rootnode.customlist[rootnode.heapsize] = None       # setting the last node to none
        rootnode.heapsize -= 1

        # call heapifyextract to make adjustments
        heapifyExtract(rootnode, 1, heaptype)
        return extractedNode

# tc = sc = O(logn)

# 7. DELETE ENTIRE HEAP
def deleteHeap(rootnode):
    rootnode.customlist = None
# tc = sc = O(1)
newBH = Heap(5)
insertnode(newBH, 4, 'max')
insertnode(newBH, 5, 'max')
insertnode(newBH, 2, 'max')
insertnode(newBH, 1, 'max')

# levelOrderTraversal(newBH)
# extractNode(newBH,'max')
# print('-----')
deleteHeap(newBH )
levelOrderTraversal(newBH)
