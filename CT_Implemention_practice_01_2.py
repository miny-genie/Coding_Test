# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
hh = int(input())

cnt = 0
for Hour in range(hh + 1):
    for Minute in range(60):
        for Second in range(60):
            if "3" in str(Hour) + str(Minute) + str(Second):
                cnt += 1
                
print(cnt)