class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)

    def print_graph(self):
        for vertex in range(self.num_vertices):
            print("Các đỉnh kề với đỉnh", vertex)
            for adjacent_vertex in self.adj_list[vertex]:
                print(adjacent_vertex, end=" ")
            print("\n")

# Sử dụng đoạn mã trên để tạo và in đồ thị
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_graph()


