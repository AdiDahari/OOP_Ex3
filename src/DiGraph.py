import random
from typing import Tuple

from src.GraphInterface import GraphInterface


class Node:
    """
    This class represents a graph's node.
    each node in graph contains:
    1. key: an unique int for each node.
    2. pos: a Tuple representing a 3D position (x,y,z)
    3. e_in: a dict containing all edges going into this node. {src(int): weight(float)}
    4. e_out: a dict containing all edges going out of this node. {dest(int): weight(float)}
    """

    def __init__(self, key: int, pos: Tuple = None, edges_in: dict = None, edges_out: dict = None):
        """
        This is the constructor of the node.
        each node contains:
        1. key(int): an unique key value for each node created.
        2. pos(Tuple): a Tuple representing a relative position on a 2D plane. format:(X(float), Y(float), Z(0.0)).
           if pos value is missing, randomizing a location using random (imported)
        3. e_in(dict): a dictionary containing all in edges of this node. each edge is formatted: {<src key>: <weight>}
           if in edges not provided, initializing an empty dict.
        4. e_out(dict): a dictionary containing all out edges of this node.
           each edge is formatted: {<dest key>: <weight>}
           if out edges not provided initializing an empty dict.
        """
        self.key = key
        if pos is None:
            pos = (random.uniform(35.0, 35.3), random.uniform(32.09, 32.11), 0.0)
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
        """
        Override method for string representation of a node.
        """
        return f"pos:{self.pos}, id:{self.key}"

    def __repr__(self):
        """
        Override method for string representation of a node.
        """
        return str(self)

    def __lt__(self, other):
        """
        Override method for comparing nodes by keys.
        """
        return self.key < other.key

    def __hash__(self):
        """
        Override method for default hashing a node by it's key.
        """
        return self.key


class DiGraph(GraphInterface):
    """
    This class is an implementation of GraphInterface.
    each Directed Weighted Graph contains:
    1. nodes(dict): a dictionary contains all nodes in graph, mapped by their keys.
    2. edges(edges): a list contains all edges in graph. each edge is represented: {<src key>, <weight>, <dest key>}.
    3. ec(int): counting the number of edges in graph.
    4. mc(int): counting the changes being made on graph.
    """

    def __init__(self, nodes: dict = None, edges: list = None, ec: int = 0, mc: int = 0):
        """
        This is the graph constructor.
        each graph initialized:
        1. nodes: dict, default: empty dict.
        2. edges: list, default: empty list.
        3. ec: int, default: 0.
        4. mc: int, default: 0.
        """
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
        """
        Override method for string representation of a graph.
        """
        return f"Nodes: {self.nodes}, Edges: {self.edges}, eCount: {self.ec}, mCount: {self.mc}"

    def __repr__(self):
        """
        Override method for string representation of a graph.
        """
        return str(self)

    def __len__(self):
        """
        Override method to define a graph's size by it's number of nodes.
        """
        return len(self.nodes)

    def v_size(self) -> int:
        """
        Override interface method, returns the number of nodes in graph.
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
        Override interface method, returns the number of edges in graph.
        """
        return self.ec

    def get_all_v(self) -> dict:
        """
        Override interface method, returns a dict containing all nodes in graph, mapped by their keys.
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        Override interface method, if such key exists in graph,
        returns a dict containing all edges going into this node.
        """
        if id1 in self.nodes:
            n = self.nodes.get(id1)
            return n.e_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        Override interface method, if such key exists in graph,
        returns a dict containing all edges going out of this node.
        """
        if id1 in self.nodes:
            n = self.nodes.get(id1)
            return n.e_out

    def get_mc(self) -> int:
        """
        Override interface method, returns the number of changes made in graph since initialized.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Override interface method, this method connects 2 nodes by a directed edge going out of id1 and into id2.
        if one or both nodes aren't related to this graph,
        the weight given is a negative number or id1 == id2, returns False.
        id1's node is being added by a new out-edge with the given weight.
        id2's node is being added by a new in-edge with the given weight.
        edges list of the graph is appended by a new edge.
        ec and mc updated relatively.
        """
        if id1 == id2:
            return False
        n1 = self.nodes.get(id1)
        n2 = self.nodes.get(id2)
        if (n1 is not None) and (n2 is not None) and (n1.e_out.get(id2) is None) and (weight >= 0):
            n1.e_out[id2] = weight
            n2.e_in[id1] = weight
            e = {"src": id1, "w": weight, "dest": id2}
            self.edges.append(e)
            self.ec += 1
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Override interface method, adds a new node to the graph with a given key and (optional) a pos Tuple.
        if such key already exist in graph returns False and does nothing.
        mc updated relatively.
        """
        if node_id in self.nodes:
            return False
        n = Node(node_id, pos)
        self.nodes[node_id] = n
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Override interface method, deletes a node off this graph, and all edges associated with it.
        if node is not related to this graph does nothing and returns False
        """
        if node_id not in self.nodes:
            return False
        n = self.nodes[node_id]
        edges_in = n.e_in
        edges_out = n.e_out
        for i in edges_in:
            self.nodes[i].e_out.pop(node_id)
            self.ec -= 1

        for j in edges_out:
            self.nodes[j].e_in.pop(node_id)
            self.ec -= 1

        delete = []
        for k in self.edges:
            if (k['src'] is node_id) or (k['dest'] is node_id):
                delete.append(k)
        for i in delete:
            self.edges.remove(i)
        self.nodes.pop(node_id)
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        n1 = self.nodes.get(node_id1)
        n2 = self.nodes.get(node_id2)
        e = {'src': node_id1, 'w': n1.e_out.get(node_id2), 'dest': node_id2}
        if not self.edges.__contains__(e):
            return False
        n1.e_out.pop(node_id2)
        n2.e_in.pop(node_id1)
        self.edges.remove(e)
        self.ec -= 1
        self.mc += 1
        return True


def main():
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
        g.add_edge(i-1, i, i * 10)
    print(g.edges)
    g.remove_edge(0, 9)
    g.remove_node(100)
    print(g.edges)


if __name__ == '__main__':
    main()
