# ---------- Import ----------
import sys
ipnut = sys.stdin.readline

# ---------- Main ----------
N = int(input())
cnt = 0

coins = [500, 100, 50, 10]

for coin in coins:
    cnt += N // coin
    N %= coin
    
print(cnt)