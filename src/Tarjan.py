from typing import List


def depth_first_search(g, n, low_link, id_dict, scc_list, scc_set, itr):
    nodes = g.get_all_v()
    scc = {}
    q = [n]
    while q:
        n = q[-1]
        if n not in id_dict:
            id_dict[n] = itr
            low_link[n] = itr
            scc[itr] = [nodes[n]]
            itr += 1
        flag = True
        for neighbor in g.all_out_edges_of_node(n):
            if neighbor not in id_dict:
                flag = False
                q.append(neighbor)
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
            q.pop()


def tarjan(g) -> List[list]:
    itr = 0
    low_link = {}
    ids = {}
    scc_set = set()
    scc_list = []
    for node in g.get_all_v():
        if node not in scc_set:
            depth_first_search(g, node, low_link, ids, scc_list, scc_set, itr)
    return scc_list
