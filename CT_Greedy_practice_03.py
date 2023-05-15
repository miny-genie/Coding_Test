# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
min_lst = []
row, column = map(int, input().split())

for _ in range(row):
    min_num = list(map(int, input().split()))
    min_lst.append(min(min_num))
    
print(max(min_lst))