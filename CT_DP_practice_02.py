# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    tmp = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(tmp, dp[i//2] + 1)
    elif i % 3 == 0:
        dp[i] = min(tmp, dp[i//3] + 1)
    elif i % 5 == 0:
        dp[i] = min(tmp, dp[i//5] + 1)
    else:
        dp[i] = tmp
        
print(dp[N])