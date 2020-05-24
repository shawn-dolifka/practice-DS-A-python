''' 
An implementation of a Tree Abstract Data Type 
'''

class Tree:
    '''Abstract base class representing a tree structure.'''

    #===================== Nested Position class =====================#
    class Position:
        '''An abstraction representing the location of a single element.'''

        def element(self):
            '''Return the element stored at this position'''
            raise NotImplementedError('Must be implemented by subclass.')

        def __eq__(self, other):
            '''Return True if other Position represents the same location'''
            raise NotImplementedError('Must be implemented by subclass.')

        def __ne__(self, other):
            '''Return True if other does not represent the same location'''
            return not (self == other)  #Opposite of __eq__

    #====== Abstract methods that concrete subcless must support ======#

    def root(self):
        '''Return Position representing the tree's root (or None if empty)'''
        raise NotImplementedError('Must be implemented by subclass.')

    def parent(self, p):
        '''Return position representing p's parent (or None if p is root)'''
        raise NotImplementedError('Must be implemented by subclass.')

    def num_children(self, p):
        '''Return the number of children that Position p has'''
        raise NotImplementedError('Must be implemented by subclass.')

    def children(self, p):
        '''Generate an iteration of Positions representing p's children'''
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        '''Return the total number of elements in the tree'''
        raise NotImplementedError('Must be implemented by subclass.')

    #======== Concrete methods implemented in this class ========#

    def is_root(self, p):
        '''Return True if Position p represents the root of the tree'''
        return self.root() == p

    def is_leaf(self, p):
        '''Return True if Position p has NO children'''
        return self.num_children(p) == 0

    def is_empty(self):
        '''Return True if the tree is empty'''
        return len(self) == 0

        