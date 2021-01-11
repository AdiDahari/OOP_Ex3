import json
from networkx import DiGraph
from networkx import strongly_connected_components as scc
from networkx import shortest_path as sp


def load_from_json_nx(file_name: str) -> DiGraph:
    gnx = DiGraph()
    edges = []
    try:
        with open(file_name, "r") as f:
            loaded = json.load(f)
            for i in loaded.get("Nodes"):
                id_key = i.get("id")
                gnx.add_node(id_key)
            for i in loaded.get("Edges"):
                src = i.get("src")
                w = i.get("w")
                dest = i.get("dest")
                if src is dest:
                    continue
                edges.append((src, dest, w))
            gnx.add_weighted_edges_from(edges)
        return gnx
    except IOError:
        print("Couldn't load graph. No changes made")


import time


def test_v10_e80():
    print("|V| = 10, |E| = 80:")
    g1 = load_from_json_nx("../Graphs/Circle/G_10_80_1.json")
    start = time.time()
    sp(g1, source=0, target=8)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    scc(g1)
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v100_e800():
    print("|V| = 100, |E| = 800:")
    g2 = load_from_json_nx("../Graphs/Circle/G_100_800_1.json")
    start = time.time()
    sp(g2, source=0, target=80)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    scc(g2)
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v1000_e8000():
    print("|V| = 1000, |E| = 8000:")
    g3 = load_from_json_nx("../Graphs/Circle/G_1000_8000_1.json")
    start = time.time()
    sp(g3, source=0, target=800)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    scc(g3)
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v10000_e80000():
    print("|V| = 10000, |E| = 80000:")
    g4 = load_from_json_nx("../Graphs/Circle/G_10000_80000_1.json")
    start = time.time()
    sp(g4, source=0, target=8000)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    scc(g4)
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v20000_e160000():
    print("|V| = 20000, |E| = 160000:")
    g5 = load_from_json_nx("../Graphs/Circle/G_20000_160000_1.json")
    start = time.time()
    sp(g5, source=0, target=16000)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    scc(g5)
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v30000_e240000():
    print("|V| = 30000, |E| = 240000:")
    g6 = load_from_json_nx("../Graphs/Circle/G_30000_240000_1.json")
    start = time.time()
    sp(g6, source=0, target=24000)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    scc(g6)
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def main():
    print("TimeTest started.\n\n")
    test_v10_e80()
    test_v100_e800()
    test_v1000_e8000()
    test_v10000_e80000()
    test_v20000_e160000()
    test_v30000_e240000()
    print("TimeTest ended.")


if __name__ == '__main__':
    main()