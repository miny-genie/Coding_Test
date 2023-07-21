# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())    # 4
ant_nest = list(map(int, input().split()))  # 1 3 1 5

dp = [0] * (N+3)

for i in range(N):
    dp[i+3] = ant_nest[i] + max(dp[i], dp[i+1])

print(max(dp))