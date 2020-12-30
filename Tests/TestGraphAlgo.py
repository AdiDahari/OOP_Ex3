from math import inf
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)
            g.add_edge(i-1, i, 1)
        ga = GraphAlgo(g)
        self.assertEqual(g, ga.get_graph())

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        g = DiGraph()
        for i in range(1000):
            g.add_node(i)
            g.add_edge(i-1, i, i)
        ga = GraphAlgo(g)
        self.assertEqual(499500, ga.shortest_path(0, 999)[0])
        self.assertEqual(1000, len(ga.shortest_path(0, 999)[1]))
        g.add_edge(0, 999, 5)
        self.assertEqual(5, ga.shortest_path(0, 999)[0])
        self.assertEqual(2, len(ga.shortest_path(0, 999)[1]))
        g1 = DiGraph()
        for i in range(4):
            g1.add_node(i)
        g1.add_edge(0, 1, 1)
        g1.add_edge(1, 0, 1)
        g1.add_edge(0, 2, 1)
        g1.add_edge(2, 0, 1)
        g1.add_edge(2, 3, 3)
        g1.add_edge(3, 2, 3)
        g1.add_edge(1, 3, 2)
        g1.add_edge(3, 1, 2)
        ga1 = GraphAlgo(g1)
        self.assertEqual(3, ga1.shortest_path(0, 3)[0])
        g1.remove_edge(1, 3)
        self.assertEqual(4, ga1.shortest_path(0, 3)[0])
        self.assertEqual(0, ga1.shortest_path(0, 0)[0])
        self.assertEqual(inf, ga1.shortest_path(0, 4)[0])


    def test_connected_component(self):
        self.fail()

    def test_connected_components(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()
