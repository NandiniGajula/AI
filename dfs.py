def dfs(graph, start, goal):
    visited = []
    stack = []
    stack.append(start)
    path = ""
    found = False
    
    while stack:
        m = stack.pop()
        path += m + " "
        visited.append(m)
        
        if m == goal:
            found = True
            break
        
        for neighbour in graph.get(m, []):
            if neighbour not in visited and neighbour not in stack:
                stack.append(neighbour)
    
    if found:
        print("Goal node found")
        print("Path:", path)
    else:
        print("Goal node not found")

n = int(input("Enter no. of nodes: "))
graph = {}

for i in range(n):
    key = input("Enter the parent node: ")
    value = input("Enter the child nodes (space-separated): ").split()
    graph[key] = value

start = input("Enter start node: ")
goal = input("Enter goal node: ")
dfs(graph, start, goal)