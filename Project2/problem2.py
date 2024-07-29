import os
import timeit
from collections import defaultdict

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v in graph[u]:
            if (u, v, graph[u][v]) not in edges and (v, u, graph[u][v]) not in edges:
                edges.append((graph[u][v], u, v))
    edges.sort()

    vertices = list(graph.keys())
    ds = DisjointSet(vertices)

    mst = []
    total_cost = 0

    for edge in edges:
        weight, u, v = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_vertices, num_edges, graph_type = lines[0].strip().split()
    num_vertices = int(num_vertices)
    num_edges = int(num_edges)
    graph = defaultdict(dict)

    for line in lines[1:]:
        parts = line.strip().split()
        if len(parts) == 3:
            u, v, w = parts
            w = int(w)
            graph[u][v] = w
            graph[v][u] = w

    return graph

def process_graph(file_path):
    graph = read_input(file_path)
    
    start_time = timeit.default_timer()
    mst, total_cost = kruskal(graph)
    end_time = timeit.default_timer()
    
    runtime = end_time - start_time

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
    print(f"Total cost of MST: {total_cost}")
    print(f"Runtime algorithm: {runtime:.10f} seconds")

def main():
    input_files = ['input1.txt', 'input2.txt', 'input3.txt', 'input4.txt']

    while True:
        print("Choose the Graph:")
        for i, file_name in enumerate(input_files, start=1):
            print(f"{i}. {file_name}")

        file_choice = input("Enter the file number (1, 2, 3, or 4): ").strip()
        
        if file_choice in ['1', '2', '3', '4']:
            file_path = os.path.join('graphs', 'undirected', input_files[int(file_choice) - 1])
            if os.path.exists(file_path):
                process_graph(file_path)
                break
            else:
                print(f"File {file_path} not found.")
        else:
            print("Invalid file choice. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
