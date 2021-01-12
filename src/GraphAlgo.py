import json
from math import inf
from typing import List
from matplotlib import pyplot as plt
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.Tarjan import tarjan


class GraphAlgo(GraphAlgoInterface):
    """
    This class implements GraphAlgoInterface.
    it contains algorithms applied to a Directed Weighted Graph (implemented in DiGraph class).

    """

    def __init__(self, graph: GraphInterface = None):
        """This is the constructor of the class.
        it has only 1 parameter - a directed weighted graph.
        if no such graph given, a new graph of the DiGraph implementation is created and initialized.
        else the given graph is initialized as the underlying graph.
        """
        if graph is None:
            graph = DiGraph()
        self.g = graph

    def get_graph(self) -> GraphInterface:
        """
        return: a shallow copy of the directed graph on which the algorithm works on.
        """
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        new_graph = DiGraph()
        try:
            with open(file_name, "r") as f:
                loaded = json.load(f)
                for i in loaded.get("Nodes"):
                    id_key = i.get("id")
                    post = None
                    if i.get("pos") is not None:
                        pos = i.get("pos").split(sep=",")
                        post = (float(pos[0]), float(pos[1]), float(pos[2]))
                    new_graph.add_node(id_key, post)
                for i in loaded.get("Edges"):
                    src = i.get("src")
                    w = i.get("w")
                    dest = i.get("dest")
                    new_graph.add_edge(src, dest, w)
            self.g = new_graph
            return True
        except IOError:
            print("Couldn't load graph. No changes made")
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, "w") as f:
                saved = {"Edges": [], "Nodes": []}
                for i in self.g.nodes.values():
                    key = i.key
                    pos = []
                    for j in i.pos:
                        pos.append(str(j))
                    pos_str = f"{pos[0]},{pos[1]},{pos[2]}"
                    saved["Nodes"].append({"pos": pos_str, "id": key})
                    for j in self.g.all_in_edges_of_node(key):
                        src = j
                        w = self.g.all_in_edges_of_node(key).get(j)
                        edge = {"src": src, "w": w, "dest": key}
                        saved["Edges"].append(edge)
                    for j in self.g.all_out_edges_of_node(key):
                        dest = j
                        w = self.g.all_out_edges_of_node(key).get(j)
                        edge = {"src": key, "w": w, "dest": dest}
                        saved["Edges"].append(edge)
                json.dump(saved, indent=4, fp=f)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through.
        If there is no path between id1 and id2, or one of them does not exist the function returns (inf, [])
        """
        if id1 not in self.g.nodes or id2 not in self.g.nodes:
            return inf, []
        if id1 is id2:
            return 0, [id1]
        dists = {}
        parents = {}
        start = self.g.nodes.get(id1)
        dists[id1] = 0
        q = [start, ]
        while len(q) > 0:
            n = q.pop(0)
            neighs = self.g.all_out_edges_of_node(n.key)
            for i in neighs:
                curr_dist = dists[n.key] + n.get_edge(i)
                if not dists.__contains__(i) or curr_dist < dists[i]:
                    dists[i] = curr_dist
                    parents[i] = n.key
                    q.append(self.g.nodes[i])
        if not dists.__contains__(id2):
            return inf, []
        path = []
        itr = id2
        while itr is not id1:
            path.insert(0, itr)
            itr = parents[itr]
        path.insert(0, id1)
        return dists[id2], path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        if id1 not in self.g.nodes:
            return []
        start = self.g.nodes.get(id1)
        connected = [id1, ]
        q = [start, ]
        visited1 = [start, ]
        visited2 = [start, ]
        while q:
            n = q.pop(0)
            neighs = self.g.all_out_edges_of_node(n.key)
            for i in neighs:
                nn = self.g.nodes[i]
                if not visited1.__contains__(nn):
                    visited1.append(nn)
                    q.append(nn)
        q.append(start)
        while q:
            n = q.pop(0)
            neighs = self.g.all_in_edges_of_node(n.key)
            for i in neighs:
                nn = self.g.nodes[i]
                if not visited2.__contains__(nn):
                    visited2.append(nn)
                    q.append(nn)
        if len(visited1) <= len(visited2):
            for i in visited1:
                if visited2.__contains__(i) and not connected.__contains__(i.key):
                    connected.append(i.key)
        elif len(visited1) > len(visited2):
            for i in visited2:
                if visited1.__contains__(i) and not connected.__contains__(i.key):
                    connected.append(i.key)
        return connected

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        using Tarjan's algorithm in an iterative implementation for being able to check very big graphs.
        for further information about Tarjan's implementation see Tarjan class doc.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        return tarjan(self.g)

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        each directed edge is represented as an arrow, which points the dest, starting from src.
        each node is represented as a red dot with it's key above it's location.
        @return: None
        """
        x_values = []
        y_values = []
        for i in self.g.nodes.values():
            pos = i.pos
            x_values.append(pos[0])
            y_values.append(pos[1])
            plt.annotate(text=f"{i.key}", xy=(pos[0] + 0.0002, pos[1] + 0.0002),
                         xytext=(pos[0] - 0.0002, pos[1] + 0.0002), color='darkcyan')
        node = self.g.nodes[0]
        x_values.append(node.pos[0])
        y_values.append(node.pos[1])
        for i in self.g.edges:
            src_key = i.get("src")
            dest_key = i.get("dest")
            src = self.g.nodes.get(src_key)
            dest = self.g.nodes.get(dest_key)
            plt.annotate("", xy=(dest.pos[0], dest.pos[1]), xytext=(src.pos[0], src.pos[1]),
                         arrowprops=dict(edgecolor='olive', facecolor='black', arrowstyle='-|>'))
        plt.plot(x_values, y_values, ".", color='red')
        plt.show()


def main():
    pass


if __name__ == '__main__':
    main()
