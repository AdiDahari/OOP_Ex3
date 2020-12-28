from typing import Tuple

from GraphInterface import GraphInterface


class Node:
    def __init__(self, key: int, pos: Tuple = None, edges_in: dict = None, edges_out: dict = None):
        self.key = key
        self.pos = pos
        if edges_in is None:
            self.e_in = {}
        else:
            self.e_in = edges_in
        if edges_out is None:
            self.e_out = {}
        else:
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
        if nodes is None:
            self.nodes = {}
        else:
            self.nodes = nodes
        if edges is None:
            self.edges = []
        else:
            self.edges = edges
        self.ec = ec
        self.mc = mc

    def __str__(self):
        return f"Nodes: {self.nodes}, Edges: {self.edges}, eCount: {self.ec}, mCount: {self.mc}"

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.nodes)

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
        if id1 == id2:
            return False
        n1 = self.nodes.get(id1)
        n2 = self.nodes.get(id2)
        if (n1 is not None) and (n2 is not None) and (n1.e_out.get(id2) is None) and (weight >= 0):
            n1.e_out[id2] = (id2, weight)
            n2.e_in[id1] = (id1, weight)
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
        if node_id not in self.nodes:
            return False
        n = self.nodes[node_id]
        edges_in = n.e_in
        edges_out = n.e_out
        for i in edges_in:
            self.nodes[i].e_out.pop(node_id)
            self.ec -= 1
            self.edges.remove((i, node_id))
        for j in edges_out:
            self.nodes[j].e_in.pop(node_id)
            self.ec -= 1
            self.edges.remove((node_id, j))
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
    for i in range(10):
        g.add_node(i)
        if i > 0:
            g.add_edge(i-1, i, i)
    for i in range(10):
        g.add_edge(0, i, 1)
    print(g)
    print(g.all_out_edges_of_node(0))
    print(g.all_in_edges_of_node(0))
    g.add_node(10)
    print(g.all_in_edges_of_node(10))


if __name__ == '__main__':
    main()
