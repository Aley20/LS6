# 1
def Graphe(S,L):
    res={S[i]:{L[i]} for i in range(len(S))}
    return res
    
S=['x1','x2','x3','x4']
L=['x2','x4',('x1','x4'),'x4']
print (Graphe(S,L))

# 2
def PrintG(D) :
    for (k, v) in D.items():
        print(k,v)  

PrintG(Graphe(S,L))

# 3
def DFS(graph, start, visited, pre, post, clock):
    visited[start] = True
    pre[start] = clock[0]
    clock[0] += 1
    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited, pre, post, clock)
    post[start] = clock[0]
    clock[0] += 1

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = dict.fromkeys(graph.keys(), False)
pre, post = {}, {}
clock = [1]

for node in graph:
    if not visited[node]:
        DFS(graph, node, visited, pre, post, clock)

print(pre)
print(post)


