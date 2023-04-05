from algo_py import graph
from algo_py import graphmat
from algo_py import queue
import ex_graphs


def __dfs_digraph(G, x, pref, suff, cpt):
    """
    DFS in digraph G from x
    fill-in pref with prefix and suff  with suffix numberings of vertices with the single counter cpt
    display back, forward and cross edges
    return cpt
    """
    cpt += 1
    pref[x] = cpt
    for y in G.adjlists[x]:
        if pref[y] == None:
            cpt = __dfs_digraph(G, y, pref, suff, cpt)
        else:
            if pref[x] < pref[y]:
                print(x, "->", y, "forward")
            elif suff[y] == None:
                print(x, "->", y, "back")
            else:
                print(x, "->", y, "cross")
    cpt += 1
    suff[x] = cpt
    return cpt


# reminder: int values are "unmutable" => cpt cannot be passed by reference
# that why the functions return cpt!

def dfs_digraph(G):
    """
    full DFS of digraph G
    return pref and suff:    vectors of prefix and suffix numberings of vertices with a single counter
    display back, forward and cross edges
    """
    pref = [None] * G.order  # used to mark vertices
    suff = [None] * G.order
    cpt = 0
    for s in range(G.order):
        if pref[s] == None:
            cpt = __dfs_digraph(G, s, pref, suff, cpt)
    return pref, suff


def __components(G, mq, act, Mat, s):
    q = queue.Queue()
    q.enqueue(s)
    while not q.isempty():
        A = q.dequeue()
        for x in Mat[A]:
            if mq[x] == 0:
                mq[x] = act
                q.enqueue(x)


def components(G):
    mq = [0] * G.order
    act = 1
    for s in range(G.order):
        if mq[s] == 0:
            mq[s] = act
            __components(G, mq, act, G.adjlists, s)
            act += 1
    return mq


def __DFS_path(G, path, mq, s, search):
    for x in G.adjlists[s]:
        if mq[x] == 0:
            mq[x] = 1
            if x == search:
                path.append(x)
                return path
            path.append(x)
            return __DFS_path(G, path, mq, x, search)


def DFS_path(G, beg, end):
    mq = [0] * G.order
    mq[beg] = 1
    return __DFS_path(G, [beg], mq, beg, end)


def __path_BFS(G, scr, dst, P):
    q = queue.Queue()
    q.enqueue(G)
    P[scr] = -1
    while not q.isempty():
        x = q.dequeue()
        for y in G.adjlists[x]:
            if P[y] == None:
                q.enqueue(y)
                P[y] = x


def path_BFS(G, src, dst):
    P = [None] * G.order
    path = []
    if __path_BFS(G, src, dst, P):
        while dst != -1:
            path.append(dst)
            dst = P[dst]
    return path


def excentricity(G, src):
    dist = [-1] * G.order
    q = queue.Queue()
    q.enqueue(src)
    dist[src] = 0
    while not q.isempty():
        s = q.dequeue()
        for adj in G.adjlists[s]:
            if dist[adj] == -1:
                dist[adj] = dist[s] + 1
                q.enqueue(adj)
    return dist[s]


def center(G):
    excMin = excentricity(G, 0)
    L = [0]
    for s in range(1, G.order):
        exc = excentricity(G, s)
        if exc < excMin:
            (L, excMin) = ([s], exc)
        elif exc == excMin:
            L.append(s)
    return L

def is_tree(G):
    L = components(G)
    i = 0
    n = len(L)
    while i < n and L[i] == 1:
        i+=1
    if i != n:
        return False
    for j in range(len(G.adjlists)-1):
        if j in G.adjlists[j]:
            return False
    return True

import files

G = graph.load("files/graphISP_tree.gra")
print(is_tree(G))








'''
print(dfs_digraph(ex_graphs.G1))
print(components(ex_graphs.G3_cc))

'''
