# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
fear = list(map(int, input().split()))
fear.sort()

totalGroup = 0
pplCnt = 0

for i in fear:
    pplCnt += 1
    if pplCnt >= i:
        totalGroup += 1
        pplCnt = 0
        
print(totalGroup)