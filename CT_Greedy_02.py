# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
num = input().rstrip()

result = 0
for i in num:
    if int(i) < 2 or result < 2:
        result += int(i)
    else:
        result *= int(i)
        
print(result)