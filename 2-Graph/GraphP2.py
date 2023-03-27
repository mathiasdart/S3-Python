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
                print(x, "->", y , "forward")
            elif suff[y] == None:
                print(x, "->", y , "back")
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

def __components(G,mq,act,Mat,s):
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
    for s in range (G.order):
        if mq[s] == 0:
            mq[s] = act
            __components(G,mq,act,G.adjlists,s)
            act +=1
    return mq

def __wayO(G,path,mq,s,search):
    for x in G.adjlists[s]:
        if mq[x] == 0:
            mq[x] = 1
            if x == search:
                return path.append(x)
            return __wayO(G,path.append(x),mq,x)
def wayO(G,search):
    mq = [0] * G.order
    path = []
    for s in range(G.order):
        if mq[s] == 0:
            finalpath = __wayO(G,path,mq,s,seach)
    return finalpath



def wayNO():
    pass
print(components(ex_graphs.G3_cc))

'''
print(dfs_digraph(ex_graphs.G1))

'''