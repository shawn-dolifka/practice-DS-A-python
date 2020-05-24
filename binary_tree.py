from tree import Tree

'''
Binary Tree ADT
'''
class BinaryTree(Tree):
    '''Abstract base class representing a binary tree structure.'''

    #================ Additional abstract methods ================#

    def left(self, p):
        '''
        Return a Position representing p's left child.
        Return None if p does NOT have a left child.
        '''
        raise NotImplementedError("Must be implemented by subclass.")

    def right(self, p):
        '''
        Return a Position representing p's right child.
        Return None if p does NOT have a right child.
        '''
        raise NotImplementedError("Must be implemented by a subclass")

    #======== Concrete methods implemented in this class ========#

    def sibling(self, p):
        '''Return a Position representing p's sibling (or None if no sibling)'''
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None     # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)   # possibly None
            else:
                return self.left(parent)    # possibly None

    def children(self, p):
        '''Generate an iteration of Positions representing p's children'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)