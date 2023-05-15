# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
num = input().rstrip()
cnt0, cnt1 = 0, 0

if num[0] == "1":
    cnt0 += 1
else:
    cnt1 += 1
        
for i in range(len(num)-1):
    if num[i] != num[i+1]:
        if num[i+1] == "1":
            cnt0 += 1
        else:
            cnt1 += 1
            
print(min(cnt0, cnt1))