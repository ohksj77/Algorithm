import sys
from collections import deque
ladder, snake = map(int, sys.stdin.readline().split())
visited = [0] * 101
graph = [i for i in range(101)]
laddersnake = [list(map(int, sys.stdin.readline().split())) for _ in range(ladder + snake)]
for i in laddersnake:
    graph[i[0]] = i[1]
def bfs():
    q = deque()
    q.append(1)
    while q:
        n = q.popleft()
        for i in range(1, 7):
            tmp = n + i
            if tmp > 100:
                continue
            count = graph[tmp]
            if visited[count] == 0:
                q.append(count)
                visited[count] = visited[n] + 1
                if count == 100:
                    return visited[100]
print(bfs())
