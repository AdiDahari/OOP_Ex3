

# Directed Weighted Graph - Python

**Authors:** Tommy Goroh and Adi Dahari.



## Description
This project is an implementation of Directed Weighted Graphs coded in Python language.
it includes an implementation of 2 interfaces:
1. **GraphInteface:**
	Implemented by DiGraph class, handles the structure of the graph and the basic actions made on it 
	(such as: adding nodes or edges, deleting node or edges, etc...)
	
2. **GraphAlgoInterface:**
	Implemented by GraphAlgo class. holds a bunch of methods and algorithms which can be applied on directed weighted graphs.
	(such as: finding the shortest path between 2 nodes on graph, saving and loading grpahs, etc...)
	this class also contains the visual plotting method of a directed weighted graph, implemented using matplotlib lib.


## Structure



### Directed Weighted Graph
(DiGraph.py - implements GraphInterface.py, GraphAlgo.py - implements GraphAlgoInterface.py)
#### Structure:
##### Node
a class for creating and handling nodes in graph. contains	a Constructor(init) that implements a key for the the new node, can also implement a location(x,y,z), a dict of in edges and a dict of out edges. if location isn't implemented the constructor randomizes a location (relatively to the given coordinates of the example graphs).

##### DiGraph
a class for creating and manipulating a directed weighted graph.
contains a constructor that creates a new graph by:
1. nodes dict, keyed by the nodes' keys.
2. edges dict, each edge is represented as dict with a src node's key, a weight value and a dest node's key (in that specific order).
3. ec(Edge Counter) is for getting the number of edges in graph efficiently.
4. mc(Mode Counter) is for counting the changes made in graph since implemented.

each graph implemented has the following methods:
* **v_size =** for getting the number of nodes in graph.
* **e_size =** for getting the number of edges in graph.
* **get_all_v =** for getting all nodes in the format: (key, |edges out|, |edges in|)
* **all_in_edges_of_node(id) =** gets all the in edges of a node related to the id given.
* **all_out_edges_of_node(id) =** gets all the out edges of a node related to the id given.
* **get_mc =** for getting the mode counter of the graph.
* **add_edge(id1, id2, weight) =** connects an edge between id1 and id2 with the given weight if not already connected
* **add_node(node_id, pos) =** creates a new node in graph with the given key, if not already exists.
(optional: location Tuple)
**remove_node (node_id)=** if exists, deletes the node and all edges associated with it off the graph.
**remove_edge(node_id1, node_id2) =** if exists, removes the edge connected out of node_id1 and in to node_id2.

##### GraphAlgo
a class for applying complicated methods and algorithms on a directed weighted graph.
Constructor: initializing an underlying graph for methods to be applied on. creates a new one if not given any.

each GraphAlgo can be applied with the following methods:
* **get_graph =** for getting a pointer to of the underlying graph.
* **load_from_json(file_name) =** for loading and initializing a graph given as a json file, given as a string which represents the path of file in memory. if loading process failed, no changes made to the current graph if exists.
* **save_to_json(file_name) =** for saving the underlying graph to a json formatted file, in the specific path given. saving format has been adapted to match the graphs given as examples.
* **shortest_path(id1, id2)** this method calculates the lowest weighted path of nodes between 2 given keys. each edge on the way has a weight (float) value which is summed up for each path available. the shortest path is **not** the one with the least nodes in it, but the one with the lowest weight of edges. this method returns a Tuple with 2 values: weight of path and ordered list of keys representing the path. example: (weight, [path])-->(123.2312, [1,2,3,4,5,6,12,0]). this method is based on the idea of Dijkstra's algorithm*(1).
* **connected_component(id1) =** this method gets all nodes in graph which are strongly connected to the given key's node. as it checks both ways of connection between each node and the given one, it uses 2 iterations: once on the out-going edges of the given node and second on the in-going edges of it. this method also uses the Dijkstra algorithm idea.
* **connected_components() =** This method returns a list of lists, representing all connected components in the underlying graph. this method implementation uses the Tarjan's algorithm idea in an iterative way, mainly for applying the method on a large scaled graphs (more than 10,000 nodes and 80,000 edges). using Tarjan's algorithm*(2) in an iterative way makes each call for the method very efficient and fast.
* **plot_graph =** This method transposes the graph from a data structure to a visual representation. does so by using matplotlib functions and visualization abilities. each node on graph is represented as a red dot on screen with it's key above it. each edge on graph is represented as an arrow out of the src node pointing to the dest node. each node's position is translated (automatically by matplotlib's algorithms) to a specific dot(x,y) on screen. 

##### Tarjan
This class made specifically for the connected components implementation. it receives a graph's nodes and edges for searching the full list of lists of connected components, as the recursive version of this algorithms returns a memory error when working on large-scale graphs (because of a large amount of recursive calls), it has been converted to an iterative implementation.

## References
* *(1) - for further information about the Dijkstra's Algorithm and how it works: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
* *(2) - for further information about Tarjan's Algorithm and how it works: https://en.wikipedia.org/wiki/Tarjan%27s_algorithm
* for more information about directed weighted graphs: https://en.wikipedia.org/wiki/Directed_graph
* Sources for implementation ideas:
	1. William Fiset youtube video with Tarjan's algorithm visual explanation: https://www.youtube.com/watch?v=wUgWX0nc4NY&t=376s
	2. Jesper Öqvist's blog with an iterative version of Tarjan's algorithm: https://llbit.se/?p=3379
	3. Computer Science youtube video with Dijkstra's Algorithm visual explanation: https://www.youtube.com/channel/UCSX3MR0gnKDxyXAyljWzm0Q


