"""
This file holds an iterative implementation of the Depth First Search algorithm,
as all of the provided parameters are of the outer wrapping method based on Tarjan.
each call of this method is called with the updated elements' such as the id list and scc list, for doing a kind of
iterative callbacks to match the idea of the recursive algorithm.
"""


def depth_first_search(g, n, low_link, id_dict, scc_list, scc_set, itr):
    nodes = g.get_all_v()
    scc = {}
    s = [n, ]
    while s:
        n = s[-1]
        flag = True
        if n not in id_dict:
            id_dict[n] = itr
            low_link[n] = itr
            scc[itr] = [nodes[n], ]
            itr += 1
        for neighbor in g.all_out_edges_of_node(n):
            if neighbor not in id_dict:
                flag = False
                s.append(neighbor)
                break
        if flag:
            min_link = low_link[n]
            for neighbor in g.all_out_edges_of_node(n):
                if neighbor not in scc_set:
                    if low_link[n] > low_link[neighbor]:
                        low_link[n] = low_link[neighbor]
            curr = low_link[n]
            if curr is not id_dict[n]:
                if curr not in scc:
                    scc[curr] = []
                scc[curr].extend(scc[min_link])
                for i in scc[min_link]:
                    key = i.key
                    low_link[key] = low_link[n]
            else:
                scc_list.append(scc[low_link[n]])
                for i in scc[low_link[n]]:
                    scc_set.update([i.key])
            s.pop()
