class BinarySearchTree:
    def __init__(self):
        self.size=0
        self.root=None

    class BSTNode:
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.left=None
            self.right=None
            self.parent=None

    def add(self, key, value):
        z=self.BSTNode(key, value)
        y=None
        x=self.root
        if(self.root==None):
            self.root=z
            self.size+=1
            return 
        while(x!=None):
            y=x
            if(z.key<x.key):
                x=x.left
            else:
                x=x.right
        if(z.key<y.key):
            y.left=z
        else:
            y.right=z
        z.parent=y
        self.size+=1
        return 

    def _size(self):
        return self.size

    def empty(self):
        if self.root==None:
            return True
        else:
            return False

    def search(self,key):
        x=self.root
        y=None
        while(x!=None):
            if(key==x.key):
                print("Exists")
                return x
            elif(key<x.key):
                x=x.left
            elif(key>x.key):
                x=x.right
        print("Does not exist")
        return False

    def find_smallest(self):
        y=None
        x=self.root
        while(x!=None):
            y=x
            x=x.left
        return y.key
    
    def find_largest(self):
        
        x=self.root
        y=x
    
        while(x!=None):
            y=x
            x=x.right
        print("NOw here", y.key)
        return y.key
    
    def delete(self, key):
        x=self.search(key)
        
        z=x.parent
        if(x.left==x.right==None):
            if(x.key<z.key):
                z.left=None
            else:
                z.right=None
        else:
            if(x.left!=None and x.right==None):
                y=self.find_largest(x)
                print("it is this one", y.key)
                if(x.key<z.key):
                    z.left=y
                else:
                    z.right=y
                y.left=x.left
                y.right=x.right
            elif(x.left==None and x.right!=None):
                y=self.find_smallest(x)
                if(x.key<z.key):
                    z.left=y
                else:
                    z.right=y
                y.left=x.left
                y.right=x.right
        #print("alright")
        self.size-=1
        
    def display(self):
        x=self.root
        while(x!=None):
            print(x.key)
            x=x.left
        x=self.root.right
        while(x!=None):
            print(x.key)
            x=x.right

    def inOrderWalk(self):
            nodes = []
            self._inOrderWalk(self.root, nodes)
            return nodes

    def _inOrderWalk(self, subtree, nodes):
        if(subtree):
            self._inOrderWalk(subtree.left, nodes)
            nodes.append(subtree.key)
            self._inOrderWalk(subtree.right, nodes)

    def preOrderWalk(self):
        nodes = []
        self._preOrderWalk(self.root, nodes)
        return nodes

    def _preOrderWalk(self, subtree, nodes):
        if(subtree):
            nodes.append(subtree.key)
            self._preOrderWalk(subtree.left, nodes)
            self._preOrderWalk(subtree.right, nodes)

    def postOrderWalk(self):
        nodes = []
        self._postOrderWalk(self.root, nodes)
        return nodes

    def _postOrderWalk(self, subtree, nodes):
        if(subtree):
            self._preOrderWalk(subtree.left, nodes)
            self._preOrderWalk(subtree.right, nodes)
            nodes.append(subtree.key)


