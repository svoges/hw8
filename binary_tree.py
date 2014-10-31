def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == "__main__":
    freq = {"begin": .05,
            "do"   : .4,
            "else" : .08,
            "end"  : .04,
            "if"   : .1,
            "then" : .1,
            "while": .23}
    r = BinaryTree(max(freq, key=freq.get))
    print(r[0])
    del(freq[r[0]])
    dleft = dict(freq.items())
    print(dleft)





# r = BinaryTree(3)
# insertLeft(r,4)
# insertLeft(r,5)
# insertRight(r,6)
# insertRight(r,7)
# l = getLeftChild(r)
# print(l)
#
# setRootVal(l,9)
# print(r)
# insertLeft(l,11)
# print(r)
# print(getRightChild(getRightChild(r)))
