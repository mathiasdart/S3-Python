import queue

from algo_py import graph
from algo_py import graphmat
from algo_py import queue
import ex_graphs


def degrees(G: graphmat):
    n = G.order
    M = G.adj
    deg = [0] * n
    for i in range(n):
        for j in range(i):
            if M[i][j] >= 1:
                deg[i] += M[i][j]
        if M[i][i] == 1:
            deg[i] += 2
        for k in range(i + 1, n):
            if M[i][k] >= 1:
                deg[i] += M[i][k]
    return deg


def in_out_degrees(G: graph.Graph):
    din = [0] * G.order
    dout = [0] * G.order
    for x in range(G.order):
        for y in G.adjlists[x]:
            # x -> y edge
            din[y] += 1
            dout[x] += 1
    return din, dout


def outdegree(G):
    return [len(L) for L in G.adjlists]


def dotMat(G: graphmat.GraphMat):
    n = G.order
    M = G.adj
    if G.directed:
        s = "digraph {"
        link = " -> "
        s += "\n"
        for i in range(n):
            for j in range(n):
                if M[i][j] > 0:
                    s += M[i][j] * (str(i) + link + str(j) + "\n")
    else:
        s = "graph {"
        link = " -- "
        s += "\n"
        for i in range(n):
            for j in range(i + 1):
                if M[i][j] > 0:
                    s += M[i][j] * (str(i) + link + str(j) + "\n")
    return s + "}\n"


def todotGraph(G):
    """Dot format of graph.

    Args:
        Graph

    Returns:
        str: String storing dot format of graph.

    """
    n = G.order
    if G.directed:
        s = "digraph {"
        link = " -> "
        s += "\n"
        for x in range(n):
            for y in G.adjlists[x]:
                s += str(x) + link + str(y) + "\n"
    else:
        s = "graph {"
        link = " -- "
        s += "\n"
    for x in range(n):
        for y in G.adjlists[x]:
            if x >= y:
                s += str(x) + link + str(x) + "\n"
    return s + "}\n"


def buildparentA(G):
    M = [False] * G.order
    A = G.adjlists
    P = [None] * G.order
    for s in range(G.order):
        if M[s] is False:
            buildparentA__(G, M, A, s, P)
    return P


def buildparentA__(G, M, A, s, P):
    """
    Args:
        G: Graph
        M: Marque
        A: G.adj
        s: sommet actuel
        P: liste des parents
    Returns: liste des parents actualisée

    """
    Q = queue.Queue()
    Q.enqueue(s)
    M[s] = True
    P[s] = -1
    print(s, end=" ")
    while not Q.isempty():
        S = Q.dequeue()
        for x in A[S]:
            if M[x] is False:
                Q.enqueue(x)
                P[x] = S
                M[x] = True
                print(x, end=" ")
    print()


def buildParentMat(G):
    M = [False] * G.order
    Mat = G.adj
    P = [None]* G.order
    for s in range(G.order):
        if M[s] is False:
            buildParentMat__(G, M, s, Mat,P)


def buildParentMat__(G, M, s, Mat, P):
    Q = queue.Queue()
    Q.enqueue(s)
    M[s] = True
    print(s, end=" ")
    while not Q.isempty():
        S = Q.dequeue()
        P[S] = -1
        i = 0
        for x in Mat[S]:
            if x != 0:
                if M[i] is False:
                    Q.enqueue(i)
                    M[i] = True
                    P[i] = x
                    print(i, end=" ")
            i += 1
        i = 0
    print()



def prefixeAdj(G, start):
    M = [False] * G.order
    Mat = G.adjlists
    BFSprefAdj(G, start, M, Mat)
    for s in range(G.order):
        if M[s] is False:
            BFSprefAdj(G, s, M, Mat)


def BFSprefAdj(G, s, M, A):
    """
    Args:
        G: Graph
        s: sommet actuel
        M: marques
        A: G.adjlists
    Returns: affiche les sommets dans l'ordre de rencontre
    """
    Q = queue.Queue()
    Q.enqueue(s)
    M[s] = True
    print(s, end=" ")
    while not Q.isempty():
        S = Q.dequeue()
        for x in A[S]:
            if M[x] is False:
                Q.enqueue(x)
                M[x] = True
                print(x, end=" ")
    print()


def prefixeMat(G: graphmat.GraphMat, start):
    M = [False] * G.order
    Mat = G.adj
    BFSprefMat(G, start, M, Mat)
    for s in range(G.order):
        if M[s] is False:
            BFSprefMat(G, s, M, Mat)


def BFSprefMat(G, s, M, Mat):
    Q = queue.Queue()
    Q.enqueue(s)
    M[s] = True
    print(s, end=" ")
    while not Q.isempty():
        S = Q.dequeue()
        i = 0
        for x in Mat[S]:
            if x != 0:
                if M[i] is False:
                    Q.enqueue(i)
                    M[i] = True
                    print(i, end=" ")
            i += 1
        i = 0
    print()


print(buildparentA(ex_graphs.G1))
print()
print(buildParentMat(ex_graphs.G1mat))

"""
prefixeAdj(ex_graphs.G1,0)
print()
prefixeMat(ex_graphs.G1mat,0)
"""
