#from node import *
_author_ = 'Nikita Karatsev'
_project_ = 'Lab4'

from tree import *


def main():
    mytree = BinarySearchTree()
    # mytree.put(3)
    # mytree.put(4)
    # mytree.put(5)
    # mytree.put(7)
    # mytree.put(2)
    # mytree.put(1)
    # mytree.put(6)
    mytree.put(5)
    mytree.put(3)
    mytree.put(7)
    mytree.put(2)
    mytree.put(3)
    mytree.put(6)
    mytree.put(8)
    mytree.put(9)
    mytree.copy_route()
    print(mytree.sizeTree(2))
    print(mytree.peaks)
    #mytree.put(2)

    #print(mytree[6])
    #print(mytree[2])

    #t.root = Node(4)
    #t.root.rchild = Node(5)
    #print (t.root.data) #this works
    #print (t.root.rchild.data) #this works too
    # t = Tree()
    # t.add(t.root,4)
    # t.add(t.root,5)
    #print (t.root.data) #this fails
    #print (t.root.rchild.data) #this fails too

if __name__ == '__main__':
     main()