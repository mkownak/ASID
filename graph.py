from enum import Enum
from typing import Any, Optional, Dict, List, Set
import graphviz


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self,data:Any, index:int=0):
        self.data=data
        self.index=index

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self,source:Vertex,destination:Vertex,weight:Optional[float]=None):
        self.source=source
        self.destination=destination
        self.weight=weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies={}
        self.current_index=0;

    def create_vertex(self, data: Any) -> Vertex:
        vertex = Vertex(data)
        vertex.index = self.current_index
        self.current_index += 1
        self.adjacencies[vertex] = []
        return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge1 = Edge(source, destination, weight)
        edge2 = Edge(destination, source, weight)
        self.adjacencies[source].append(edge1)
        self.adjacencies[destination].append(edge2)

    def add_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None, edge_type: EdgeType = EdgeType.directed) -> None:
        if edge_type == EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def __str__(self):
        result = ""
        for vertex, edges in self.adjacencies.items():
            neighbors = []
            for edge in edges:
                neighbors.append(f"{edge.destination.index}: {edge.destination.data}")
            result += f"{vertex.index}: {vertex.data} ----> {neighbors}\n"
        return result

    def show(self):
        dot = graphviz.Digraph(comment='Graph')
        for vertex in self.adjacencies:
            dot.node(str(vertex.index), vertex.data)
        for vertex, edges in self.adjacencies.items():
            for edge in edges:
                dot.edge(str(edge.source.index), str(edge.destination.index))
        dot.render('graph', view=True)

    def get_neighbors(self, vertex: Vertex) -> List[Vertex]:
        neighbors = []
        for edge in self.adjacencies[vertex]:
            neighbors.append(edge.destination)
        return neighbors

    def depth_first_search_recursive(self, vertex: Vertex, visited: Set[Vertex]) -> None:
        visited.add(vertex)
        for neighbor in self.get_neighbors(vertex):
            if neighbor not in visited:
                self.depth_first_search_recursive(neighbor, visited)

    def depth_first_search(self, start_vertex: Vertex) -> List[Vertex]:
        visited = set()
        self.depth_first_search_recursive(start_vertex, visited)
        return list(visited)
    







g = Graph()
v0 = g.create_vertex("v0")
v1 = g.create_vertex("v1")
v2 = g.create_vertex("v2")
v3 = g.create_vertex("v3")
v4 = g.create_vertex("v4")
v5 = g.create_vertex("v5")
g.add_edge(v0, v1)
g.add_edge(v0, v5)
g.add_edge(v1, v2)
g.add_edge(v1, v4)
g.add_edge(v2, v3)
g.add_edge(v3, v4)
g.add_edge(v4, v5)

print(g)
#g.show()
