# -------------------------------------------------- Lucky Strike --------------------------------------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = input().rstrip()
arr = []

for i in N:
    arr.append(int(i))
    
tmp = 0
for i in range(len(arr)//2):
    tmp += arr[i]

if sum(arr)-tmp == tmp:
    print("LUCKY")
else:
    print("READY")