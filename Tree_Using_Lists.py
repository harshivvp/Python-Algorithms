def BinaryTree(r): #for root node R
    return [r,[],[]]

def insertLeftChild(root,newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])

    else:
        root.insert(1,[newBranch,[],[]])

    return root

def insertRightChild(root,newBranch):
    t = root.pop(2)

    if len(t) > 1:
        t = root.insert(2,[newBranch,[],t])

    else:
        t = root.insert(2,[newBranch,[],[]])

def getRootValue(root):
    return root[0]

def setRootValue(root,newValue):
    root[0] = newValue

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == "__main__":

    r = BinaryTree(3)

    insertLeftChild(r,4)
    insertLeftChild(r,5)
    insertRightChild(r,6)
    insertRightChild(r,7)

    l = getLeftChild(r)
    print(l)

