from typing import Tuple, Dict
from GraphInterface import GraphInterface


class Node:

    def __init__(self, key: int, pos: Tuple = None, edges_in: dict = {}, edges_out: dict = {}):
        self.key = key
        self.pos = pos
        self.e_in = edges_in
        self.e_out = edges_out

    def __str__(self):
        return f"pos:{self.pos}, id:{self.key}"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.key < other.key

    def __hash__(self):
        return self.key


class DiGraph(GraphInterface):

    def __init__(self, nodes: dict = {}, edges: list = [], ec: int = 0, mc: int = 0):
        self.nodes = nodes
        self.edges = edges
        self.ec = ec
        self.mc = mc

    def __str__(self):
        return f"Nodes: {self.nodes}, Edges: {self.edges}, eCount: {self.ec}, mCount: {self.mc}"

    def __repr__(self):
        return str(self)

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.ec

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.nodes:
            n = self.nodes.get(id1)
            return n.e_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.nodes:
            n = self.nodes.get(id1)
            return n.e_out

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        n1 = self.nodes.get(id1)
        n2 = self.nodes.get(id2)
        if (n1 is not None) and (n2 is not None) and (n1.e_out.get(id2) is None) and (weight >= 0):
            n1.e_out.update({id2: (id2, weight)})
            n2.e_in.update({id1: (id1, weight)})
            e = (id1, id2)
            self.edges.append(e)
            self.ec += 1
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        n = Node(node_id, pos)
        self.nodes[node_id] = n
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        n = self.nodes[node_id]
        if n is None:
            return False
        edges_in = n.e_in
        edges_out = n.e_out
        for i in edges_in:
            i.e_out.pop(node_id)
            self.ec -= 1
        for j in edges_out:
            j.e_in.pop(node_id)
            self.ec -= 1
        self.nodes.pop(node_id)
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        n1 = self.nodes.get(node_id1)
        n2 = self.nodes.get(node_id2)
        if not self.edges.__contains__((node_id1, node_id2)):
            return False
        n1.e_out.pop(node_id2)
        n2.e_in.pop(node_id1)
        self.edges.remove((node_id1, node_id2))
        self.ec -= 1
        self.mc += 1
        return True


def main():
    g = DiGraph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 1)
    print(g.all_out_edges_of_node(1))
    # print(g.all_in_edges_of_node(3))
    # print(g.all_in_edges_of_node(1))


if __name__ == '__main__':
    main()
