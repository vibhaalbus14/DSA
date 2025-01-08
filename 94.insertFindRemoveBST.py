#time comp
#insert,remove,find : O(logn) bc,avg case and O(n) wc
#space comp
#recursive:O(logn) bc,avg case and O(n) wc
#iterative: O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        #create a node
        newNode=Node(value)
        #checking if tree is empty
        if  self.root==None:
            self.root=newNode
            return self
        curr=self.root
        if value<curr.value:
            if curr.left==None:#no left node
                curr.left=newNode
                return self
            curr=curr.left
        else:
            if curr.right==None:#no right node
                curr.right=newNode
                return self
            curr=curr.right

    def find(self, value):
        #check if tree is empty
        if self.root==None:
            return False
        curr=self.root
        while curr:
            if value==curr.value:
                return curr
            elif value<curr.value:
                curr=curr.left
            else:
                 curr=curr.right
        return False

    def remove(self, value, current=None, parent=None):
        #if tree is empty
        if not self.root:
            return False
        if current==None:
            current=self.root
        #identify the node to be deleted
        while current:
            if value<current.value:
                parent=current
                current=current.left
            elif value>current.value:
                parent=current
                current=current.right
            else:
                #curr.value==value

                #2 nodes
                if current.left and current.right:#be it root node or any other node
                    #replace the curr.value with inorder predecessor or successor
                    current.value=self.get_min(current.right)#successor present in right subtree
                    #now delete the replaced node
                    self.remove(current.value,current.right,current)
                
                #root node
                elif parent==None:
                    #only one node
                    if current.left:
                        self.root=current.left
                    else:
                        self.root=current.right
                    #no node
                    if  not current.left and not current.right:
                        self.root=None
                #other node , having both 1 node or 0 node case
                elif current==parent.left:
                    if current.left:
                        parent.left=current.left
                    else:
                        parent.left=current.right
                elif current==parent.right:
                    if current.left:
                        parent.right=current.left
                    else:
                        parent.right=current.right
                break
        return self

    def get_min(self, node):
            while node.left:
                node = node.left
            return node.value

    


