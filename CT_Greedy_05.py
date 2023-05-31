# ---------- Import -----
from collections import defaultdict
import sys
input = sys.stdin.readline

# ---------- Function ----------
def comb(n, k):
    def factorial(N):
        if N == 0 or N == 1:
            return 1
        
        dp = [0] * (N+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, N+1):
            dp[i] = i * dp[i-1]

        return dp[N]
    
    top = factorial(n)
    btm = factorial(n-k) * factorial(k)

    return top // btm

# ---------- Main ----------
N, M = map(int, input().split())
ballList = list(map(int, input().split()))

ballDict = defaultdict(int)
for ball in ballList:
    ballDict[ball] += 1

minusCnt = 0
for value in ballDict.values():
    if value > 1:
        minusCnt += comb(value, 2)

allCnt = comb(N, 2)
result = allCnt - minusCnt
print(result)