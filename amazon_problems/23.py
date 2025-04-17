# serialize and deserialize a binary tree
# Serialization is the process of converting 
# a data structure or object into a sequence of 
# bits so that it can be stored in a file or memory buffer, 
# or transmitted across a network connection link to be reconstructed
# later in the same or another computer environment.

class Treenode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self,root):
        def doit(node): # recursive helper function to perform preorder traversal
            if node: # if current node is not none
                vals.append(str(node.val)) # append the string representation of the nodes value to vals list
                doit(node.left) # recursively call 'doit' on the left child
                doit(node.right) #recursively call 'doit' on the right child
            else: #if the current node is none (missing child)
                vals.append('#')
        vals = [] # initialize an empty list to store the serialized tree values
        doit(root) # call the recursive doit function starting from the root
        return ' '.join(vals)
    
    def deserialize(self, data):
        def doit(): #define a recursive helper function to reconstruct the tree
            val = next(vals) # get the next value from the iterator 'vals'
            if val == '#': # null node
                return None
            node = Treenode(int(val))
            node.left = doit()
            node.right = doit()
            return node # return the reconstructed tree
        vals = iter(data.split())
        return doit() 
            