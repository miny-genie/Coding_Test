# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = input().rstrip()    # 1mklem12k3mk12l4m12mk321mkl123mlk

resultStr = []
resultNum = 0

for i in N:
    if ord(i) < 60:
        resultNum += int(i)
    else:
        resultStr.append(i)

resultStr.sort()
for s in resultStr:
    print(s, end="")
print(resultNum)
