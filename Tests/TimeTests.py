from src.GraphAlgo import GraphAlgo
import time


def test_v10_e80():
    print("|V| = 10, |E| = 80:")
    g1 = GraphAlgo()
    g1.load_from_json("../Graphs/Circle/G_10_80_1.json")
    start = time.time()
    g1.shortest_path(0, 8)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    g1.connected_components()
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v100_e800():
    print("|V| = 100, |E| = 800:")
    g2 = GraphAlgo()
    g2.load_from_json("../Graphs/Circle/G_100_800_1.json")
    start = time.time()
    g2.shortest_path(0, 80)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    g2.connected_components()
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v1000_e8000():
    print("|V| = 1000, |E| = 8000:")
    g3 = GraphAlgo()
    g3.load_from_json("../Graphs/Circle/G_1000_8000_1.json")
    start = time.time()
    g3.shortest_path(0, 800)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    g3.connected_components()
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v10000_e80000():
    print("|V| = 10000, |E| = 80000:")
    g4 = GraphAlgo()
    g4.load_from_json("../Graphs/Circle/G_10000_80000_1.json")
    start = time.time()
    g4.shortest_path(0, 8000)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    g4.connected_components()
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v20000_e160000():
    print("|V| = 20000, |E| = 160000:")
    g5 = GraphAlgo()
    g5.load_from_json("../Graphs/Circle/G_20000_160000_1.json")
    start = time.time()
    g5.shortest_path(0, 16000)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    g5.connected_components()
    end = time.time()
    print(f"Connected Components = {end - start}\n")


def test_v30000_e240000():
    print("|V| = 30000, |E| = 240000:")
    g6 = GraphAlgo()
    g6.load_from_json("../Graphs/Circle/G_30000_240000_1.json")
    start = time.time()
    g6.shortest_path(0, 24000)
    end = time.time()
    print(f"Shortest Path = {end - start}")
    start = time.time()
    g6.connected_components()
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
