'''
Quick tree structure for practice. It doesn't do balancing.
'''
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = None

    #Insert Node into tree
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    #Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    #Preorder Traversal

    #Inorder traversal
    # Left -> Root -> Right