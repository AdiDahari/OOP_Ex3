from typing import List
"""
This class additionally made for handling the connected_components method of GraphAlgo's class.
this implementation gives a very good time complexity for finding the connected components of a given Directed Graph in
a very efficient way.
the main structure of this implementation is based on the DFS algorithm.
each node is being checked only once by holding all checked elements in a data structure and assuring each iteration 
the given node hasn't been checked and applied for another connected component.
the wrapping element is the tarjan method, which handles the iteration as an alternative 
to the recursive implementation of Tarjan.
an iterator (itr) is marking each iteration to the outer elements of tarjan method each iteration.
at each end of the DFS iterations the scc_list, which holds all the components already found is extended by a new list.
the conversion of the recursive method to the iterative one has been done by the ideas explained in the following links:
1. https://www.youtube.com/watch?v=wUgWX0nc4NY&t=376s - William Fiset's youtube video visualizing and explaining
                                                        Tarjan's algorithm on directed graphs.

2. https://llbit.se/?p=3379 - Jesper Öqvist's blog, a PhD student of Lund University in Sweden.
"""


def depth_first_search(g, n, low_link, id_dict, scc_list, scc_set, itr):
    nodes = g.get_all_v()
    scc = {}
    s = [n, ]
    while s:
        n = s[-1]
        if n not in id_dict:
            id_dict[n] = itr
            low_link[n] = itr
            scc[itr] = [nodes[n]]
            itr += 1
        flag = True
        for neighbor in g.all_out_edges_of_node(n):
            if neighbor not in id_dict:
                flag = False
                s.append(neighbor)
                break
        if flag:
            min_link = low_link[n]
            for neighbor in g.all_out_edges_of_node(n):
                if neighbor not in scc_set:
                    low_link[n] = min(low_link[n], low_link[neighbor])
            if low_link[n] is not id_dict[n]:
                if low_link[n] not in scc:
                    scc[low_link[n]] = []
                scc[low_link[n]].extend(scc[min_link])
                for i in scc[min_link]:
                    low_link[i.key] = low_link[n]
            else:
                scc_list.append(scc[low_link[n]])
                scc_set.update([curr.key for curr in scc[low_link[n]]])
            s.pop()


def tarjan(g) -> List[list]:
    itr = 0
    low_link = {}
    ids = {}
    scc_set = set()
    scc_list = []
    ans = []
    for node in g.get_all_v():
        if node not in scc_set:
            depth_first_search(g, node, low_link, ids, scc_list, scc_set, itr)

    for i in scc_list:
        curr_list = []
        for j in i:
            curr_list.append(j.key)
        ans.append(curr_list)
    return ans
