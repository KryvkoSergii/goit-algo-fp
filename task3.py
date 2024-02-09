import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, start, end, weight):
        self.vertices[start].append((end, weight))
        self.vertices[end].append((start, weight))

def dijkstra(graph, start):
    heap = [(0, start)]  # Початкова вершина з вагою 0
    visited = set()

    while heap:
        (current_distance, current_vertex) = heapq.heappop(heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight

            if neighbor not in visited:
                heapq.heappush(heap, (distance, neighbor))

    return visited

def main():
    # Створення графа
    graph = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2), ('B', 'D', 5),
             ('C', 'D', 1), ('D', 'E', 7), ('E', 'F', 2)]

    for vertex in vertices:
        graph.add_vertex(vertex)

    for edge in edges:
        graph.add_edge(*edge)

    # Виклик алгоритму Дейкстри
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    print("Найкоротші шляхи від вершини", start_vertex, "до інших вершин:", shortest_paths)

if __name__ == "__main__":
    main()
