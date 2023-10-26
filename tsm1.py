import itertools

# Function to calculate the total distance of a path
def calculate_total_distance(path, graph):
    total_distance = 0
    path_with_weights = []
    for i in range(len(path) - 1):
        source = path[i]
        destination = path[i + 1]
        distance = graph[source][destination]
        total_distance += distance
        path_with_weights.append(f"{source} -({distance})-> {destination}")
    return total_distance, path_with_weights

# Input the number of nodes
num_nodes = int(input("Enter the number of nodes: "))

# Initialize an empty graph as a dictionary
graph = {}

# Input the connections and weights
for i in range(num_nodes):
    node_name = input(f"Enter the name of node {i+1}: ")
    num_outgoing_connections = int(input(f"Enter the number of outgoing connections from {node_name}: "))
    connections = {}
    for j in range(num_outgoing_connections):
        connected_node, weight = input(f"Enter connected node and weight (e.g., B 5): ").split()
        connections[connected_node] = int(weight)
    graph[node_name] = connections

# Ask for the starting position
start_node = input("Enter the starting node: ")

# Generate all possible permutations of nodes starting from the specified node
nodes = list(graph.keys())
nodes.remove(start_node)
permutations = itertools.permutations(nodes)

# Initialize variables to track the shortest distance
shortest_distance = float('inf')
shortest_paths = []

# Print all possible paths, calculate the shortest distance, and paths with weights
print("All Possible Paths:")
for perm in permutations:
    current_path = list(perm)
    total_distance, path_with_weights = calculate_total_distance([start_node] + current_path + [start_node], graph)
    print(" -> ".join(path_with_weights))
    print(f"Total Distance: {total_distance}")
    if total_distance < shortest_distance:
        shortest_distance = total_distance
        shortest_paths = [(start_node,) + tuple(current_path) + (start_node,)]
    elif total_distance == shortest_distance:
         shortest_paths.append((start_node,) + tuple(current_path) + (start_node,))

# Print the shortest distance and paths of the shortest distance
print("\nShortest Distance and Paths of Shortest Distance:")
print(f"Shortest Distance: {shortest_distance}")
print("Shortest Paths:")
for path in shortest_paths:
    total_distance, path_with_weights = calculate_total_distance(path, graph)
    print(" -> ".join(path_with_weights))
    print(f"Total Distance: {total_distance}")
