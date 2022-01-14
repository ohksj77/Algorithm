from itertools import combinations
import sys
n = int(sys.stdin.readline())
member_lst = list(i for i in range(n))
score_map = []
for _ in range(n) :
    score_map.append(list(map(int, sys.stdin.readline().split())))
ans = 10**8
for i in range(1, int((n/2)+1)) :
    member_divide = combinations(member_lst, i)
    min_diff = 10**8
    for x in member_divide :
        start_lst = list(x)
        link_lst = list(set(member_lst) - set(start_lst))
        start_all_sum = 0
        link_all_sum = 0
        for j in range(n-1):
            for k in range(n-1):
                try :
                    start_sum = score_map[start_lst[j]][start_lst[k]]
                except IndexError:
                    start_sum = 0
                try :
                    link_sum = score_map[link_lst[j]][link_lst[k]]
                except IndexError:
                    link_sum = 0
                start_all_sum += start_sum
                link_all_sum += link_sum
        diff = abs(start_all_sum - link_all_sum)
        min_diff = min(min_diff, diff)
    ans = min(ans, min_diff)
print(ans)
