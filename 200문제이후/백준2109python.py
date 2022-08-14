import heapq
import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])
queue = []
for p, d in arr:
    heapq.heappush(queue, p)
    if d < len(queue):
        heapq.heappop(queue)
sys.stdout.write(str(sum(queue)))
