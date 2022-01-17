import sys
n = int(sys.stdin.readline())
parent = [0] * (n + 1)
result = [0] * (n + 1)
graphSize = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graphSize[a] += 1
    graphSize[b] += 1
while 1 in graphSize:
    for i in range(1, n + 1):
        if graphSize[i] == 1:
            parent[i] = graph[i][0]
            graphSize[i] = 0
            graphSize[parent[i]] -= 1
            graph[parent[i]].remove(i)
while any(parent):
    for i in range(1, n + 1):
        if parent[i] != 0:
            if parent[parent[i]] == 0:
                result[i] = result[parent[i]] + 1
                parent[i] = 0
for i in range(1, n + 1):
    print(result[i], end=' ')
