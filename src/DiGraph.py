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
        return f"{self.key}"

    def __repr__(self):
        """
        Override method for string representation of a node.
        """
        return f"{self.key}: |edges out| {len(self.e_out)} |edges in| {len(self.e_in)}"

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

    def get_edge(self, other_key: int) -> float:
        return self.e_out[other_key]


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
        return f"Graph: |V|={self.v_size()} , |E|={self.e_size()}"

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
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.ec

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        if id1 in self.nodes:
            n = self.nodes.get(id1)
            return n.e_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if id1 in self.nodes:
            n = self.nodes.get(id1)
            return n.e_out

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
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
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id in self.nodes:
            return False
        n = Node(node_id, pos)
        self.nodes[node_id] = n
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
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
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
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
