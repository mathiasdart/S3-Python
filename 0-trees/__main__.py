import trees_examples
from algo_py import tree
from algo_py import treeasbin
from algo_py import queue


def to_linear(T):
    s = '(' + str(T.key)
    for child in T.children:
        pass


def to_linear_TAB(B):
    s = '(' + str(B.key)
    C = B.sibling
    while C:
        s += to_linear_TAB(C)
        C = C.sibling
    s += ')'
    return s


def to_linear_bin(B):
    s = '(' + str(B.key)
    if B.child:
        s += to_linear_bin(B.child)
    s += ')'
    if B.sibling:
        s += to_linear_bin(B.sibling)
    return s


## BFS

def printLevel(T):
    Q = queue.Queue()
    Q.enqueue(T)
    Q.enqueue(None)
    while not Q.isempty():
        N = Q.dequeue()
        if N == None:
            if not Q.isempty():
                print()
                Q.enqueue(None)
        else:
            print(N.key, end=" ")
            for child in N.children:
                Q.enqueue(child)


def dot(T):
    s = "graph{\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s = s + "     " + str(T.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
    return s + "\n}"


def dotTAB(TAB):
    s = "graph{\n"
    q = queue.Queue()
    q.enqueue(TAB)
    while not q.isempty():
        B = q.dequeue()
        C = B.child
        while C:
            s = s + '    ' + str(B.key) + " -- " + str(C.key) + "\n"
            q.enqueue(C)
            C = C.sibling
        return s + "}"


def morechildren(T):
    if T.children is None:
        return True
    else:
        i = 0
        res = True
        while i < T.nbchildren is not None and res:
            if T.children[i].nbchildren != 0:
                res = T.nbchildren < T.children[i].nbchildren and morechildren(T.children[i])
            i += 1
        return res


def PMEB(T):
    if T.nbchildren == 0:
        return 1, 1
    else:
        LCE = 0
        NF = 0
        for child in T.children:
            LCEB, NFB = PMEB(child)
            LCE += LCEB + 1
            NF += NFB
        return LCE, NF


def PME(T):
    LCE, NF = PMEB(T)
    print(LCE)
    print(NF)
    return LCE / NF


def PMETAB(B):
    pass


def symmetric(T, B):
    if T == None or B == None:
        return T == B
    if T.key == B.key:
        BChild = B.child
        TChild = T.children
        n = T.nbchildren
        i = n
        while i >= 0 and BChild and (TChild[n - 1 - i].key == BChild.key) and symmetric(TChild[n - 1 - i], BChild):
            BChild = BChild.sibling
            i -= 1
        return i == 0 and not BChild
    else:
        return False


def tabtotree(B):
    if B == None:
        return []
    else:
        L = []
        while B:
            L.append(tree.Tree(B.key, tabtotree(B.child)))
            B = B.sibling
        return L


T = tabtotree(trees_examples.B1)
#printLevel(T)

print(symmetric(trees_examples.T6, trees_examples.B6))
print(symmetric(trees_examples.T7, trees_examples.B7))
print(symmetric(trees_examples.T8, trees_examples.B8))
##T1 : LCE = 15 / NF = 7
##print(dot(trees_examples.T3))
"""
Correction
"""


def _count(T, depth=0):
    if not T.children:
        return depth, 1
    else:
        sum_depth, nb_leaves = (0, 0)
        for child in T.children:
            s, n = _count(child, depth + 1)
            sum_depth += s
            nb_leaves += n
        return sum_depth, nb_leaves


def external_average_depth(T):
    s, n = _count(T)
    return s / n


def _count_tab(B, depth=0):
    if B.child is None:
        return depth, 1
    else:
        BChild = B.child
        sum_depth, nb_leaves = 0, 0
        while BChild != None:
            s, n = _count_tab(BChild, depth + 1)
            sum_depth += s
            nb_leaves += n
            BChild = BChild.sibling
        return sum_depth, nb_leaves


def external_average_depth_tab(T):
    s, n = _count_tab(T, 0)
    return s / n


def same(T, B):
    if T.key != B.key:
        return False
    else:
        C = B.sibling
        i = 0
        while C and i < T.nbchildren and same(T.children[i], C):
            C = C.sibling
            i += 1
        return C == None and i == T.nbchildren

def treeasbin_to_tree(B):
    T = tree.Tree(B.key,[])
    C = B.child
    while C:
        T.children.append(treeasbin_to_tree(C))
        C = C.sibling
    return T




print(external_average_depth(trees_examples.T1))
print(external_average_depth_tab(trees_examples.B1))
T = treeasbin_to_tree(trees_examples.B1)
printLevel(T)
