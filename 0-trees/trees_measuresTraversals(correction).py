# -*- coding: utf-8 -*-
"""
S3 - trees measures & traversals
"""

from algopy import tree, treeasbin
from algopy import queue

"""
Measures
"""

def size(T):
    s = 1
    for i in range(T.nbchildren):
        s += size(T.children[i])
    return s
    
# or
def size2(T):
    s = 1
    for C in T.children:
        s += size(C)
    return s    


def sizeasbin(B):
    s = 1
    child = B.child
    while child != None :
        s += sizeasbin(child)
        child = child.sibling
    return s
                
# height

def height(T):
    h = 0
    for C in T.children:
        h = max(h, height(C)+1)
    return h

def heightasbin(B):
    h = -1
    C = B.child
    while C != None:
        h = max(h, heightasbin(C))
        C = C.sibling
    return h + 1

# bonus
def heightasbin2(B):
    if B == None:
        return -1
    else:
        return max(1 + heightasbin2(B.child), heightasbin2(B.sibling))
    

    

"""
Traversals
"""

"""
Depth First Search (DFS)
"""

# most of the time, use the simple version

def dfs(T):
    print(T.key)    # preorder = prefix
    for C in T.children:
        dfs(C)
    # postorder = suffix
        
def dfs_TAB(B):
    print(B.key) # prefix
    child = B.child
    while child != None:
        dfs_TAB(child)
        child = child.sibling
    # postorder

# "full" version (with intermediate added) => use them only when really necessary

def dfs_full(T):
    print(T.key)    # preorder = prefix
    if T.nbchildren != 0:
        for i in range(T.nbchildren - 1):
            dfs_full(T.children[i])
            # intermediate
        dfs_full(T.children[T.nbchildren-1])
    # postorder = suffix
        
def dfs_TAB_full(B):
    print(B.key) # preorder
    if B.child != None:
        child = B.child
        while child.sibling != None:
            dfs_TAB_full(child)
            # intermediate
            child = child.sibling
        dfs_TAB_full(child)
    # postorder

# example: displayu a tree "<o A0,A1,...>"
def display_tree(T):
    print('<', T.key, sep='', end='')    # preorder = prefix
    if T.nbchildren != 0:
        for i in range(T.nbchildren - 1):
            display_tree(T.children[i])
            # intermediate
            print(',', end='')
        display_tree(T.children[T.nbchildren-1])
    # postorder = suffix
    print('>', end='')
        
def display_tree_TAB(B):
    print('<', B.key, sep='', end='')    # preorder = prefix
    if B.child != None:
        child = B.child
        while child.sibling != None:
            display_tree_TAB(child)
             # intermediate
            print(',', end='')
            child = child.sibling
        display_tree_TAB(child)
    # postorder
    print('>', end='')        
        

"""
Breadth First Search (BFS)
"""

# simple BFS: : displays keys 

def BFS(T):
    """
    T: Tree
    display T's keys
    """
    q = queue.Queue()
    q.enqueue(T)
    
    while not q.isempty():
        T = q.dequeue()
        print(T.key, end=' ')
        for child in T.children:
            q.enqueue(child)

def BFS_tab(B):
    """
    B: TreeAsBin
    display B's keys
    """
    q = queue.Queue()
    q.enqueue(B)
    
    while not q.isempty():
        B = q.dequeue()
        print(B.key, end=' ')
        child = B.child
        while child != None:
            q.enqueue(child)
            child = child.sibling

#############
# print one level per line :  need to know when we change level
# first version with Tree: a "end level mark" (None) is add in the queue

def bfs_levels(T):
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
   
    while not q.isempty():
        T = q.dequeue()
        if T == None:
            print()
            if not q.isempty():
                q.enqueue(None)
        else:
            print(T.key, end=' ')
            for child in T.children:
                q.enqueue(child)



#second version with TreeAsBin: two queues

def bfsasbin_levels(B):
    q_out = queue.Queue()
    q_in = queue.Queue()
    q_out.enqueue(B)
    while not q_out.isempty():
        #FIXME
        pass

    
