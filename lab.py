from py_alg_dat.graph import DirectedWeightedGraph
from py_alg_dat.graph_vertex import UnWeightedGraphVertex
from py_alg_dat.graph_algorithms import GraphAlgorithms


def create_graph():
    graph = DirectedWeightedGraph(7)

    vertex0 = UnWeightedGraphVertex(graph, "A")
    vertex1 = UnWeightedGraphVertex(graph, "B")
    vertex2 = UnWeightedGraphVertex(graph, "C")
    vertex3 = UnWeightedGraphVertex(graph, "D")
    vertex4 = UnWeightedGraphVertex(graph, "E")
    vertex5 = UnWeightedGraphVertex(graph, "F")
    vertex6 = UnWeightedGraphVertex(graph, "G")

    graph.add_vertex(vertex0)
    graph.add_vertex(vertex1)
    graph.add_vertex(vertex2)
    graph.add_vertex(vertex3)
    graph.add_vertex(vertex4)
    graph.add_vertex(vertex5)
    graph.add_vertex(vertex6)

    graph.add_edge(vertex0, vertex1, 7)
    graph.add_edge(vertex1, vertex2, 2)
    graph.add_edge(vertex1, vertex6, 3)
    graph.add_edge(vertex2, vertex3, 2)
    graph.add_edge(vertex2, vertex6, 4)
    graph.add_edge(vertex3, vertex4, 5)
    graph.add_edge(vertex3, vertex6, 1)
    graph.add_edge(vertex4, vertex5, 6)
    graph.add_edge(vertex5, vertex0, 1)
    graph.add_edge(vertex5, vertex6, 4)
    graph.add_edge(vertex6, vertex0, 7)
    graph.add_edge(vertex6, vertex4, 1)

    return graph


print GraphAlgorithms.kruskals_algorithm(create_graph())
