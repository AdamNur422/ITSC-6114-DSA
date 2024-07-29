import os
import heapq
from collections import defaultdict
from PIL import Image

def dijkstra(graph, source):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]
    paths = {vertex: [] for vertex in graph}
    paths[source] = [source]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                paths[neighbor] = paths[current_vertex] + [neighbor]

    return distances, paths

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
            graph[u.lower()][v.lower()] = w
            if graph_type == 'U':
                graph[v.lower()][u.lower()] = w

    return graph

def process_graph(file_path, image_path):
    graph = read_input(file_path)

    while True:
        source = input("Enter the source node: ").strip().lower()
        if source in graph:
            break
        else:
            print(f"Node {source} not found in the graph. Enter a valid source node.")

    distances, paths = dijkstra(graph, source)
    print(f"Single-source Shortest Paths from {source}")
    for vertex in distances:
        print(f"Path to {vertex}: {' -> '.join(paths[vertex])}, Cost: {distances[vertex]}")

    img = Image.open(image_path)
    img.show()

def main():
    while True:
        print("Choose the type of graph:")
        print("1. Undirected Graph")
        print("2. Directed Graph")

        choice = input("Enter 1 or 2: ").strip()

        if choice == '1':
            graph_type = 'undirected'
            break
        elif choice == '2':
            graph_type = 'directed'
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

    input_files = ['input1.txt', 'input2.txt', 'input3.txt','input4.txt']
    image_files = ['1.png', '2.png', '3.png', '4.png']

    while True:
        print("Choose the Graph:")
        for i, file_name in enumerate(input_files, start=1):
            print(f"{i}. {file_name}")

        file_choice = input("Enter the file number (1, 2, 3, or 4): ").strip()

        if file_choice in ['1', '2', '3', '4']:
            file_path = os.path.join('graphs', graph_type, input_files[int(file_choice) - 1])
            image_path = os.path.join('graphs', graph_type, image_files[int(file_choice) - 1])
            if os.path.exists(file_path) and os.path.exists(image_path):
                process_graph(file_path, image_path)
                break
            else:
                print(f"File {file_path} or {image_path} not found.")
        else:
            print("Invalid file choice. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
