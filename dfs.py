def dfs(graph, start):

    stack = [start]  
    visited = set()  

    while stack:
        node = stack.pop()  # Remove last inserted node (LIFO)
        if node not in visited:
            print(node, end=" ")  # Process node
            visited.add(node)

            # Push neighbors manually (in reverse order to maintain correct order)
            for i in range(len(graph[node]) - 1, -1, -1):
                neighbor = graph[node][i]
                if neighbor not in visited:
                    stack.append(neighbor)

# Example Graph (Adjacency List)
graph={
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Traversal:")
dfs(graph, 'A')  # Expected Output: A B D E F C
