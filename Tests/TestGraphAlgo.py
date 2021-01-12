from math import inf
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        g1 = DiGraph()
        for i in range(100):
            g1.add_node(i)
            g1.add_edge(i - 1, i, 1)
        ga1 = GraphAlgo(g1)
        self.assertEqual(g1, ga1.get_graph())

    def test_load_from_json(self):
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json("C:/Users/Adi Dahari/Desktop/OOP-_Ex3/data/A0"))
        self.assertFalse(ga.load_from_json("C:/Users/Adi Dahari/Desktop/OOP-_Ex3/data/NoSuchFile"))
        ga_equal = GraphAlgo()
        ga_equal.load_from_json("C:/Users/Adi Dahari/Desktop/OOP-_Ex3/data/A0")
        self.assertEqual(ga.get_graph().__str__(), ga_equal.get_graph().__str__())

    def test_save_to_json(self):
        ga4 = GraphAlgo()
        ga4.load_from_json("C:/Users/Adi Dahari/Desktop/OOP-_Ex3/data/A0")
        self.assertFalse(ga4.save_to_json("C:/Users/Adi Dahari/Desktop/Test/testG"))
        self.assertTrue(ga4.save_to_json("C:/Users/Adi Dahari/Desktop/OOP-_Ex3/data/A0_testsave1"))
        ga4_loaded = GraphAlgo()
        ga4_loaded.load_from_json("C:/Users/Adi Dahari/Desktop/OOP-_Ex3/data/A0_testsave1")
        self.assertEqual(ga4.get_graph().__str__(), ga4_loaded.get_graph().__str__())

    def test_shortest_path(self):
        g2 = DiGraph()
        for i in range(1000):
            g2.add_node(i)
            g2.add_edge(i - 1, i, i)
        ga2 = GraphAlgo(g2)
        self.assertEqual(499500, ga2.shortest_path(0, 999)[0])
        self.assertEqual(1000, len(ga2.shortest_path(0, 999)[1]))
        g2.add_edge(0, 999, 5)
        self.assertEqual(5, ga2.shortest_path(0, 999)[0])
        self.assertEqual(2, len(ga2.shortest_path(0, 999)[1]))
        g3 = DiGraph()
        for i in range(4):
            g3.add_node(i)
        g3.add_edge(0, 1, 1)
        g3.add_edge(1, 0, 1)
        g3.add_edge(0, 2, 1)
        g3.add_edge(2, 0, 1)
        g3.add_edge(2, 3, 3)
        g3.add_edge(3, 2, 3)
        g3.add_edge(1, 3, 2)
        g3.add_edge(3, 1, 2)
        ga3 = GraphAlgo(g3)
        self.assertEqual(3, ga3.shortest_path(0, 3)[0])
        g3.remove_edge(1, 3)
        self.assertEqual(4, ga3.shortest_path(0, 3)[0])
        self.assertEqual(0, ga3.shortest_path(0, 0)[0])
        self.assertEqual(inf, ga3.shortest_path(0, 4)[0])

    def test_connected_component(self):
        g5 = DiGraph()
        for i in range(1000):
            g5.add_node(i)
            g5.add_edge(i-1, i, 1)
            if i%100 != 0:
                g5.add_edge(i, i-1, 1)
        ga5 = GraphAlgo(g5)
        self.assertEqual(len(ga5.connected_component(0)), 100)
        ga5.get_graph().add_edge(100, 99, 1)
        self.assertEqual(len(ga5.connected_component(0)), 200)

    def test_connected_components(self):
        g6 = DiGraph()
        for i in range(1000):
            g6.add_node(i)
            g6.add_edge(i - 1, i, 1)
            if i % 100 != 0:
                g6.add_edge(i, i - 1, 1)
        ga6 = GraphAlgo(g6)
        self.assertEqual(len(ga6.connected_components()), 10)
        ga6.get_graph().add_edge(100, 99, 1)
        self.assertEqual(len(ga6.connected_components()), 9)
