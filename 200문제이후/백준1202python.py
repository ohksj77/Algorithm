import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
mv = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = [int(sys.stdin.readline()) for _ in range(k)]
mv.sort()
k.sort()
ans = 0
q = []
for i in k:
    while mv and mv[0][0] <= i:
        heapq.heappush(q, -heapq.heappop(mv)[1])
    if q:
        ans -= heapq.heappop(q)
sys.stdout.write(str(ans))
