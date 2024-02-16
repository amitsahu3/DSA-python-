# 1. CREATION 
class TrieNode:
    def __init__(self):
        self.children = {}      # using dict as we need to create links between children and their children
        self.endOfString = False       # blank node and endOfString is false

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    # 2. INSERT STRING
    def insertString(self, word):
        # find current node and use that to loop through the word passed and if the character is present or not 
        current = self.root
        for i in word:
            ch = i

            # check if this character ch exist in children or not by using get
            # if exists: then set current node to this node, if not create a new node an update children to this node 
            node = current.children.get(ch)     # it will return None if a node doesnot exist and if it exist it will return that node
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})    # update current's children to this new node
            current = node
        current.endOfString = True
        print('inserted successfully')
    
    # 3. SEARCH NODE
    def searchNode(self, word):
        currentnode = self.root
        for i in word:

            # creating new node
            node = currentnode.children.get(i)
            if node == None:
                return False
            
            # if exists then currentnode = node
            currentnode = node
        
        # after looping the value of currentnode will be the last node
        if currentnode.endOfString == True:  
            return True  
        else:
            return False            # just a prefix
        

# 4. DELETE STRING
def deleteString(root, word, index):            # word we want to delete, index of characters in the word
    ch = word[index]    # find first character
    currentnode = root.children.get(ch)     # current node
    canThisNodeBeDeleted = False

    # case 1. some other string prefix is same as the one we want to delete(API,APPLE)
    if len(currentnode.children) > 1:
        deleteString(currentnode, word, index+1)
        return False    # this is used for canThisNodeBeDeleted 
    
    # case 2. we are at the last word but this is also a prefix of some other word
    if index == len(word)-1:
        if len(currentnode.children) >= 1:
            currentnode.endOfString = False
            return False
        
        # if theres not any other node dependent on this character(not a prefix) simply delete the node
        else:
            root.children.pop(ch)
            return True     # returning true (ok to delete the character )

    # case 3. other string is a prefix of this string(APIS,AP)
    if currentnode.endOfString == True:
        deleteString(currentnode, word, index+1)
        return False
    # case 4. not dependent on any string(call deletestring recusrively and save the result to canthisnodebedeleted)
    canThisNodeBeDeleted = deleteString(currentnode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False        # some other string is dependent on this character

# 1. CREATION
newTrie = Trie()

# tc = sc = O(1)  as empty node is being created

# 2. INSERTION
newTrie.insertString('App')
newTrie.insertString('Appi')
# tc = sc = O(M)  if characters doesnot exist then it will create m space for m character 

# 3. SEARCH
#print(newTrie.searchNode('App'))

# 4. DELETE
print(deleteString(newTrie.root, 'App', 0))     # make sure calling it for rootnode not trie
# tc : O(M), sc:(1)