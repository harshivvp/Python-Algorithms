class BinaryTree(object):

    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self,newNode):

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild  = self.leftChild
            self.leftChild = t

    def insertRightChild(self,newNode):

        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        print(self.key)

r = BinaryTree('a')

r.getRootVal()

r.insertLeftChild('b')
r.insertRightChild('c')

r.getLeftChild().getRootVal()
r.getRightChild().getRootVal()
