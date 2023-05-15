# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
location = list(input().rstrip())

X, Y = ord(location[0])-96, int(location[1])
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

cnt = 0
for index in range(8):
    nx = X + dx[index]
    ny = Y + dy[index]
    
    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        continue
    else:
        cnt += 1
        
print(cnt)