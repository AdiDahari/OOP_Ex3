from unittest import TestCase
from DiGraph import DiGraph, Node


class TestDiGraph(TestCase):

    def test_v_size(self):
        g = DiGraph()
        for i in range(5):
            g.add_node(i)
        self.assertEqual(g.v_size(), 5)
        g.remove_node(5)
        self.assertEqual(g.v_size(), 5)
        g.remove_node(4)
        self.assertNotEqual(g.v_size(), 5)
        for i in range(5, 100):
            g.add_node(i)
        self.assertEqual(g.v_size(), 99)
        g.add_node(4)
        self.assertEqual(g.v_size(), 100)

    def test_e_size(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)
            g.add_edge(i-1, i, 1)
        self.assertEqual(g.e_size(), 99)
        g.remove_edge(0, 1)
        self.assertEqual(g.e_size(), 98)
        g.remove_edge(1, 0)
        self.assertEqual(g.e_size(), 98)
        for i in range(1000):
            g.remove_edge(i, i+1)
        self.assertEqual(g.e_size(), 0)

    def test_get_all_v(self):
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        self.assertEqual(len(g), len(g.get_all_v()))

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)
            g.add_edge(i, 0, 1)
        self.assertEqual(len(g.all_in_edges_of_node(0)), 99)
        for i in range(2,100):
            g.remove_edge(i, 0)
        self.assertEqual(len(g.all_in_edges_of_node(0)), 1)

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        for i in range(100):
            g.add_node(i)
            g.add_edge(0, i, 1)
        self.assertEqual(len(g.all_out_edges_of_node(0)), 99)
        for i in range(2, 100):
            g.remove_edge(0, i)
        self.assertEqual(len(g.all_out_edges_of_node(0)), 1)

    def test_get_mc(self):
        g = DiGraph()
        for i in range(1000000):
            g.add_node(i)
            g.add_edge(i-1, i, 1)
        self.assertEqual(g.get_mc(), 1999999)

    def test_add_edge(self):
        g = DiGraph()
        for i in range(10):
            g.add_edge(i,i+1, 1)
        self.assertEqual(g.e_size(), 0)
        for i in range(2000):
            g.add_node(i)
            g.add_edge(i-1, i, 1)
        self.assertEqual(g.e_size(), 1999)
        for i in range(2000):
            g.add_edge(i, i, 1)
            g.add_edge(i-1, i, 1)
        self.assertEqual(g.e_size(), 1999)

    def test_remove_node(self):
        g = DiGraph()
        for i in range(10000):
            g.add_node(i)
            g.add_edge(0, i, 1)
            g.add_edge(i, 0, 1)
        self.assertEqual(g.e_size(), 19998)
        g.remove_node(0)
        self.assertEqual(g.v_size(), 9999)
        self.assertEqual(g.e_size(), 0)

    def test_remove_edge(self):
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
            g.add_edge(0, i, 1)
        g.remove_edge(0, 9)
        g.remove_edge(10002, 999)
        self.assertEqual(g.e_size(), 8)
        g.add_edge(0, 9, 1)
        g.remove_edge(9, 0)
        self.assertEqual(g.e_size(), 9)
