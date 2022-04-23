import sys
weight = int(sys.stdin.readline())
sys.stdout.write("YES" if weight % 2 == 0 and weight != 2 else "NO")
