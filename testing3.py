def dfs(graph,start):
    stack=[start]
    visited=set()

    order=[]
    while stack:
        node=stack.pop()

        if node not in visited:
            # print(node,end=" ")
            visited.add(node)
            order.append(node)

            for i in range(len(graph[node])-1,-1,-1):
                neighbor=graph[node][i]
                if neighbor not in visited:
                    stack.append(neighbor)
    return order

graph = {
    '0': ['1', '2'],  
    '1': ['0','2'],
    '2': ['0','1','2','3','4'],
    '3': ['2'],
    '4': ['2'],
}

print("DFS Traversal:",dfs(graph, '1'))
# dfs(graph, '1')  # Expected Output: A B D E F C