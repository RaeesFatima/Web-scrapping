def dfs (graph,start):
    stack=[start]
    visited=set()

    order=[]

    while stack:
        node=stack.pop()
       

        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            order.append(node)
            
            for i in range(len(graph[node])-1,-1,-1):
                neighbor=graph[node][i]
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return order

graph={
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result=dfs(graph,'A')
print('here is the result of dfs: ',result)